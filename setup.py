from setuptools import setup,find_packages
from typing import List


PROJECT_NAME = "housing-prediction"
VERSION = "0.0.1"
AUTHOR = "AJ"
DISCREPTION = "predict the house price"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"


def get_requirements_list()->List[str]:
    """
    Ddescription : thsi function is going to return list of requiremnts mention in the requirements.txt file

    return this fuction is going to return a list which contins name of libraries mentioned in requirements.txt file
    """
    
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines()

setup(
name = PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description = DISCREPTION,
package = find_packages(),
install_requires=get_requirements_list()
)

# if __name__ == "__main__":
#     print(get_requirements_list())