from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT ='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    reqiurements=[]
    with open(file_path) as file_obj:
        reqiurements=file_obj.readlines()
        reqiurements=[req.replace("\n","") for req in reqiurements]

        if HYPHEN_E_DOT in reqiurements:
            reqiurements.remove(HYPHEN_E_DOT)

    return reqiurements       



setup(
    name='projectsml',
    version='0.0.1',
    author='Nistha',
    author_email='nisthasinghindore@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)