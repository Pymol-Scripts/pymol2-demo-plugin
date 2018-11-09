'''
PyMOL Demo Plugin

The plugin resembles the old "Rendering Plugin" from Michael Lerner, which
was written with Tkinter instead of PyQt.

(c) Schrodinger, Inc.

License: BSD-2-Clause
'''

from __future__ import absolute_import
from __future__ import print_function

# Avoid importing "expensive" modules here (e.g. scipy), since this code is
# executed on PyMOL's startup. Only import such modules inside functions.

import os


def __init_plugin__(app=None):
    '''
    Add an entry to the PyMOL "Plugin" menu
    '''
    from pymol.plugins import addmenuitemqt
    addmenuitemqt('Demo "Render" Plugin', run_plugin_gui)


def run_plugin_gui():
    '''
    Open our custom dialog
    '''
    # entry point to PyMOL's API
    from pymol import cmd

    # pymol.Qt provides the PyQt5 interface, but may support PyQt4
    # and/or PySide as well
    from pymol.Qt import QtWidgets
    from pymol.Qt.utils import loadUi
    from pymol.Qt.utils import getSaveFileNameWithExt

    # create a new Window
    dialog = QtWidgets.QDialog()

    # populate the Window from our *.ui file which was created with the Qt Designer
    uifile = os.path.join(os.path.dirname(__file__), 'demowidget.ui')
    form = loadUi(uifile, dialog)

    # callback for the "Ray" button
    def run():
        # get form data
        height = form.input_height.value()
        width = form.input_width.value()
        dpi = form.input_dpi.value()
        filename = form.input_filename.text()
        units = form.input_units.currentText()

        # calculate dots per centimeter or inch
        if units == 'cm':
            dots_per_unit = dpi * 2.54
        else:
            dots_per_unit = dpi

        # convert image size to pixels
        width *= dots_per_unit
        height *= dots_per_unit

        # render the image
        if filename:
            cmd.png(filename, width, height, dpi=dpi, ray=1, quiet=0)
        else:
            cmd.ray(width, height, quiet=0)
            print('No filename selected, only rendering on display')

    # callback for the "Browse" button
    def browse_filename():
        filename = getSaveFileNameWithExt(
            dialog, 'Save As...', filter='PNG File (*.png)')
        if filename:
            form.input_filename.setText(filename)

    # hook up button callbacks
    form.button_ray.clicked.connect(run)
    form.button_browse.clicked.connect(browse_filename)
    form.button_close.clicked.connect(dialog.close)

    # show the dialog
    dialog.show()
