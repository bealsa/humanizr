#from distutils.core import setup
from setuptools import setup

setup(
    name = 'Organization-Personal Classifier',
    version = '0.0.1',
    packages = ['op-classifier'],
    package_dir = {'op-classifier': 'op-classifier'},
#    install_requires = ['numpy>=1.7', 'python-cjson'],
    install_requires = ['python-cjson', 'MySQL-python'],
    author = 'James McCorriston',
    author_email = 'james.mccorriston@mail.mcgill.ca'
#    description = "A tool for classifying Twitter users as Organizations or Personal accounts. Includes feature extraction and SVM classification."
)

