import unittest 
import os

os.environ['TESTING'] = 'true'
from app import app
class AppTestCase(unittest.TestCase): 
    def setUp(self):
        self.client = app.test_client()
    def test_home(self):
        response = self.client.get("/") 
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Marcela Obeso</title>" in html
        assert "<h2>Education:</h2>" in html
        assert "<h2>Work Experience:</h2>" in html
        assert "Hobbies" in html

    def test_hobbies(self):
        response = self.client.get("/hobbies")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<h2>Hobbies</h2>" in html
        
    def test_timeline(self):
        #Test Get
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        #Test post
    def test_timeline_post_and_delete(self):
        response = self.client.post("/api/timeline_post", data={
            'name': 'Test',
            'email': 'Test@test.com',
            'content': 'Testing 123.'
        })
        json = response.get_json()
        assert response.status_code == 201
        assert json["id"] == 1
        assert json["name"] == 'Test'
        assert json["content"] == 'Testing 123.'
        #Test Delete
        response = self.client.delete("/api/timeline_post/1")
        assert response.status_code == 200
        response = self.client.delete("/api/timeline_post/2")
        assert response.status_code == 404
        response = self.client.get("/api/timeline_post")
        json = response.get_json()
        assert len(json["timeline_posts"]) == 0
        
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
        