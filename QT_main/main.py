# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:47:40 2024

@author: w
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from model import Model

class View(QWidget):
    def __init__(self, model):
        super().__init__()

        self.model = model

        self.label = QLabel("Counter: 0")
        self.button = QPushButton("Increment")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.button.clicked.connect(self.handle_button_click)

    def update_view(self):
        counter_value = self.model.get_counter()
        self.label.setText(f"Counter: {counter_value}")

    def handle_button_click(self):
        self.model.increment_counter()
        self.update_view()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    model = Model()
    view = View(model)

    view.show()

    sys.exit(app.exec_())