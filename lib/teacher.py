import random
from user import User

class Teacher(User):
    knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
    ]

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = Teacher.knowledge.copy()  # instance copy of knowledge list

    def teach(self):
        # Choose a random index in self.knowledge list and return the element
        index = random.randint(0, len(self.knowledge) - 1)
        return self.knowledge[index]
