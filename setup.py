# setup.py
from setuptools import setup, find_packages

setup(
    name='QuatNet',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'torch>=2.0.0'
    ],
    author='aryan',
    author_email='datasenseiaryan@gmail.com',
    description='A PyTorch-based library for quaternion neural networks',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/DataSenseiAryan/QuatNet',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
