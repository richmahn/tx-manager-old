import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(f_name):
    return open(os.path.join(os.path.dirname(__file__), f_name)).read()

setup(
    name="tx-manager",
    version="0.0.8",
    author="unfoldingWord",
    author_email="unfoldingword.org",
    description="Classes for executing tX Manager",
    license="MIT",
    keywords="tX manager",
    url="https://github.org/unfoldingWord-dev/tx-manager",
    packages=['tx_manager'],
    long_description=read('README.md'),
    classifiers=[],
    dependency_links=[
        'git+git://github.com/richmahn/tx_shared_tools.git@develop#egg=tx_shared_tools',
    ],
    install_requires=[
        'requests',
        'tx_shared_tools'
    ]
)
