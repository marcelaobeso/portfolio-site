import os
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv
from app.education import education_entry
from app.hobby import hobby_entry
from app.country import country_entry


load_dotenv()
app = Flask(__name__)
with open('./app/static/content/content.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    about, title, hobbies_list, picture, travels = data["about"], data["title"], data["hobbies-list"], data["picture"], data["travels"]

edu_1_json = data["education"]["entry 1"]

edu_1 = education_entry(edu_1_json["name"], 
                        edu_1_json["degree"], 
                        edu_1_json["start_date"], 
                        edu_1_json["end_date"], 
                        edu_1_json["grade"], 
                        edu_1_json["skills"])

hobbies_items = []
for hobby in hobbies_list:
    hobbies_items.append(hobby_entry(**hobby))

country_list = []
for country in travels:
    country_list.append(country_entry(**country))


@app.route('/')
def index():
    return render_template('index.html',
                           title=title,
                           about=about["content"],
                           picture=data["picture"],
                           institute_name=edu_1.name,
                           degree=edu_1.degree,
                           start_date=edu_1.start_date,
                           end_date=edu_1.end_date,
                           grade=edu_1.grade,
                           skills =edu_1.skills,
                           countries=country_list,
                           url=os.getenv("URL"))

@app.route('/hobbies', methods=['GET'])
def hobbies():
    return render_template('hobbies.html', picture=data["picture"],  title=title, hobbieTitle="Hobbies", list=hobbies_items, url=os.getenv("URL"))