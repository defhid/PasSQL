from twine.commands import upload
from shutil import rmtree
from os import path


def publish() -> bool:
    print("# PUBLISHING...")

    try:
        upload.main([r'dist\*'])
    except Exception as e:
        print(e)
        return False
    else:
        return True


def remove_dist_files():
    print("# REMOVING DIST FILES...")

    dirs = ['dist', 'passql.egg-info']

    for directory in dirs:
        if path.exists(directory):
            rmtree(directory)


ok = publish()

remove_dist_files()

print("# " + ("SUCCESS" if ok else "FAILURE"))
