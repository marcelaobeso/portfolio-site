import json

class country_entry:
    def __init__(self, name, top, left):
        self.name = name
        self.top = top
        self.left = left

class job_entry:
    def __init__(self, title, company_name, start_date, description, skills, end_date="Present"):
        self.title = title
        self.company_name = company_name
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.skills = skills

class education_entry:
    def __init__(self, name, degree, start_date, end_date="Present", grade=None, skills=None):
        self.name = name
        self.degree = degree
        self.start_date = start_date
        self.end_date = end_date
        self.grade = grade
        self.skills = skills

class hobby_entry:
    def __init__(self, img_url, name, description=""):
        self.img_url = img_url
        self.name = name
        self.description = description

class about_entry:
    def __init__(self, content, title, picture):
        self.content = content
        self.title = title
        self.picture = picture
# Load our static content from JSON file
with open('./app/static/content/content.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    about, title_content, hobbies_list, picture_img, edu_list, job_list, travels = data["about"], data["title"], data["hobbies-list"], data["picture"], data["education"], data["jobs"], data["travels"]
edu_items, job_items, hobbies_items, country_list = [], [], [], []
about_items = {
    "title": title_content,
    "content": about["content"],
    "picture": picture_img
}
about = about_entry(**about_items)
# picture = data["picture"]

for hobby in hobbies_list:
    hobbies_items.append(hobby_entry(**hobby))
    
for edu in edu_list:
    edu_items.append(education_entry(**edu))
    
for job in job_list:
    job_items.append(job_entry(**job))

for country in travels:
    country_list.append(country_entry(**country))