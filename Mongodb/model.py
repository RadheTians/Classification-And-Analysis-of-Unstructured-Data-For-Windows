
import pymongo
from pymongo import MongoClient
import urllib
from urllib import request
import json

client = MongoClient()

db = client.db_demo

collection_demo  = db.collection_demo


url_str = 'https://graph.facebook.com/http://www.jmu.edu'

response = request.urlopen(url_str)

html_str = response.read().decode("utf-8")

json_data = json.loads(html_str)
print(json_data)
collection_demo.insert(json_data)

cursor = collection_demo.find()

for document in cursor:
    print(document)
