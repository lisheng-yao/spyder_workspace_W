#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 17:10:37 2023

@author: yaolisheng
"""

import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="0000",
  database="test1"
)

cursor = db.cursor()
cursor.execute("SELECT * FROM new_table")
results = cursor.fetchall()

for x in results:
  print(x)
  
db.close()
