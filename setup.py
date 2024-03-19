from setuptools import setup, find_packages
from typing import List


HDE = '-e .'
def get_requirements(file_path:str) -> List:
    requirements= []
    with open(file_path,'r') as f:
        requirements =f.readlines()
    requirements = [req.replace('\n','') for req in requirements]

    if HDE in requirements:
        requirements.remove(HDE)

    return requirements

setup(
    author= 'Vraj bhavsar',
    author_email= 'vrajcbhavsar0905@gmail.com',
    version= '0.0.1',
    name= 'FlightFarePrediction',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)