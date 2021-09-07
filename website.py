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

@app.route("/search")
def search():
   pass
   
app.run(host='0.0.0.0', port=8080)