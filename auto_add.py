from typing import List
import ast


MAX_CHAR_LEN = 79
PREFIX = "__all__ = "
FRONT_PAD = len(PREFIX) + 1 # one char for "["




def generate(filename) -> List[str]:
    names = []

    with open(filename, 'r') as fh:
        tree = ast.parse(fh.read())
        for body in tree.body:
            if hasattr(body, "name") and body.name[0] != "_":
                names.append(body.name)

    return names


def format(names: List[str]) -> str:
    str_names = str(names).replace("'", "\"")
    if len(str_names) > MAX_CHAR_LEN:
        str_names = str_names.replace(" ", "\n" + " "*FRONT_PAD)
    return f"{PREFIX}{str_names}"


def insert(filename, text):
    pass


def run(filename):
    names = generate(filename)
    str_names = format(names)
    print(str_names)


if __name__ == "__main__":
    filename = ""
    run(filename)
