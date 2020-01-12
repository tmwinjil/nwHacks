import os
import sys
import sqlite3
import numpy as np

os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))
connection = sqlite3.connect('train-data/FPA_FOD_20170508.sqlite')
cur = connection.cursor()
cur.execute("SELECT * FROM Fires")
rows = cur.fetchall()

data = np.array(rows)