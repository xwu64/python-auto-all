import re
from os import walk
from sys import argv
from auto_all import run


PYTHON_FILE_PATTERN = ".py"

files = []
directory=argv[1]
for dirpath, dirnames, filenames in walk(directory):
    for filename in filenames:
        if re.search(PYTHON_FILE_PATTERN, filename) and not filename[0]=="_":
            files.append([dirpath, filename])

for d, f in sorted(files, key=lambda x:x[1]):
    try:
        run(f"{d}/{f}")
    except:
        print(f"fail to add __all__ to {d}/{f}")
