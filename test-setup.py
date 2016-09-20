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
        'git+git://github.com/richmahn/tx-shared-tools.git@develop#egg=tx-shared-tools',
        'git+git://github.com/richmahn/tx-shared-tools.git@develop#egg=aws_tools',
        'git+git://github.com/richmahn/tx-shared-tools.git@develop#egg=general_tools',
        'git+git://github.com/richmahn/tx-shared-tools.git@develop#egg=gogs_tools',
    ],
    install_requires=[
        'requests',
        'aws_tools',
        'gogs_tools'
    ],
    test_suite='tests'
)
