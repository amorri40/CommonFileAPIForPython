#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3

def connect_to_database(database_name):
    con = sqlite3.connect(database_name+'.db')
    return con.cursor()

def execute_sql(database, sql):
    assert isinstance(database, sqlite3.Cursor)
    database.execute(sql)
    data = database.fetchall()
    return data
