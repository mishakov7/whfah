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

MATCH_URL = requests.get('http://localhost:5000/URL').text

@displaysite.route("/title", methods=['GET','POST'])
def titleRoute():
   rawtitle = displayElement(t_collection, MATCH_URL)
   title = rawtitle.text.strip()
   return str(title)

@displaysite.route("/sources")
def sourceRoute():
   rawsources = displayElement(src_collection, MATCH_URL)
   sources = rawsources.text.strip()
   return '<a href="' + MATCH_URL + '" target="_blank" style="text-decoration: none;">' + str(sources) + '</a>'

@displaysite.route("/ingredients")
def ingredientRoute():
   ingredients = displayElement(in_collection, MATCH_URL)
   return "<h3>Ingredients</h3>" + str(ingredients)

if __name__ == '__main__':
   displaysite.debug = True
   displaysite.port = 5500
   displaysite.threaded = True
   displaysite.run()