#!/usr/bin/env python2

from flask import Flask, render_template, redirect, url_for, request
import mysql.connector
from base64 import b64encode as enc
from base64 import b64decode as dec

app = Flask(__name__)

db = mysql.connector.connect(host='107.181.191.59', 
                            user='root', 
                            passwd='P@$$06281a', 
                            database='cur_Monitor'
                            ) 
                           # user='reader', 
                           # passwd='R#]7>y#q<AM', 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/commodities', methods=['GET', 'POST'])
def commodities_all():

    if request.method == 'POST':
        form = request.form
        return redirect(url_for('commodities', query = enc(form['query']))) 
    else:
        return redirect(url_for('commodities', query = enc('.*')))

@app.route('/commodities/<query>/')
def commodities(query):
    query = dec(query) 
    cursor = db.cursor()
    sql = "SELECT * FROM Commodity_Data WHERE commodity REGEXP %s"
    cursor.execute(sql, (query,))
    results = cursor.fetchall()
    return render_template('commodities.html', results=results)

@app.route('/currency')
def currency():
    return render_template('currency.html')

@app.route('/news')
def news():
    return render_template('news.html')


@app.after_request
def add_header(response):
    response.cache_control.no_cache = True 
    response.cache_control.no_store = True 
    response.cache_control.must_revalidate = True 
    return response

if __name__ == '__main__':
    app.run()
