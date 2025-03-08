# Hold dependencies
# Installable package 
from setuptools import find_packages, setup



with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Ramazan Acikgoz'
    author_email='ramazan.acikgz@gmail.com'
    description='Backup PostgreSQL databases.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ramazanacikgoz/pgbackup',
    packages=find_packages('src')
)