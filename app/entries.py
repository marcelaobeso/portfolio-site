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