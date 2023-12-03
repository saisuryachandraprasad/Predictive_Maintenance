from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(filepath)-> List:
    """ This method is responsible for installing all requirements"""

    requirements = []

    with open(filepath, "r") as filepath_obj:
        requirements = filepath_obj.readlines()
        requirements = [req.replace("/n","")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        return requirements

setup(
    name= "Predictive Maintenance",
    version="0.0.1",
    author= "Sai Surya Chandra Prasad",
    author_email="saisuryachandraprasad@gmail.com",
    packages= find_packages(),
    requirements = get_requirements("requirements.txt")
)