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
    version="0.0.1",
    author="unfoldingWord",
    author_email="unfoldingword.org",
    description="Classes for executing tX Manager",
    license="MIT",
    keywords="tX manager",
    url="https://github.org/unfoldingWord-dev/tx-manager",
    packages=['tx_manager'],
    long_description=read('README.md'),
    classifiers=[],
    install_requires=[
        'tx-shared-tools'
    ],
    dependency_links=['git+git://github.com/richmahn/tx-shared-tools.git@develop#egg=tx-shared-tools'],
    requires=['pygithub', ]
)
