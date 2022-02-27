from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import numpy as np
import pandas as pd
import xlrd
import os
import random
import pprint

app = Flask(__name__)
df = None
#df2 = None;

@app.route("/")
def home():
    return render_template('base.html')

#testing
@app.route("/Main")
def main():

    return "<h1>Welcome to Centrak Field Services Dashboard<h1>"
    
    
@app.route("/about")
def about():
    return "<h1>THIS IS CENTRAK FIELD SERVICES DASHBOARD THIS WILL HELP YOU NAVIGATE INFORMATION FROM FAES<h1>"

@app.route('/upload')
def upload_file():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file1():
   if request.method == 'POST':
      f = request.files.get('file')
      print(f)

      #f.save(secure_filename(f.filename))
      global df1
      df1 = pd.read_csv (f)
      #print(adm.head())
#adm.to_csv (r'ActiveMonitorData', index=None)
      #return render_template('table.html', column_names=df.columns.values, row_data=list(df.values.tolist()), zip=zip)
      return render_template('home.html')

@app.route('/uploader2', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      f = request.files.get('file')
      print(f)

      #f.save(secure_filename(f.filename))
      global df2
      df2 = pd.read_csv (f)
      #print(adm.head())
#adm.to_csv (r'ActiveMonitorData', index=None)
      page = [{'userId': '2', 'customers': '43'},{'userId': '1', 'customers': '35'}]
      #return render_template('table.html', column_names=df2.columns.values, row_data=list(df2.values.tolist()), zip=zip)      
      return render_template('home.html')

@app.route('/process', methods = ['GET', 'POST'])
def process():
   if request.method == 'POST':
      global df2
      global df1
      result = processFiles()
      return render_template('table.html', column_names=df1.columns.values, row_data=list(df1.values.tolist()), zip=zip)      

def processFiles():
       for key in df2.keys():
              print(key)
              for i,j in df1.iterrows():
                     print(i,j)


if __name__ == '__main__':
   app.run(debug = True)



