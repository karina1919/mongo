
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
courses = db["courses"]

course = {
    'author': 'Inna',
    'course': 'Maths',
    'price': 95,
    'rating': 3
}

course1 = {
    'author': 'Nastya',
    'course': 'History',
    'price': 35,
    'rating': 2
}


result = courses.insert_one(course)
print(result)


result1 = courses.insert_one(course1)
print(result1)