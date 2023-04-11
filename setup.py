from setuptools import find_packages, setup 
from typing import List

Unwanted_Obj_Req = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''This will return the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", "")for req in requirements]

        if Unwanted_Obj_Req in requirements:
            requirements.remove(Unwanted_Obj_Req)



setup(
    name = "E2E-DS Project", 
    version = '0.0.1',
    author = 'Adithya Sharma',
    author_email = 'indragantiadithyasharma@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)