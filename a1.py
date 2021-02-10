import pandas
import sqlite3
exerciese_data = pandas.read_csv('/home/greg/Downloads/exercise_logs01012020.csv')
from pathlib import Path

Path('1.db').touch()
conn = sqlite3.connect('1.db')
c = conn.cursor()
# create table
# c.execute('''CREATE TABLE exercise2 (Exercise, Category, Muscles, Weight, Reps, Hours, Minutes, Seconds, Distance , Calories, Date, Note)''')
# load the data into a Pandas DataFrame
exerciese_data = pandas.read_csv('/home/greg/Downloads/exercise_logs01012020.csv')
# write the data to a sqlite table
exerciese_data.to_sql('exercise2', conn, if_exists='append', index = False)
conn = sqlite3.connect('1.db')
c = conn.cursor()
# select all data from database

results = c.execute('''SELECT date(date) FROM exercise2''').fetchall()  #
def  getDataFromLastDate():
    results = c.execute('''SELECT * FROM exercise2 where date(date) = (SELECT MAX(DATE(date)) FROM exercise2)''').fetchall()  # [(1, 'pokerkid'), (2, 'crazyken')]
    return(results)
    # Exercise, Category, Muscles, Weight, Reps, Hours, Minutes, Seconds, Distance , Calories, Date, Note



