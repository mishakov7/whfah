from flask import Flask, request
from flask_cors import CORS
from display import t_collection, src_collection, in_collection, displayElement, parseElement
import requests

# # # # # # # # # # # # # # # # # # 
#
#              FLASK
#
# # # # # # # # # # # # # # # # # # 

displaysite = Flask(__name__)
CORS(displaysite)

#  This is taking in the recipe's URL from a route on /backend
MATCH_URL = requests.get('http://localhost:5000/URL').text

#  This is taking in the recipe's ingredients from a route on /backend
MATCH_INGRED = requests.get('http://localhost:5000/userIngredients').text

#  Displays the title for the recipe
#
#  REQUEST:    none
#  RESPONSE:   recipe title
#  RETURNS:    recipe title
#
@displaysite.route("/title", methods=['GET','POST'])
def titleRoute():
   rawtitle = displayElement(t_collection, MATCH_URL)
   title = rawtitle.text.strip()
   return str(title)

#  Displays the author or source for the recipe
#
#  REQUEST:    none
#  RESPONSE:   recipe source
#  RETURNS:    recipe source
#
@displaysite.route("/sources")
def sourceRoute():
   rawsources = displayElement(src_collection, MATCH_URL)
   sources = rawsources.text.strip()
   return '<a href="' + MATCH_URL + '" target="_blank" style="text-decoration: none;">' + str(sources) + '</a>'

#  Displays the ingredients
#
#  REQUEST:    none
#  RESPONSE:   recipe ingredients
#  RETURNS:    recipe ingredients
#
@displaysite.route("/ingredients")
def ingredientRoute():
   ingredientsraw = displayElement(in_collection, MATCH_URL)
   ingredientsstr = str(ingredientsraw)
   ingredients = ingredientsstr.split()
   ingredList = MATCH_INGRED.split(',')

   for i in ingredList:
      for element in ingredients:
         print(element)
         match = element.find(i)
         if match != -1 and match != None:
            print("ENTERED")
            print(match)
            print(element[match])
         else:
            continue

   return "<h3>Ingredients</h3>" + str(ingredientsraw)

if __name__ == '__main__':
   displaysite.debug = True
   displaysite.port = 5500
   displaysite.threaded = True
   displaysite.run()