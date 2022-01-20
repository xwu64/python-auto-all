from typing import List
import ast


MAX_CHAR_LEN = 79
PREFIX = "__all__ = "
FRONT_PAD = len(PREFIX) + 1 # one char for "["


def is_exist(filename: str) -> bool:
    with open(filename, 'r') as fh:
        tree = ast.parse(fh.read())
        for body in tree.body:
            if isinstance(body, ast.Assign):
                for var in body.targets:
                    print(var.__dict__)
                    if isinstance(var, ast.Name) and var.id == "__all__":
                        # assign with one variable
                        return True
                    if isinstance(var, ast.Tuple) and any([e.id == "__all__" for e in var.elts]):
                        # assign with multiple variables
                        return True

        return False


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
    return f"\n{PREFIX}{str_names}\n"


def insert_to_file_at_line(filename, line_num, text):
    assert text[-1] == "\n", "text should end with \\n"

    with open(filename, "r") as fh:
        content = fh.readlines()
        content.insert(line_num-1, text)

    with open(filename, "w") as fh:
        fh.writelines(content)


def find_position(filename: str) -> int:
    # insert after import
    position = 0
    with open(filename, "r") as fh:
        tree = ast.parse(fh.read())
        for i, body in enumerate(tree.body):
            if i == 0 and isinstance(body, ast.Expr):
                # ignore docstring
                continue
            if not (isinstance(body, ast.Import) or isinstance(body, ast.ImportFrom)):
                break
            else:
                position = body.end_lineno
    return position + 1


def run(filename: str):
    names = generate(filename)
    text = format(names)
    line_num = find_position(filename)
    if not is_exist(filename):
        insert_to_file_at_line(filename, line_num, text)


if __name__ == "__main__":
    from sys import argv
    filename = argv[1]
    run(filename)
