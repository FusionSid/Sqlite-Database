import sqlite3
from person import Person

conn = sqlite3.connect('People.db')

c = conn.cursor()


def create_table():
    with conn:
        c.execute("CREATE TABLE IF NOT EXISTS Person (id INTEGER PRIMARY KEY AUTOINCREMENT, first TEXT, last TEXT, age INT)")
    print("Table Created!")

def insert_per(per):
    with conn:
        c.execute("INSERT INTO Person (first, last, age) VALUES (:first, :last, :age)",{'first':per.first, 'last':per.last, 'age':per.age})

def get_per_by_fname(firstname):
    c.execute("SELECT * FROM Person WHERE first= :first", {'first': firstname})
    return c.fetchall()

def get_per_by_lname(lastname):
    c.execute("SELECT * FROM Person WHERE last= :last", {'last': lastname})
    return c.fetchall()

def get_per_by_age(age):
    c.execute("SELECT * FROM Person WHERE age= :age", {'age': age})
    return c.fetchall()

def get_all():
    c.execute("SELECT * FROM Person")
    return c.fetchall()

def update_age(per, age):
    with conn:
        c.execute("UPDATE Person SET age = :age WHERE first = :first AND last = :last", {'first':per.first, 'last':per.last, 'age':age})

def remove_per(per):
    with conn:
        c.execute("DELETE from Person WHERE first = :first AND last = :last", {'first':per.first, 'last':per.last})

p1 = Person("Siddhesh", "Zantye", 14)
p2 = Person("Abhijit", "Zantye", 44)
p3 = Person("Deepti", "Zantye", 40)
p4 = Person("Vedant", "Zantye", 12)
p5 = Person("Prakash", "Zantye", 73)
p6 = Person("Neeta", "Zantye", 70)

conn.close()