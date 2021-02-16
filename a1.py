import pandas
import sqlite3
import matplotlib.pyplot as plt
import numpy as np
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

def  getDaysWithTraining():
    results = c.execute('''SELECT distinct  DATE(date) FROM exercise3''').fetchall()  # [(1, 'pokerkid'), (2, 'crazyken')]
    return(results)

def  exerciseReportFromDate(date):
    results = c.execute(''' select  Exercise, Category, count(Exercise) as ilosc_serii, sum(Reps) as iloscp_owtorzen,  sum(Weight*Reps) as exercise_volume, sum(Reps) as iloscp_owtorzen, sum(Reps)/count(Exercise) as srednia_ilosc_powtorzen_w_serii, sum(Weight*Reps)/sum(Reps) as sredni_ciezar   from exercise3 where (?)  =  DATE(date) group by Exercise  ''', (date,))
    data = results.fetchall()
    print(data)
    return(data)

def  exerciseReportFromWeel(Week):
    results = c.execute(''' select Exercise, Category, count(Exercise) as ilosc_serii, sum(Reps) as iloscp_owtorzen,  sum(Weight*Reps) as exercise_volume, sum(Reps) as iloscp_owtorzen, sum(Reps)/count(Exercise) as srednia_ilosc_powtorzen_w_serii, sum(Weight*Reps)/sum(Reps) as sredni_ciezar   from exercise3 where (STRFTIME('%W', Date)) = (?) group by Exercise order by category ''', (Week,))
    data = results.fetchall()
    for t in data:
       print( ' '.join(str(s) for s in t) + '\n')
    return(data)

def  performanceExerice(exercise):
    results = c.execute(
        '''select Exercise, Category, count(Exercise) as ilosc_serii, sum(Reps) as iloscp_owtorzen,  sum(Weight*Reps) as exercise_volume,  sum(Reps)/count(Exercise) as srednia_ilosc_powtorzen_w_serii, sum(Weight*Reps)/sum(Reps) as sredni_ciezar, max(Weight), date(date)   from exercise3 where Exercise  = (?) group by date(Date)  order by category''',
        (exercise,))
    print
    data = results.fetchall()
    print(data)


    x_val = [x[8] for x in data]
    y_val = [x[4] for x in data]
    y_val2 = [x[6] for x in data]

    fig, ax1 = plt.subplots()

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('time (s)')
    ax1.set_ylabel('exp', color=color)
    ax1.plot(x_val, y_val, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('sin', color=color)  # we already handled the x-label with ax1
    ax2.plot(x_val, y_val2, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    ax3 = ax1.twinx()  # instantiate a second axes that shares the same x-axis


    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()

    return (data)




exerciseReportFromDate('2020-12-30')
exerciseReportFromWeel('52')
performanceExerice('Bench Press (Barbell)')