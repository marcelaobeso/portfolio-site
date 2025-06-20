class education_entry:
    def __init__(self, name, degree, start_date, end_date, grade=None, skills=None):
        self.name = name
        self.degree = degree
        self.start_date = start_date
        self.end_date = end_date
        self.grade = grade
        self.skills = skills