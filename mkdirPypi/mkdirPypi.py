

                        #********************************************************************************#
                        #                                                                                #
                        #                                  нεℓℓσ,вαтεs!                                  #
                        #                                                                                #
                        #   filename: mkdirPypi.py                                                       #
                        #   created: 2022-03-10                                                          #
                        #   system: Windows                                                              #
                        #   version: 64bit                                                               #
                        #                                       by: Bates <https://github.com/batestin1> #
                        #********************************************************************************#
                        #                           import your librarys below                           #
                        #********************************************************************************#

from pathlib import Path
from datetime import date
import getpass
import platform
import subprocess

def mkdirPypi(file):
    users=getpass.getuser()
    res = subprocess.run(["git", "config", "user.name"], stdout=subprocess.PIPE)
    git_username = res.stdout.strip().decode()
    filename = file.replace(' ', '_')
    #create a home directory#
    cd = 'Codigo fonte'
    dw = 'Download'
    linkGit = f'https://github.com/{git_username}/'
    codigo_fonte = f"{cd} : {linkGit}"
    download = f"{dw} : {linkGit}"
    project_urls = {codigo_fonte, download}
    path = Path(f"./{filename}")
    path.mkdir(parents=True, exist_ok=True)
    data_atual = date.today()
    data = f"""{data_atual.strftime('%Y-%m-%d')}"""

    #### create a LICENSE ####
    textLic ="""
MIT License
Copyright (c) 2018 Yan Orestes
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge,publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
    """
    licensa = open(f"{filename}/LICENSE", "w")
    licensa.write(textLic)

    #### create a README.md ###

    textReadm = f"""
<h1 align="center">
<img src="https://img.shields.io/static/v1?label={filename.upper()}%20POR&message={users}&color=7159c1&style=flat-square&logo=ghost"/>
<h3> <p align="center">{filename.upper()} </p> </h3>
<h3> <p align="center"> ================= </p> </h3>
>> <h3> Resume </h3>
<p> text here </p>
>> <h3> How install </h3>
```
code here
```
>> <h3> How Works </h3>
```
code here
```
    """
    readme = open(f"{filename}/README.md", "w")
    readme.write(textReadm)

    ###setup.cfg###

    cfgTxt = """
[metadata]
description-file = README.md
license_file = LICENSE.txt
"""
    cfgsetup = open(f"{filename}/setup.cfg", "w")
    cfgsetup.write(cfgTxt)

    ###setup.py ######

    setupyT = f"""
from setuptools import setup
setup(
    name = '{filename}',
    version = '1.0.0',
    author = '{users}',
    author_email = '{users}@mailer.com.br',
    packages = ['{filename}'],
    description = 'a way to make your life easier',
    long_description = 'file: README.md',
    url = 'https://github.com/{git_username}/',
    project_urls = {project_urls},
    keywords = 'a way to make your life easier',
    classifiers = []
)"""

    setupy = open(f"{filename}/setup.py", "w")
    setupy.write(setupyT)

    #### create dir #####

    path = Path(f"./{filename}/{filename}")
    path.mkdir(parents=True, exist_ok=True)
    txtnull=f"""
#############################################################################################################################
#   filename:{filename}.py                                                       
#   created: {data}                                                              
#   import your librarys below                                                    
#############################################################################################################################


def {filename}():
    pass
    """

    main = open(f"{filename}/{filename}/{filename}.py", "w")
    main.write(txtnull)


    txtnull2=f"""
#############################################################################################################################
#   filename:{filename}.py                                                       
#   created: {data}                                                              
#   import your librarys below                                                    
#############################################################################################################################



from .{filename} import *

    """
    init = open(f"{filename}/{filename}/__init__.py", "w")
    init.write(txtnull2)

    print(f"your project call {filename} was create to be upper on Pypi")