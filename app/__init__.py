import os
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv
from app.education import education_entry

load_dotenv()
app = Flask(__name__)
with open('./app/static/content/content.json', 'r', encoding='utf-8') as file:
    content = json.load(file)

edu_1_json = content["education"]["entry 1"]

edu_1 = education_entry(edu_1_json["name"], 
                        edu_1_json["degree"], 
                        edu_1_json["start_date"], 
                        edu_1_json["end_date"], 
                        edu_1_json["grade"], 
                        edu_1_json["skills"])

@app.route('/')
def index():
    return render_template('index.html', 
                           title=content["title"], 
                           about=content["about"]["content"], 
                           picture=content["picture"],
                           institute_name=edu_1.name,
                           degree=edu_1.degree,
                           start_date=edu_1.start_date,
                           end_date=edu_1.end_date,
                           grade=edu_1.grade,
                           skills =edu_1.skills,
                           url=os.getenv("URL"))

app.run()

