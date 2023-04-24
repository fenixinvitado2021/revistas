# Revistas
Python 3 library
# Description
Client for libraries, author : RayServer
# Features 1.0.1
# Quickstart & Installation
Revistas requires an installation of Python 3.6 or greater, as well as pip. (Pip is typically bundled with Python 
To install from the source with pip:
```
pip install revistas
```
- Using revistas in a Python script
```
from revs.client import Revistas


client = Revistas("host","username","password")
login = client.login()
if login:
	#your code
```
