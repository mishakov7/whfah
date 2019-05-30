import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

#  Necessary variables for MongoDB
client = MongoClient("127.0.0.1", 27017)
database = client.recipe
t_collection = database.recipe_title
src_collection = database.sources
in_collection = database.ingredient_content

# This function can be used for each of the extraneous elements
def displayElement(collection, URL):
    item = collection.find( {"url": URL}, 
                           {"_id": 0, "url": 1, "tag": 1, "attribute": 1, 
                           "content": 1})

    if item.count() > 1:
        count = 0
        displayList = [[x for x in range(4)] for y in range(item.count())]

        for i in item:

            url = i.get("url")
            tag = i.get("tag")
            attribute = i.get("attribute")
            content = i.get("content")

            displayList[count][0] = url
            displayList[count][1] = tag
            displayList[count][2] = attribute
            displayList[count][3] = content

            if  tag == "" or attribute == "" or content == "":
                tag = '<div style="display: none;"></div>'

            count += 1
        return displayList 

    else: 
        for i in item:
            url = i.get("url")
            tag = i.get("tag")
            attribute = i.get("attribute")
            content = i.get("content")

        display = parseElement(url, tag, attribute, content)
        return display

def parseElement(url, tag, attribute, content):

   response = requests.get(url)
   page = response.text
   soop = BeautifulSoup(page, 'html.parser')

   # This alone will retain the html tags
   element = soop.find(tag, attrs={attribute: content})

   return element