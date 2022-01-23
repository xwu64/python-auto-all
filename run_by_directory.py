import re
from os import walk
from sys import argv
from auto_all import run


PYTHON_FILE_PATTERN = "^(?!_).*\.py$" # ignore .py files with prefix '_'

files = []
directory=argv[1]
for dirpath, dirnames, filenames in walk(directory):
    for filename in filenames:
        if re.search(PYTHON_FILE_PATTERN, filename):
            files.append([dirpath, filename])

for d, f in sorted(files, key=lambda x:x[1]):
    try:
        run(f"{d}/{f}")
    except:
        print(f"fail to add __all__ to {d}/{f}")
