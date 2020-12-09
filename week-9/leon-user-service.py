# =============================================
# Title: Exercise 9.2 
# Author: Richard Krasso
# Modified by: Wendy Leon
# Date:  12/8/20
# Description: Querying and Creating a Document
# ==============================================

from pymongo import MongoClient

import pprint

import datetime

client=MongoClient('localhost', 27017)
#use web 335
db=client.web335
#create user
user={
    "first_name": "Wen",
    "last_name": "D",
    "email": "email@domain.com",
    "employee_id": "001",
    "date_created": datetime.datetime.utcnow()
}
#insert user
user_id = db.users.insert_one(user).inserted_id
#print user id
print(user_id)
#print user w/ id 001
pprint.pprint(db.users.find_one({"employee_id": "001"}))