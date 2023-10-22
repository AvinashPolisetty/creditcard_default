from setuptools import find_packages,setup
from typing import List

Hypen_e_dot="-e ."

def get_requirements(file_path:str)->List:
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)

    return requirements


setup(

    name="CreditCardDefault",
    version="0.0.1",
    author="avinash",
    author_email="polisettyavinash@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)