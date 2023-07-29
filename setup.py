from setuptools import find_packages, setup

setup(
    name='foxes_cool',
    packages=find_packages(include=['foxes_cool']),
    version='1.0.0',
    description='An API for all your fox image needs',
    author='Arthur Melton',
    license='MIT',
    install_requires=['requests'],
)
