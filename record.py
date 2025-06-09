

class Record:
    def __init__(self, title, company, date, location):
        self.title = title
        self.company = company
        self.date = date
        self.location = location

    def __repr__(self):
        return f"{self.title}, {self.company}, {self.date}, {self.location}"