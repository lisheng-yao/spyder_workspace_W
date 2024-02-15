# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 12:20:57 2024

@author: w
"""

import select
import socket


def non_blocking_operation():
    print("Start Non-blocking Operation")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)