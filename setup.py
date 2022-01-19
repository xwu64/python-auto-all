from setuptools import find_packages, setup

print(find_packages(exclude=["tests"]))
setup(
    name="auto_add",
    packages=find_packages(exclude=["tests"], include=['auto_all']),

    )
