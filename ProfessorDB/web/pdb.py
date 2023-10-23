from flask import Flask, render_template, request
import pymongo
import re

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client['professors_db']
mongo_collection = mongo_db['professors']

# distinct values for department and college
departments = mongo_collection.distinct('Department')
colleges = mongo_collection.distinct('College')

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        professors = []
    else:
        match = {}
        if request.form['department'] != "any":
            match['Department'] = request.form['department']
        if request.form['college'] != "any":
            match['College'] = request.form['college']
        if request.form['name']:
            match['Name'] = {'$regex': request.form['name']}
        if request.form['aoe']:
            match['AOE'] = {'$regex': request.form['aoe']}
        search_results = mongo_collection.aggregate([
            {
                "$match": match
            }
        ])
        professors = list(search_results)
    return render_template('index.html', professors=professors, departments=departments, colleges=colleges)

