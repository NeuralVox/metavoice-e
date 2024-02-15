from setuptools import find_packages, setup  # type: ignore

setup(
    name="metavoice-e",
    packages=find_packages(".", exclude=["tests"]),
)
