# tests/test_app. py
import unittest 
import os
os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest. TestCase):
    def setUp(self):
        self.client = app.test_client()
    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Name Of the Developer</title>" in html
        # Add more tests relating to the home page
        assert "About Me" in html
        assert "<h2>Education:</h2>" in html
        assert "Hobbies" in html
        assert "<h2>Work Experience:</h2>" in html

    def test_timeline(self):
        response = self.client.get("/api/timeline_post" )
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json 
        # Add more tests relating to the /api/timeline_post GET and POST apis

    def test_post_timeline_post(self):
        response = self.client.post("/api/timeline_post", data={
            'name': 'John Doe',
            'email': 'john@mail.com',
            'content': 'This is a test post.'
        })
        json = response.get_json()
        assert response.status_code == 200
        assert "id" in json
        assert json["name"] == 'John Doe'

    # Add more tests relating to the timeline page
    def test_hobbies(self):
        response = self.client.get("/hobbies")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<h2>Hobbies</h2>" in html


    def test_malformed_timeline_post(self) :
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "<h1>Bad Request</h1>" in html
        # POST request with empty content
        response = self. client. post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Missing name, email or content" in html
        # POST request with malformed email
        response = self. client. post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John! "})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email format" in html