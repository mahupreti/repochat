from setuptools import setup, find_packages

setup(
    name='repochat',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'click>=8.1.0',
        'gitpython>=3.1.0',
        'rich>=13.0.0',
    ],
    entry_points={
        'console_scripts': [
            'repochat=repochat.cli:cli',
        ],
    },
    python_requires='>=3.10',
)
