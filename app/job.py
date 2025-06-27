class job_entry:
    def __init__(self, title, company_name, start_date, description, skills, end_date="Present"):
        self.title = title
        self.company_name = company_name
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.skills = skills