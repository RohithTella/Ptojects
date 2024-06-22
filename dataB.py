# -*- coding: utf-8 -*-
import os
import sqlite3
import ASeces
from tkinter import messagebox


class database:
    def __init__(self):
        # self.key = "Saeid_javadi_usp"
        # self.key = key.encode('utf-8')
        print("ok")

    def dbcn(self, a, b):
        dbenc = ASeces.ramznegari()
        self.a, self.b = dbenc.enccc(a), dbenc.enccc(b)
        print(os.getcwd())
        if not(os.path.exists(os.getcwd()+"/Data")):
            os.mkdir(os.getcwd()+'/Data')
        self.database = sqlite3.connect("Data/NoteDLL.db")
        # self.database.SetPassword("8103094")
        print("connected to database")
        self.table = "CREATE TABLE IF NOT EXISTS  Notes(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,Onvan VARCHAR ,NoteText TEXT )"
        self.database.execute(self.table)
        print("Table OK")
        self.database.execute("""INSERT INTO Notes(Onvan,NoteText) VALUES (?,?)""", (self.a, self.b))
        self.database.commit()
        print("recorde created")
        self.database.close()

    def dbselect(self):
        # self.dbpath = self.resource_path("Data/DataFile.db")
        database = sqlite3.connect("Data/NoteDLL")
        database.text_factory = str
        print("connected to database")
        select = "SELECT * FROM Notes"
        curser = database.execute(select)
        dbsenc = ASeces.ramznegari()
        for row in curser:
            row1 = dbsenc.deccc(row[1])
            row2 = dbsenc.deccc(row[2])
            print('Onvn: {} \n Text:\n {}'.format(row1, row2))
        self.database.close()
