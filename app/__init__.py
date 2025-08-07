import os
import datetime
from flask_cors import cross_origin, CORS
from flask import Flask, render_template, request, abort
from peewee import MySQLDatabase, CharField, TextField, DateTimeField, Model, SqliteDatabase
from playhouse.shortcuts import model_to_dict
from dotenv import load_dotenv
from app.entries import edu_items, job_items, hobbies_items, country_list, about


load_dotenv()
# Initialize Flask app
app = Flask(__name__)

# Initialize MySQL database connection
# Ensure you have the MySQL server running and the database created
if os.getenv("TESTING") == "true" :
    print("Running in test mode")
    mydb = SqliteDatabase('file: memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase (os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306)

print("Database connection established.")
print(mydb)

# Define the TimeLinePost model
class TimeLinePost(Model):
    '''Model for timeline posts'''
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        '''Database configuration'''
        database = mydb

mydb.connect()
mydb.create_tables([TimeLinePost], safe=True)

@app.route('/')
def index():
    """Render the home page with about, education, and work experience."""
    return render_template('index.html',
                           title=about.title,
                           about=about.content,
                           picture=about.picture,
                           edu_items=edu_items,
                           job_items=job_items,
                           countries=country_list,
                           url=os.getenv("URL"))

@app.route('/hobbies', methods=['GET'])
def hobbies():
    """Render the hobbies page."""
    return render_template(
        'hobbies.html',
        picture=about.picture,
        title=about.title,
        hobbieTitle="Hobbies",
        list=hobbies_items,
        coutries=country_list,
        url=os.getenv("URL")
    )

@app.route('/api/timeline_post', methods=['POST'])
def post_timeline_post():
    """Create a new timeline post."""
    print('request.form:', request.form)
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    # Validate input
    if not name or not content or not email:
        abort(400, 'Missing name, email or content')
    if '@' not in email or '.' not in email.split('@')[-1]:
        abort(400, 'Invalid email format')
    timeline_post = TimeLinePost.create(name=name, email=email, content=content)

    return model_to_dict(timeline_post), 201

@app.route('/api/timeline_post', methods=['GET'])
def get_timeline_posts():
    """Retrieve all timeline posts."""
    time_line_list = TimeLinePost.select().order_by(TimeLinePost.created_at.desc())
    return {
        'timeline_posts': [ model_to_dict(post) for post in time_line_list ]
    }

@app.route('/api/timeline_post/<int:post_id>', methods=['DELETE'])
def delete_timeline_post(post_id):
    """Delete a timeline post by ID."""
    try:
        post = TimeLinePost.get_by_id(post_id)
        post.delete_instance()
        return 'Entry removed', 200
    except TimeLinePost.DoesNotExist:
        return {'error': 'Post not found'}, 404

@app.route('/timeline', methods=['GET'])
@cross_origin()  # Allow cross-origin requests for this endpoin
def timeline():
    """Render the timeline page with all posts."""
    timeline_posts = TimeLinePost.select().order_by(TimeLinePost.created_at.desc())
    return render_template('timeline.html', posts=timeline_posts, url=os.getenv("URL"))
