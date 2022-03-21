from concurrent.futures.process import _threads_wakeups
from random import random
from urllib import response
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, ObjectId
import requests
import random
import json


app = Flask(__name__)


app.config['MONGO_URI']='mongodb://localhost/pokemonapi'
mongo = PyMongo(app)
db = mongo.db.equipo

def miPokemon(pokemon):

    name=""
    peso=""
    data={
        "name":"",
        "peso":pokemon["height"],
        "numero":pokemon["id"]
    }
    
    for forms in pokemon["forms"]:
        for name in forms["name"]:
            name = forms
            data["name"]+=str(name)
            break
        
    equipo = db.insert_one(data)
    
    return (data, equipo.inserted_id())

    


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/info',methods=["GET","POST"])
def inicio():
    cad=""
    cad+="URL:"+request.url+"<br/>"
    cad+="Método:"+request.method+"<br/>"
    cad+="header:<br/>"
    for item,value in request.headers.items():
        cad+="{}:{}<br/>".format(item,value)    
    cad+="información en formularios (POST):<br/>"
    for item,value in request.form.items():
        cad+="{}:{}<br/>".format(item,value)
    cad+="información en URL (GET):<br/>"
    for item,value in request.args.items():
        cad+="{}:{}<br/>".format(item,value)    
    cad+="Ficheros:<br/>"
    for item,value in request.files.items():
        cad+="{}:{}<br/>".format(item,value)
    return cad
@app.route("/pokemon", methods = ["GET"])
def Pokemon():
    
    id = random.randint(1, 950)
    url = 'https://pokeapi.co/api/v2/pokemon/'+str(id)
    response = requests.get(url)#json.loads(url)
    
    pokemon = json.loads(response.text)

    mis_pokemones = miPokemon(pokemon)


    return mis_pokemones

if __name__ == "__main__":
    app.run(debug =True)