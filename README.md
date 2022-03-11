<h1 align="center">
<img src="https://img.shields.io/static/v1?label=mkdirPypiR%20POR&message=MAYCON%20BATESTIN&color=7159c1&style=flat-square&logo=ghost"/>


<h3> <p align="center">mkdirPypi </p> </h3>
<h3> <p align="center"> ================= </p> </h3>

>> <h3> Resume </h3>

<p> This project is to create the directory tree to upload your project to Pypi </p>

>> <h3> How install </h3>
```
pip install mkdirPypi

```

>> <h3> How Works </h3>
```
from mkdirPypi import *


mkdirPypi("hello")

```

>> <h3> After that </h3>

<p> After configuring your project, run the following commands to upload it to Pypi </p>

```
python setup.py sdist


py -m twine upload  dist/*

```

<p> obs - it is necessary to have twine installed </p>
```
pip install twine
```