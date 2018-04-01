RE 2 DFA Windows Source Code By Finimata
=============================

Requirements
--------------------
python,pydot,tkinter

graphviz has been included as graphviz-2.38.zip, unzip it in the same directory

Linux source code usage:
--------------------------------------
1. compile re2dfa.c as re2dfa.exe using Devcpp
2. app.py is GUI wrapper based on tkinter
3. run it with python3.6
4. edit build package options in setup.py
4. convert into app using cx_freeze with command
------> python setup.py bdist_msi