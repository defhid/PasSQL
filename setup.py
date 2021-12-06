""" python setup.py sdist """

from setuptools import setup
from twine.commands import upload
from shutil import rmtree

print("## CREATING DIST FILES...")

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='passql',
    version='0.2.1',

    description='Super light ORM',
    long_description=long_description,
    long_description_content_type='text/markdown',

    author='Vladislav Mironov',
    author_email='hidden120@mail.ru',

    packages=['passql'],
    zip_safe=False,

    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

print("## PUBLISHING...")

upload.main(['dist\*'])

print("## REMOVING DIST FILES...")

rmtree('dist')
rmtree('passql.egg-info')

print("## SUCCESS")
