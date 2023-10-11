#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
:Author: Ajith
:Date: 11/10/2023
:Copyright: © 2023, Ajith
:License: MIT
"""

import os
import sqlite3
import datetime

from snipp import __db_directory__

class DBConnection:

    def __init__(self):
        self.connection = None
        self.cursor = None
        self.check_connection()
        self.initialize_database()

    def check_connection(self):
        if not os.path.isdir(__db_directory__):
            try:
                os.mkdir(__db_directory__)
            except OSError as error:
                print(error)
        self.connection = sqlite3.connect(__db_directory__ + "\snipp.db")
        self.cursor = self.connection.cursor()

    def initialize_database(self):
        query = """ CREATE TABLE IF NOT EXISTS SNIPPET (
            id INTEGER PRIMARY KEY,
            title TEXT,
            content TEXT,
            timestamp TEXT
        ); """
        self.cursor.execute(query)

    def add_snipp(self, title, content):
        snippet_data = (title, content, datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y"))
        self.cursor.execute('INSERT INTO SNIPPET(title, content, timestamp) VALUES (?,?,?)', snippet_data)
        self.connection.commit()

    def get_snipp(self, id):
        _id = (id,)
        self.cursor.execute('SELECT * FROM SNIPPET WHERE id = ?', _id)
        return self.cursor.fetchall()
    
    def get_all_snipp(self):
        self.cursor.execute('SELECT * FROM SNIPPET')
        return self.cursor.fetchall()

    def delete_snipp(self, id):
        _id = (id,)
        self.cursor.execute('DELETE FROM SNIPPET WHERE id = ?', _id)
        self.connection.commit()

    def __del__(self):
        if self.connection is not None:
            self.connection.close()
