from setuptools import setup, find_packages  # or find_namespace_packages

setup(
    # ...
    packages=find_packages(
        # All keyword arguments below are optional:
        where='src',  # '.' by default
        include=['expensemanager*'],  # ['*'] by default
        exclude=['expensemanager.tests'],  # empty by default
    ),
    # ...
)