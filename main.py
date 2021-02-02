import psycopg2
import random


nazwiska = ['Kowalski', 'Wójcik', 'Dąbrowski','Bąk', 'Arekci', 'Nowak', 'Kiepski', 'Pazdzioch']
imiona = ['Lukasz','Tomasz','Artur','Kamil','Marian','Arnold', 'Patryk', 'Stefan']


class DataBase:
    def __init__(self, user, pw):
        self.conn = psycopg2.connect(dbname='postgres', host='localhost', user=f'{user}', password=f'{pw}')
        self.cur = self.conn.cursor()

    def insertquerry(self, data):
        for row in data:
            print(row)
            self.cur.execute(f"insert into main (name, surname) values ('{row[0]}','{row[1]}')")
            self.conn.commit()

    def dane(self, qua):
        list = []
        for i in range(0, qua):
            name = random.choice(imiona)
            surname = random.choice(nazwiska)
            full=[name,surname]
            #print(full)
            list.append(full)
        return list


db=DataBase('postgres', 'admin')
c=DataBase.dane(db, 230)
print(c)
DataBase.insertquerry(db, c)