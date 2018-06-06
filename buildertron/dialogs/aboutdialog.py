#!/usr/bin/python3
# -*- coding: utf-8 -*
"""
Copyright (c) 2018 Simon Wu <swprojects@runbox.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from version import __version__
from forms.uiaboutdialog import Ui_AboutDialog
from PyQt5.QtWidgets import QDialog


class AboutDialog(QDialog, Ui_AboutDialog):

    def __init__(self, parent):
        super(AboutDialog, self).__init__(parent)

        self.ui = Ui_AboutDialog()
        self.ui.setupUi(self)
        self.open()

        self.ui.labelVersion.setText('{0}'.format(__version__))