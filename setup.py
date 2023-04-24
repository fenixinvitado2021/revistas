import codecs
import os

from setuptools import setup, find_packages

setup(
    name='revistas',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'bs4'
    ],
    description='Client to Libraries',
    author='RayServer',
    author_email='susej.mabel2009@gmail.com',
    url='https://github.com/fenixinvitado2021/revistas',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)