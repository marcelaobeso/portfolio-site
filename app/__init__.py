import os
import json
import datetime
from peewee import *
from pprint import pprint
from playhouse.shortcuts import model_to_dict
from flask import Flask, render_template, request
from dotenv import load_dotenv
from app.education import education_entry
from app.hobby import hobby_entry
from app.country import country_entry
from app.job import job_entry

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"), user=os.getenv("MYSQL_USER"), password=os.getenv("MYSQL_PASSWORD"), host=os.getenv('MYSQL_HOST'), port=3306)



class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])
    
    
with open('./app/static/content/content.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    about, title, hobbies_list, picture, edu_list, job_list, travels = data["about"], data["title"], data["hobbies-list"], data["picture"], data["education"], data["jobs"], data["travels"]

edu_items, job_items, hobbies_items, country_list = [], [], [], []
for hobby in hobbies_list:
    hobbies_items.append(hobby_entry(**hobby))
    
for edu in edu_list:
    edu_items.append(education_entry(**edu))
    
for job in job_list:
    job_items.append(job_entry(**job))

for country in travels:
    country_list.append(country_entry(**country))


@app.route('/')
def index():
    return render_template('index.html',
                           title=title,
                           about=about["content"],
                           picture=data["picture"],
                           edu_items=edu_items,
                           job_items=job_items,
                           countries=country_list,
                           url=os.getenv("URL"))

@app.route('/hobbies', methods=['GET'])
def hobbies():
    return render_template('hobbies.html', picture=data["picture"],  title=title, hobbieTitle="Hobbies", list=hobbies_items, edu_list=edu_list, job_list=job_list, coutries=country_list, url=os.getenv("URL"))



@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    
    return model_to_dict(timeline_post)

@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts':[
            model_to_dict(p)
            for p in
            TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
        
    }


print(get_time_line_post())
@app.route('/timeline', methods=['GET'])
def timeline():
    return render_template('timeline.html', postlist=get_time_line_post()['timeline_posts'] )

TimelinePost.select(TimelinePost.name, TimelinePost.email, TimelinePost.content)
    
