# PyMOL Demo Plugin

Demo plugin for [PyMOL](https://pymol.org) which demonstrates the usage of PyQt to create a dialog.

## Requirements

PyMOL 2.x

## Usage

[Download ZIP](https://github.com/Pymol-Scripts/pymol2-demo-plugin/archive/master.zip)
and install with PyMOL's plugin manager
(Plugin > Plugin Manger > Install New Plugin > Install from local file).

Alternatively, you can clone this repo into a directory which is in PyMOL's plugin search path
(Plugin > Plugin Manger > Settings > Plugin override search path).

## Plugin files

* [\_\_init\_\_.py](__init__.py): Entry point, provides the `__init_plugin__` function which adds an entry to PyMOL's plugin menu.
* [demowidget.ui](demowidget.ui): Graphical user interface file, created with [Qt Designer](http://doc.qt.io/qt-5/qtdesigner-manual.html)

## License

[BSD-2-Clause](LICENSE)

(c) Schrodinger, Inc.
