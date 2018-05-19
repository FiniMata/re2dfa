#setup.py
import sys, os
from cx_Freeze import setup, Executable

import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

__version__ = "1.2.0"

include_files = ['l.jpg', 're2dfa.exe', 'icon.ico','graphviz-2.38/',os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')]
packages = ["os", "tkinter","PIL","sys","subprocess","pydot","graphviz"]

setup(
    name = "Finimata RE2DFA",
    description='RE To DFA',
    version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    'include_msvcr': True,
}},
executables = [Executable("app.py",base="Win32GUI")]
)