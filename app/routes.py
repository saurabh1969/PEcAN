from flask import Flask, g, render_template,request, redirect,Response
import sqlite3
import json
import os
import pandas as pd
from Model.dbcreate import *

# Create app
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'db_key'

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/insert',methods = ['POST', 'GET'])
def insert():    
    if request.method == 'POST':
        
        file=request.args['file']
        init_db(file)
        
    return "File Uploaded"

@app.route('/search',methods = ['POST', 'GET'])
def search():    
    cur = get_db().cursor()
    if request.method == 'POST':
        id=request.args['id']
        query="""SELECT * FROM data_table WHERE id = %s"""% (id,)
        #res=cur.execute("""SELECT * FROM data_table WHERE id = %s"""% (id,))
        res=sql_query(query)
    return Response(json.dumps(res),  mimetype='application/json')


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
 
    
