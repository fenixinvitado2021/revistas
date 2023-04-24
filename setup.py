import codecs
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "revistas", "version.py")) as fp:
    exec(fp.read())

requires = []
with open(os.path.join(here, "requirements.txt"),'r') as fp:
    requires = str(fp.read()).split('\n'

setup(
    name='revistas',
    version=__version__,
    packages=["revistas"],
    install_requires=requires,
    description='Client to Libraries',
    author='RayServer',
    package_data={"": ["LICENSE"],},
    author_email='susej.mabel2009@gmail.com',
    license="The Unlicense (Unlicense)",
    url='https://github.com/fenixinvitado2021/revistas',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: The Unlicense (Unlicense)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
    zip_safe=True,
    python_requires=">=3.6",
    keywords=["telegram", "download", "stream", "bots",],
)