import pandas
import sqlite3
exerciese_data = pandas.read_csv('/home/greg/Downloads/exercise_logs01012020.csv')
from pathlib import Path

Path('1.db').touch()
conn = sqlite3.connect('1.db')
c = conn.cursor()
# create table
# c.execute('''CREATE TABLE exercise3 (Exercise, Category, Muscles, Weight, Reps, Hours, Minutes, Seconds, Distance , Calories, Date, Note)''')
# load the data into a Pandas DataFrame
# exerciese_data = pandas.read_csv('/home/greg/Downloads/exercise_logs01012020.csv')
# write the data to a sqlite table
# exerciese_data.to_sql('exercise3', conn, if_exists='append', index = False)
conn = sqlite3.connect('1.db')
c = conn.cursor()
# select all data from database
results = c.execute('''SELECT date(date) FROM exercise3''').fetchall()  #
def  getDataFromLastDate():
    results = c.execute('''SELECT * FROM exercise2 where date(date) = (SELECT MAX(DATE(date)) FROM exercise3)''').fetchall()  # [(1, 'pokerkid'), (2, 'crazyken')]
    return(results)
    # Exercise, Category, Muscles, Weight, Reps, Hours, Minutes, Seconds, Distance , Calories, Date, Note


def  getDaysWithTraining():
    results = c.execute('''SELECT distinct  DATE(date) FROM exercise3''').fetchall()  # [(1, 'pokerkid'), (2, 'crazyken')]
    return(results)

    # Exercise, Category, Muscles, Weight, Reps, Hours, Minutes, Seconds, Distance , Calories, Date, Note

def  exerciseReportFromDate(date):
    results = c.execute('''select Exercise, count(Exercise) as ilosc_serii,  Category, sum(Weight*Reps) as exercise_volume, sum(Reps) as iloscp_owtorzen, sum(Reps)/count(Exercise) as srednia_ilosc_powtorzen_w_serii, sum(Weight*Reps)/sum(Reps) as sredni_ciezar   from exercise3 where (?)  =  DATE(date) group by Exercise  ''', (date,)) # [(1, 'pokerkid'), (2, 'crazyken')]
    data = results.fetchall()
    print(data)
    return(data)

def  exerciseReportFromWeel(Week):
    results = c.execute('''select Exercise, count(Exercise) as ilosc_serii,  Category, sum(Weight*Reps) as exercise_volume, sum(Reps) as iloscp_owtorzen, sum(Reps)/count(Exercise) as srednia_ilosc_powtorzen_w_serii, sum(Weight*Reps)/sum(Reps) as sredni_ciezar   from exercise3 where (STRFTIME('%W', Date)) = (?) group by Exercise order by category ''', (Week,)) # [(1, 'pokerkid'), (2, 'crazyken')]
    data = results.fetchall()
    print(data)
    return(data)



exerciseReportFromDate('2020-12-30')
exerciseReportFromWeel('52')