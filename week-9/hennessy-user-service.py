# Title:  hennessy-user-service.py
# Author: Professor Krasso
# Date:   25 June 2019
# Modified By: Jordan Hennessy
# Description: Querying and Creating Documents


#imports
from pymongo import MongoClient

import pprint

import datetime


# connect to local MongoDB instance
client = MongoClient('localhost', 27017)

db = client.web335


# new user document
user = {

  "first_name": "Jessie",
  "last_name": "McGarth",
  "email": "jegarth@yahoo.com",
  "employee_id": "2749374",
  "date_created": datetime.datetime.utcnow()
}

#insert new user document
user_id = db.users.insert_one(user).inserted_id


# output id
print(user_id)

# find by employee id
employee_id = "2749374"

pprint.pprint(db.users.find_one({"employee_id": employee_id}))
