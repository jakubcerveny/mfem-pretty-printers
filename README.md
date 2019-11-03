# mfem-pretty-printers

GDB pretty printers for [MFEM](https://mfem.org/) classes `Array`, `Vector` and `Matrix`.

Allows you to see the content of MFEM containers in debuggers such as Arm DDT:

![](https://raw.githubusercontent.com/jakubcerveny/mfem-pretty-printers/master/img/ddt.png)

## Installation

Clone this repo into `~/.allinea/gdb` (see also Arm Forge [User Guide](https://developer.arm.com/docs/101136/latest/ddt),
section [Custom Pretty Printers](https://developer.arm.com/docs/101136/latest/ddt/viewing-variables-and-data#x12-1560008)).

The file `auto-load/libm.so.6-gdb.py` should really be called `auto-load/libmfem.so-gdb.py` if MFEM 
was a shared library, so that the pretty printers get loaded any time a MFEM-based program is loaded.
However, MFEM is a static library at the moment, so I had to use the name of the `libm` shared object
that gets loaded for each of my MFEM program. This name can be different on other systems, so either use
the exact name of your program (e.g., `auto-load/ex1p-gdb.py`) or use `ldd` to determine which `so` files
your program uses (`ldd ex1p`).

## Other debuggers

The printers could possibly work in GDB or TotalView as well. Create an issue with install
instructions for your debugger and I will update this page.
