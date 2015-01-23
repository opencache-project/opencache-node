#!/usr/bin/env python2.7

from setuptools import setup, find_packages

conf = dict(
    name='opencache-node',
    version='0.1.0',
    description='Serve cached content in response to a user request.',
    long_description='For more details and the README, please see our `GitHub page <https://github.com/opencache-project/opencache-node>`_.',
    author='Matthew Broadbent',
    author_email='matt@matthewbroadbent.net',
    scripts=['scripts/opencache-node'],
    install_requires=['pymongo', 'pyzmq', 'configparser', 'opencache-lib'],
    url='https://github.com/opencache-project/opencache-node',
    download_url = 'https://github.com/opencache-project/opencache-node/tarball/0.1.0',
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: DFSG approved',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: System :: Networking',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring'
        ],
    keywords = ['content', 'caching', 'distribution', 'software defined networking'],
    packages=find_packages(),
    namespace_packages=['opencache']
)

setup(**conf)
