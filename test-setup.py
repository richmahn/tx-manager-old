from setuptools import setup

setup(
    name="tx-manager",
    version="0.0.1",
    author="unfoldingWord",
    author_email="unfoldingword.org",
    description="Unit test setup file.",
    keywords="",
    url="https://github.org/unfoldingWord-dev/tx-manager",
    packages=['tx_manager'],
    long_description='Unit test setup file',
    classifiers=[],
    dependency_links=[
        'git+git://github.com/richmahn/tx_shared_tools.git@develop#egg=tx_shared_tools',
    ],
    install_requires=[
        'requests',
        'tx_shared_tools'
    ],
    test_suite='tests'
)
