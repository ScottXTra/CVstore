from flask import Flask, render_template
import json
from flask import request
from db import setup_db , insert_company, insert_job,edit_job,remove_job,remove_company,insert_job_app,remove_job_app,get_job_apps,update_job_app_status
app = Flask(__name__)

setup_db()
insert_company("Facebook")
insert_job("Ass eatta","http://facebook.com",6969420,1)
insert_job_app(1,7)
#remove_job_app(5)
#remove_job_app(3)
#remove_job(3)
#update_job_app_status(6,4)
@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/auth/login')
def about():
    return render_template('/auth/login.html')

@app.route('/api/get_job_apps')
def get_job_apps_endpoint():
    print(get_job_apps())
    return json.dumps(get_job_apps())

@app.route('/api/update_job_app_status', methods = ['POST'])
def update_job_app_status_endpoint():
    data = request.form
    print(data['job_id'])
    update_job_app_status(data['job_id'],data['status_id'])
    return 'Updated'

@app.route('/api/remove_job', methods = ['POST'])
def remove_job_endpoint():
    data = request.form
    remove_job_app(data['job_id'])
    remove_job(data['job_id'])
    
    return 'Job removed'

