from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json
import uuid
import os

from src.creditcardDefault.pipeline.predict_pipeline import CustomData, PredictPipeline

cloud_config = {
    'secure_connect_bundle': 'secure-connect-creditcard.zip'
}

token_file_path = "creditcard-token.json"
if not os.path.isfile(token_file_path):
    print(f"Error: File not found: {token_file_path}")
    exit(1)

with open(token_file_path) as f:
    secrets = json.load(f)

CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]

auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

keyspace_name = 'database'
session.set_keyspace(keyspace_name)

table_name = 'credit_card1'

create_table_query = f"""
CREATE TABLE IF NOT EXISTS {keyspace_name}.{table_name} (
    id UUID PRIMARY KEY,
    sex INT,
    education INT,
    marital_status INT,
    age INT,
    limit_balance INT,
    pay_0 INT,
    pay_2 INT,
    pay_3 INT,
    pay_4 INT,
    pay_5 INT,
    pay_6 INT,
    total_bill_amount INT,
    total_pay_amount FLOAT
)
"""
session.execute(create_table_query)

application = Flask(__name__)
app = application

@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        data = CustomData(
            LIMIT_BAL=int(request.form.get('LIMIT_BAL')),
            AGE=int(request.form.get('AGE')),
            SEX=int(request.form.get('SEX')),
            EDUCATION=int(request.form.get('EDUCATION')),
            MARRIAGE=int(request.form.get('MARRIAGE')),
            PAY_0=int(request.form.get('PAY_0')),
            PAY_2=int(request.form.get('PAY_2')),
            PAY_3=int(request.form.get('PAY_3')),
            PAY_4=int(request.form.get('PAY_4')),
            PAY_5=int(request.form.get('PAY_5')),
            PAY_6=int(request.form.get('PAY_6')),
            TOTAL_BILL_AMT=int(request.form.get('TOTAL_BILL_AMT')),
            TOTAL_PAY_AMT=float(request.form.get('TOTAL_PAY_AMT'))
        )

        query = f"""
            INSERT INTO {table_name} (
                id, sex, education, marital_status, age, limit_balance,
                pay_0, pay_2, pay_3, pay_4, pay_5, pay_6, total_bill_amount, total_pay_amount
            )
            VALUES (
                uuid(), :sex, :education, :marital_status, :age, :limit_balance,
                :pay_0, :pay_2, :pay_3, :pay_4, :pay_5, :pay_6, :total_bill_amount, :total_pay_amount
            )
        """

        parameters = {
            'id': uuid.uuid4(),
            'sex': data.SEX,
            'education': data.EDUCATION,
            'marital_status': data.MARRIAGE,
            'age': data.AGE,
            'limit_balance': data.LIMIT_BAL,
            'pay_0': data.PAY_0,
            'pay_2': data.PAY_2,
            'pay_3': data.PAY_3,
            'pay_4': data.PAY_4,
            'pay_5': data.PAY_5,
            'pay_6': data.PAY_6,
            'total_bill_amount': data.TOTAL_BILL_AMT,
            'total_pay_amount': data.TOTAL_PAY_AMT
        }

        try:
            pred_df = data.get_data_as_data_frame()
            predict_pipeline = PredictPipeline()
            output = predict_pipeline.predict(pred_df)

            session.execute(
                f"INSERT INTO {keyspace_name}.{table_name} "
                "(id, sex, education, marital_status, age, limit_balance, "
                "pay_0, pay_2, pay_3, pay_4, pay_5, pay_6, "
                "total_bill_amount, total_pay_amount) "
                "VALUES "
                "(%(id)s, %(sex)s, %(education)s, %(marital_status)s, %(age)s, %(limit_balance)s, "
                "%(pay_0)s, %(pay_2)s, %(pay_3)s, %(pay_4)s, %(pay_5)s, %(pay_6)s, "
                "%(total_bill_amount)s, %(total_pay_amount)s)",
                parameters
            )
            print("Document inserted successfully.")
            
            if output == 0:
                msg = 'This Customer will pay the credit card payment on time'
                return render_template('result.html', results=msg)
            if output == 1:
                msg = 'This Customer will make a default in his/her payment!!!!'
                return render_template('result.html', results=msg)
        except Exception as e:
            print(f"Error inserting document: {e}")
            #
            return "Error inserting document"

        # Returning a default response
        return "Unhandled condition"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
