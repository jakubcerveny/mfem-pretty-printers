# -*- coding: utf-8 -*-
# -*- python -*-
import sys
import gdb
import os
import os.path

pythondir = os.path.dirname(__file__) + '/../python'

# Update module path.

if not pythondir in sys.path:
    sys.path.insert(0, pythondir)

# Load the pretty-printers.
from mfem.mfem import register_mfem_printers
register_mfem_printers(gdb.current_objfile())

