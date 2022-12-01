from setuptools import find_packages, setup

setup(
    name="tos",
    version="0.1.0",
    author="Cameron Russell",
    description="Automates covered call writing in Thinkorswim",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'tos = tools.cmd:main',
        ],
    }
)
