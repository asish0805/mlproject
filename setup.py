from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and req.strip() != "-e ."]
    return requirements


setup(
    name="mlproject",
    version="0.0.1",
    author="asish",
    author_email="srigakollapuasish@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=get_requirements("requirements.txt"),
)
