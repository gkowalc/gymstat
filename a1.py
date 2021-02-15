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
    results = c.execute('''SELECT  Exercise, Category, Weight, Reps, Date   FROM exercise3 where (?)  =  DATE(date) ''', (date,)) # [(1, 'pokerkid'), (2, 'crazyken')]
    data = results.fetchall()
    #  sample output list of turples[('Bench Press (Barbell)', 'Chest', 55.0, 10, '2020-11-23 20:14:11'), ('Bench Press (Barbell)', 'Chest', 55.0, 10, '2020-11-23 20:19:24'),
    # add a comma after (date) otherwise https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta
    # result of list of turples
    return(data)


tuple_list = exerciseReportFromDate('2020-12-30')
#print (tuple_list)
first_tuple_elements = []

for a_tuple in tuple_list:
 #   print (a_tuple)
  #   print (a_tuple[0], a_tuple[3], a_tuple[2])
    first_tuple_elements.append((a_tuple[0], a_tuple[3], a_tuple[2]))

#print(tuple_list)
# print (first_tuple_elements)

# print (first_tuple_elements)
#print("\n".join(first_tuple_elements))

def dayExericeReport(tuple_list):
    exerice_list = []
    list_of_lists = [list(elem) for elem in tuple_list]
    print (list_of_lists)
    for first_element in list_of_lists:
        if len(exerice_list)==0:
                temp_list = []
                temp_list.append(first_element[0])
                temp_list.append(1)
                temp_list.append(first_element[2])
                temp_list.append(first_element[3])
                exerice_list.append(temp_list)
            # exerice_list.append(first_element[2])


        def Extract(lst):
            return [item[0] for item in lst]

        z = Extract(exerice_list)
        for i in exerice_list:
             z = Extract(exerice_list)
             if (first_element[0])    not in  z:


                        temp_list2 = []
                        temp_list2.append(first_element[0])
                        temp_list2.append(1)
                        temp_list2.append(first_element[2])
                        temp_list2.append(first_element[3])
                        exerice_list.append(temp_list2)
                       # if temp_list2[0] not in
                      #  print(temp_list2)

    # print(exerice_list)
                    # print (temp_list)
                    # exerice_list.append(temp_list)

                #else:
                 #   print (first_element[1])
                  #  exerice_list[1] = [x+1 for x in  first_element[1]]

                   # temp_list = []
       #  print(exerice_list)

    #  print(exerice_list)

    # print (exerice_list)
    return exerice_list
dayExericeReport(tuple_list)
# exerciseReportFromDate('2020-11-23')

