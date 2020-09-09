from flask import Flask, render_template, request
import os
import sqlite3
import time

import sys
#===This (sys.path.append) is needed for VisualStudioCode
#sys.path.append("C:\\Users\\yourUserName\\yourPythonProjectDirectory\\")

from pyprofi.cc02_clientservermgmt_app.dbsqlite__clientservermgmt_app__tbl__ciud__m import cSQLite_ClientServerMgmt_App__ciud

from pyometry.time.time__m import cTime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enternew')
def new_student():
    return render_template('clientservermgmt.html')

@app.route('/addrecord', methods=['POST', 'GET'])
def addrecord():
    
    msg = "..."

    if request.method == 'POST':
            clientserver_name = request.form['clientserver_name']
            clientserver_addr = request.form['clientserver_addr']
            clientserver_city = request.form['clientserver_city']
            clientserver_ipsubnet = request.form['clientserver_ipsubnet']

            print("===============================================================")
            print("==  for testing, lets print the return values in the console   ")
            print("===============================================================")
            print(clientserver_name)
            print(clientserver_addr)
            print(clientserver_city)
            print(clientserver_ipsubnet)


            PWD = os.path.realpath(os.path.dirname(__file__))

            result = cSQLite_ClientServerMgmt_App__ciud("")

            result.insert_row_of_data__into__ClientServerMgmt(clientserver_name,clientserver_addr,clientserver_city,clientserver_ipsubnet)
        
    return render_template('home.html')


@app.route('/list')
def list():

    result = cSQLite_ClientServerMgmt_App__ciud("")
    six_col_table = result.get_six_col_table__w__verified_ipsubnetaddress_dynamic()

    return render_template("list.html", rows=six_col_table)

@app.route('/sign')
def sign():
    print("..... in sign method")    

if __name__ == '__main__':
    #db.create_all()
    #app.run(debug=True)

    app.run(host="127.0.0.1", port=80, debug=True)
