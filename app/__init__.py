import os
import json
from flask import Flask, render_template, request
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
with open('./app/static/content/content.json', 'r', encoding='utf-8') as file:
    content = json.load(file)



@app.route('/')
def index():
    return render_template('index.html', title=content["title"], about=content["about"]["content"], url=os.getenv("URL"))

