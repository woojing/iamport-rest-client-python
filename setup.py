# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = ['requests']


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='iamport-rest-client',
    version='0.2.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    author='PerhapsSPY',
    author_email='perhapsspy@gmail.com',
    url='https://github.com/iamport/iamport-rest-client-python',
    description="REST client for I'mport;(http://www.iamport.kr)",
    long_description=readme(),
    license='MIT',
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
