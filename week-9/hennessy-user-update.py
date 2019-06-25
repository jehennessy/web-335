# Title:  hennessy-user-service.py
# Author: Professor Krasso
# Date:   25 June 2019
# Modified By: Jordan Hennessy
# Description: Updating and Deleting Documents

# imports
from pymongo import MongoClient
import pprint
import datetime

# connect to local MongoDB
client = MongoClient('localhost', 27017)
db = client.web335

# update user email by employee id
db.users.update_one(
  {"employee_id": "2749374"},
  {
    "$set":{
      "email": "jehennessy@my365.bellevue.edu"
    }
  }
)

# print email, first_name, last_name and employee_id fields
pprint.pprint(db.users.find_one({"employee_id": "2749374"}, {"_id": False, "date_created": False}))


