# author: <Don Mathew>
# setup file for CLI
# Necessary imports.
from setuptools import setup

# The commands used for run the server is runserver and for client is runclient.
# Usage:
# runserver --help   or   runserver --port <port_number>
# runclient --help   or   runclient --port <port_number> --path <location>
setup(
    name="runserver runclient",
    version='0.1',
    py_modules=['server', 'client'],
    install_requires=[
        'click',
        'Flask',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        runserver=server:run
        runclient=client:getfiles
    ''',
)
