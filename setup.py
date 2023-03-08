from setuptools import find_packages,setup 
from typing import List


def get_requirements()->List[str]:
    
    """
    This function will retrun of requirements
    
    
    """
    requirements_list =[]
    return requirements_list

setup(

     name="sensor",
     version="0.0.1",
     author="ineuron",
     author_email="avnish@ineuron.ai",
     packages = find_packages(),
     install_requires=get_requirements,#["pymongo==4.2.0"],

)