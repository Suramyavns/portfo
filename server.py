from flask import Flask as fl
from flask import render_template
from flask import request
import csv
app = fl(__name__)

@app.route('/')
def HomePage():
    return render_template("index.html")

@app.route('/<string:pagename>')
def Page(pagename):
    return render_template(f'{pagename}')

@app.route("/submit_form",methods=['POST'])
def submit_form():
    data = request.form.to_dict()
    with open(r'./contacts.csv','+a') as fh:
        writer = csv.writer(fh, lineterminator='\n')
        writer.writerow([data['email'],data['subject'],data['message']])
        fh.close()
    return render_template('thankyou.html',name=data['email'])