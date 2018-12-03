__author__ = "LuisSas"

import pymongo

uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['fullstack']
collection = database['students']

students = [student['mark'] for student in collection.find({}) if student['mark'] == 99]

print(students)
