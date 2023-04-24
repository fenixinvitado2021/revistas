import codecs
import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

#with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
#    long_description = "\n" + fh.read()

with open(os.path.join(here, "revistas", "version.py")) as fp:
    exec(fp.read())

requires = []
with open(os.path.join(here, "requirements.txt"),'r') as fp:
    requires = str(fp.read()).split('\n')

setup(
    name="revistas",
    version=__version__,  # noqa: F821
    author="RayServer",
    author_email="obysoftt@gmail.com",
    packages=["revistas"],
    install_requires=requires,
    package_data={"": ["LICENSE"],},
    url="https://github.com/fenixinvitado2021/revistas",
    license="The Unlicense (Unlicense)",
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
    description=("Python 3 library for telegram bots"),
    zip_safe=True,
    python_requires=">=3.6",
    keywords=["telegram", "download", "stream", "bots",],
)