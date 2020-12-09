# =============================================
# Title: Exercise 9.3
# Author: Richard Krasso
# Modified by: Wendy Leon
# Date:  12/8/20
# Description: Updating and Deleting Documents

# ==============================================

from pymongo import MongoClient

import pprint

import datetime

client = MongoClient('localhost', 27017)

#select DB
db = client.web335

#Update
db.users.update_one(
    {"employee_id":"008"},
    {
        "$set":{
            "email":"email@mydomain.com"
        }
    }
)

pprint.pprint(db.users.find_one({"employee_id":"0008"}))