from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in data_mining2/__init__.py
from data_mining2 import __version__ as version

setup(
	name="data_mining2",
	version=version,
	description="DM",
	author="DM",
	author_email="d@dmm.cm",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
