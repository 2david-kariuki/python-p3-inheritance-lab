from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []  # empty list at initialization

    def learn(self, new_knowledge):
        # Add the string new_knowledge to self.knowledge list
        self.knowledge.append(new_knowledge)
