import os
from auto_add import insert_to_file_at_line


def test_insert_to_file_at_line():
    TEST_FILE_NAME = "test_fake_file"
    with open(TEST_FILE_NAME,  "w") as fh:
        fh.writelines("1\n3\n")

    insert_to_file_at_line(TEST_FILE_NAME, 2, "2\n")
    with open(TEST_FILE_NAME, "r") as fh:
        for i, line in enumerate(fh):
            assert line == f"{i+1}\n"

    os.remove(TEST_FILE_NAME)
