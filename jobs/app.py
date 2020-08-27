import sqlite3
import datetime
from flask import Flask, render_template, g, request, redirect, url_for

PATH = 'db/jobs.sqlite'

app = Flask(__name__)



@app.route('/')
@app.route('/jobs')
def jobs():
    #jobs = execute_sql('SELECT job.id, job.title, job.description, job.salary, employer.id as employer_id, employer.name as employer_name FROM job JOIN employer ON employer.id = job.employer_id')
    return render_template('index.html')#, jobs=jobs)