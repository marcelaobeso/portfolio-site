import os
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv
from app.education import education_entry
from app.hobby import hobby_entry
from app.job import job_entry

load_dotenv()
app = Flask(__name__)
with open('./app/static/content/content.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    about, title, hobbies_list, picture, edu_list, job_list = data["about"], data["title"], data["hobbies-list"], data["picture"], data["education"], data["jobs"]

edu_items, job_items, hobbies_items = [], [], []
for hobby in hobbies_list:
    hobbies_items.append(hobby_entry(**hobby))
    
for edu in edu_list:
    edu_items.append(education_entry(**edu))
    
for job in job_list:
    job_items.append(job_entry(**job))
    
@app.route('/')
def index():
    return render_template('index.html',
                           title=title,
                           about=about["content"],
                           picture=data["picture"],
                           edu_items=edu_items,
                           job_items=job_items,
                           url=os.getenv("URL"))

@app.route('/hobbies', methods=['GET'])
def hobbies():
    return render_template('hobbies.html', picture=data["picture"],  title=title, hobbieTitle="Hobbies", list=hobbies_items, edu_list=edu_list, job_list=job_list, url=os.getenv("URL"))
