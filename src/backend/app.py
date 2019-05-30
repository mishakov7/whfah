from flask import Flask, request
from flask_cors import CORS
from recipe import findRecipe, processRecipe, randomRecipe, getRecipe
import requests

# # # # # # # # # # # # # # # # # # 
#
#              FLASK
#
# # # # # # # # # # # # # # # # # # 

website = Flask(__name__)
CORS(website)

# this is where we get the list of ingredients from the user  ??? myaeb
@website.route("/userIngredients", methods = ['POST', 'GET'])
def input_list():
   global ingredSent
   while request.method == 'POST':
      ingredSent = request.form.getlist('ingredient')
      break

   return ','.join(ingredSent)

@website.route("/recipe", methods = ['POST','GET'])
def recipeRoute():
   global url
   if request.method == 'GET':
      recipe, rawURL = getRecipe(input_list())

   url = requests.post('http://localhost:5000/URL', rawURL)
   return "<h3>Instructions</h3>" + str(recipe)

@website.route("/URL", methods = ['POST','GET'])
def urlRoute():
   global URL
   while request.method == 'POST':
      URL = request.data
      break

   return URL

if __name__ == '__main__':
   website.debug = True
   website.port = 5000
   website.threaded = True
   website.run()