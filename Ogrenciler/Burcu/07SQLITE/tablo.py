"""import sqlite3
database=sqlite3.connect("data.db")
imlec=database.cursor()
database.close()"""

import sqlite3
database=sqlite3.connect("data.db")
imlec=database.cursor()
def tabloOlustur():
    imlec.execute("CREATE TABLE IF NOT EXISTS wordlist(Word TEXT, Type TEXT, Synonym TEXT, Antonym TEXT)")
    database.commit() 
tabloOlustur()
database.close()






