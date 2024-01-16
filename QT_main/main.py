# -*- coding: utf-8 -*-

"""
Created on Tue Jan 16 15:48:14 2024

@author: w
"""

import sys
from PyQt5.QtWidgets import QApplication
from model import Model
from view import View
from controller import Controller


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    model = Model()
    view = View(model)
    controller = Controller(model,view)
    
    view.show()
    
    
    sys.exit(app.exec_())
    
    
    