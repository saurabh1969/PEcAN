from flask import Flask, g, render_template,request, redirect
import sqlite3
import os
import pandas as pd
from Model.dbcreate import *

# Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/insert',methods = ['POST', 'GET'])
def insert():    
    if request.method == 'POST':
        url = request.form['file']
        init_db(url)
        cur = get_db().cursor()
        res=cur.execute("select * from data_table LIMIT 5" )
    return render_template("result.html", results=res)

@app.route('/search',methods = ['POST', 'GET'])
def search():    
    cur = get_db().cursor()
    if request.method == 'POST':
        id = request.form['id']
        res=cur.execute("select * from data_table where id=?", (id,) )
    return render_template("result.html", results=res)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("500.html"), 500

# Helper to close
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    #init_db()
    app.run(debug=True)
 
    