import os
import sqlite3
import pandas as pd
from flask import g
from routes import app



DATABASE = "./metadata.db"


# Check if the database exist, if not create the table 
def init_db(url):
	
	if os.path.exists(DATABASE):
	    os.remove(DATABASE)
	with app.app_context():
			    conn = sqlite3.connect(DATABASE)
			    data_url = url
			    
			    data_table = pd.read_csv(data_url)

			    data_table.to_sql('data_table', conn, dtype={
			    'checked':'INTEGER',
			    'result_type':'VARCHAR(10)',
			    'id':'INTEGER PRIMARY KEY',
			    'citation_id':'INTEGER',
			    'site_id':'INTEGER',
			    'treatment_id':'INTEGER',
			    'sitename':'VARCHAR(256)',
			    'city':'VARCHAR(10)',
			    'lat':'INTEGER',
			    'lon':'INTEGER',
			    'scientificname':'VARCHAR(256)',
			    'commonname':'VARCHAR(256)',
			    'genus':'VARCHAR(256)',
			    'species_id':'INTEGER',
			    'cultivar_id':'INTEGER',
			    'author':'VARCHAR(256)',
			    'citation_year':'INTEGER',
			    'treatment':'VARCHAR(256)',
			    'date':'VARCHAR(256)',
			    'time':'VARCHAR(256)',
			    'raw_date':'VARCHAR(256)',
			    'month':'VARCHAR(5)',
			    'year':'INTEGER',
			    'dateloc':'REAL',
			    'trait':'VARCHAR(256)',
			    'trait_description':'VARCHAR(256)',
			    'mean':'REAL',
			    'units':'VARCHAR(256)',
			    'n':'INTEGER',
			    'statname':'VARCHAR(5)',
			    'stat':'REAL',
			    'notes':'VARCHAR(256)',
			    'access_level':'INTEGER',
			    'cultivar':'VARCHAR(256)',
			    'entity':'VARCHAR(5)',
			    'method_name':'VARCHAR(256)',
			})

   
# Helper method to get the database since calls are per thread,
# and everything function is a new thread when called
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def sql_query(query):
	cur = get_db().cursor()
	cur.execute(query)
	rows = cur.fetchall()
	#conn.close()
	return rows

"""def sql_edit_insert(query,var):
    
    cur.execute(query,var)
    

def sql_delete(query,var):
    
    cur.execute(query,var)"""
