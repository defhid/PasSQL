def setup():
    from setuptools import setup

    with open("README.md", "r") as fh:
        long_description = fh.read()

    setup(name='passql',
          version='0.2.1',
          description='Super light ORM',
          long_description=long_description,
          long_description_content_type='text/markdown',
          packages=['passql'],
          author='Vlad Mironov',
          author_email='hidden120@mail.ru',
          python_requires='>=3.6',
          zip_safe=False,
          classifiers=[
                "Programming Language :: Python :: 3.8",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
          ])


def publish():
    from twine.commands import upload

    upload.main(['dist\*'])


if __name__ == '__main__':
    # python setup.py sdist
    publish()
else:
    setup()
