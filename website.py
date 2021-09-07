from flask import Flask, render_template, request, jsonify
import sqlite3 as sql
from person import Person
from database import get_all

app = Flask(__name__)

@app.route('/')
def home():
   conn = sql.connect("People.db")
   c = conn.cursor()
   c.execute("SELECT * FROM Person")
   stuff = c.fetchall()

   return jsonify(stuff)

# Search

@app.route("/first=<name>")
def sfname(name):
   conn = sql.connect("People.db")
   c = conn.cursor()
   c.execute("SELECT * FROM Person WHERE first= :first", {'first': name})
   stuff = c.fetchall()

   return jsonify(stuff)

@app.route("/last=<name>")
def slname(name):
   conn = sql.connect("People.db")
   c = conn.cursor()
   c.execute("SELECT * FROM Person WHERE last= :last", {'last': name})
   stuff = c.fetchall()

   return jsonify(stuff)
   
@app.route("/age=<age>")
def sage(age):
   conn = sql.connect("People.db")
   c = conn.cursor()
   c.execute("SELECT * FROM Person WHERE age= :age", {'age': age})
   stuff = c.fetchall()

   return jsonify(stuff)

@app.route("/id=<id>")
def sid(id):
   conn = sql.connect("People.db")
   c = conn.cursor()
   c.execute("SELECT * FROM Person WHERE id= :id", {'id': id})
   stuff = c.fetchall()

   return jsonify(stuff)


app.run(host='0.0.0.0', port=8080)