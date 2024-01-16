# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 16:51:46 2024

@author: w
"""

# model.py
class Model:
    def __init__(self):
        self._counter = 0

    def get_counter(self):
        return self._counter

    def increment_counter(self):
        self._counter += 1

