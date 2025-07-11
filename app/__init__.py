import os
import json
import datetime
from flask import Flask, render_template, request
from peewee import MySQLDatabase, CharField, TextField, DateTimeField, Model
from playhouse.shortcuts import model_to_dict
from dotenv import load_dotenv
from app.entries import education_entry, hobby_entry, country_entry, job_entry




# Load our static content from JSON file
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

load_dotenv()

# Initialize Flask app
app = Flask(__name__)
# Initialize MySQL database connection
# Ensure you have the MySQL server running and the database created
mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
                     user=os.getenv("MYSQL_USER"),
                     password=os.getenv("MYSQL_PASSWORD"),
                     host=os.getenv("MYSQL_HOST"), 
                     port=3306
)
print("Database connection established.")
print(mydb)

# Define the TimeLinePost model
class TimeLinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimeLinePost], safe=True)



                     
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
def post_timeline_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimeLinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post), 201

@app.route('/api/timeline_post', methods=['GET'])
def get_timeline_posts():
    return {
        'timeline_posts': [ model_to_dict(post) for post in TimeLinePost.select().order_by(TimeLinePost.created_at.desc()) ]
    }

@app.route('/api/timeline_post/<int:post_id>', methods=['DELETE'])
def delete_timeline_post(post_id):
    try:
        post = TimeLinePost.get_by_id(post_id)
        post.delete_instance()
        return 'Entry removed', 200
    except TimeLinePost.DoesNotExist:
        return {'error': 'Post not found'}, 404