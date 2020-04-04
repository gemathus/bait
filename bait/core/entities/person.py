class Person:
    def __init__(self, name, last_name, email):
        self.name = name
        self.last_name = last_name
        self.email = email
    
    def full_name(self):
       return "{} {}".format(self.name, self.last_name)
