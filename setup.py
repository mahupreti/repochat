from setuptools import setup, find_packages

setup(
    name='repochat',
    version='1.0.0',
    author='Mahesh Upreti',
    author_email='maheshupretiofficial@gmail.com',
    description='A CLI tool to chat with any GitHub repository using GitHub Copilot CLI.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/mahupreti/repochat',
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
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
