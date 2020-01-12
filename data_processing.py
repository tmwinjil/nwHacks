import os
import sqlite3
import numpy as np

os.chdir('/home/kyle/nwHacks/')
connection = sqlite3.connect('train-data/FPA_FOD_20170508.sqlite')
cur = connection.cursor()
cur.execute("SELECT * FROM Fires")
rows = cur.fetchall()

data = np.array(rows)