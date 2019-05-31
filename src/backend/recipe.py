import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import random

#  Necessary variables for MongoDB
client = MongoClient("127.0.0.1", 27017)
database = client.recipe
r_collection = database.ingredients

#  findRecipe(ingredient, ingredients)
#  Searches through the Mongo database to retrieve a list
#  of recipes depending on the user's input
#
#  RETURNS: list of recipes
#
def findRecipe(ingredient, ingredients):

   # Initialize counter
   count = 0

   #  Query that pulls all records that contain the ingredient
   item = r_collection.find( {"ingredients": ingredient}, 
                           {"_id": 0, "url": 1, "tag": 1, "attribute": 1, 
                           "content": 1})

   # Initialize list that will store query of recipes
   recipeQuery = [[x for x in range(4)] for y in range(item.count())]

   for recipe in item:

      url = recipe.get("url")
      tag = recipe.get("tag")
      attribute = recipe.get("attribute")
      content = recipe.get("content")

      recipeQuery[count][0] = url
      recipeQuery[count][1] = tag
      recipeQuery[count][2] = attribute
      recipeQuery[count][3] = content

      count += 1
   return recipeQuery


#  processRecipe(url, tag, attribute, content)
#  Parses the html from a web page into text.
#
#  RETURNS: recipe that has been scraped
#
def processRecipe(url, tag, attribute, content):

   response = requests.get(url)
   page = response.text
   soop = BeautifulSoup(page, 'html.parser')

   # This alone will retain the html tags
   recipe_elmt = soop.find(tag, attrs={attribute: content})

   return str(recipe_elmt)

def randomRecipe(recipeFirst, recipeLast):
   index = random.randint(recipeFirst, recipeLast)
   return index

#s # # # # # # # # # # # # # # # # # # 
#
#       RECIPE PROCESSING
#
# # # # # # # # # # # # # # # # # # 

def getRecipe(ingredients):
   # Initialize iterator
   i = 0

   # Initialize lists
   recipeList = []
   recipeURLs = []

   # This makes a list out of the flask input
   ingredientList = ingredients.split(",")

   # Retrieve the recipes needed for the ingredients the user entered.
   for item in ingredientList:

      # Collects all possible recipes for the user's query into a list
      recipes = findRecipe(item, ingredientList)

      for i in range(len(recipes)):
         # Parses the HTML from the recipe websites into elements
         recipeText = processRecipe(recipes[i][0], recipes[i][1], recipes[i][2], recipes[i][3])
         recipeList.append(recipeText)
         recipeURLs.append(recipes[i][0])

   # Have the program pick a random recipe from the list you made above
   randIdx = randomRecipe(0, len(recipeList))

   return recipeList[randIdx], recipeURLs[randIdx]
