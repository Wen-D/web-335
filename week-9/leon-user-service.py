# ========================================
# Title: Exercise 9.2 
# Author: Richard Krasso
# Modified by: Wendy Leon
# Date:  12/8/20
# Description: Querying and Creating Documents
# =========================================

from pymongo import MongoClient

import pprint

import datetime

client=MongoClient('localhost', 27017)

db=client.web335

user={
    "first_name": "Wen",
    "last_name": "D",
    "email": "email@domain.com",
    "employee_id": "001",
    "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"employee_id": "0000001"}))