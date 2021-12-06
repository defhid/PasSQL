""" python setup.py sdist """

INFO = {
    'name': "passql",
    'version': "0.2.2",

    'description': "Super light ORM",

    'author': "Vladislav Mironov",
    'author_email': "hidden120@mail.ru",

    'python_requires': ">=3.6",
    'classifiers': [
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
}


def make_dist_files():
    from setuptools import setup

    print("## CREATING DIST FILES...")

    with open("README.md", "r") as fh:
        long_description = fh.read()

    setup(
        **INFO,
        long_description=long_description,
        long_description_content_type='text/markdown',
        packages=['passql'],
        zip_safe=False,
    )


def publish() -> bool:
    from twine.commands import upload

    print("## PUBLISHING...")

    try:
        upload.main([r'dist\*'])
    except Exception as e:
        print(e)
        return False
    else:
        return True


def remove_dist_files():
    from shutil import rmtree

    print("## REMOVING DIST FILES...")

    rmtree('dist')
    rmtree('passql.egg-info')


make_dist_files()

ok = publish()

remove_dist_files()

print("## " + ("SUCCESS" if ok else "FAILURE"))
