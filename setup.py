from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='isNullOrEmpty',
    version='1.0.0',
    packages=find_packages(),
    description='A simple Python package to check if an object is null or empty.',
    author='Thiago S Adriano',
    author_email='prof.thiagoadriano@gmail.com',
    url='https://github.com/programadriano/isNullOrEmpty',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown' 
)