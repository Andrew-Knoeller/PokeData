from flask import Flask, request, render_template
import urllib.request, json
import requests

import os

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        text = request.form.get("searchBox")
        url = "https://pokeapi.co/api/v2/pokemon/" + text
        response = requests.get(url)
        response_code = response.status_code

        if response_code != 404:
            data = response.json()
            return data
        else:
            err_msg = "Incorrect Pokémon name, please try again"
            return err_msg


    return render_template ("index.html")


@app.route('/name/')
def name():
    url = "https://pokeapi.co/api/v2/pokemon?limit=3000&offset=0"
    response = requests.get(url).text
    response_text = json.loads(response)

    names = []
    for key in response_text['results']:
        names.append([key['name']])
    return render_template("main.html", names=names)

@app.route('/number/')
def number():
    url = "https://pokeapi.co/api/v2/pokemon?limit=3000&offset=0"
    response = requests.get(url).text
    response_text = json.loads(response)

    numbers = []
    for key in response_text['results']:
        numbers.append([key['name']])
    return render_template("main.html", numbers=numbers)

@app.route('/type/')
def type():
    url = "https://pokeapi.co/api/v2/type/"
    response = requests.get(url).text
    response_text = json.loads(response)

    types = []
    for key in response_text['results']:
        types.append([key['name']])
        
    return render_template("main.html", types=types)

@app.route('/ability/')
def ability():
    url = "https://pokeapi.co/api/v2/ability?limit=500/"
    response = requests.get(url).text
    response_text = json.loads(response)

    abilities = []
    for key in response_text['results']:
        abilities.append([key['name']])
    return render_template("main.html", abilities=abilities)

@app.route('/move/')
def move():
    url = "https://pokeapi.co/api/v2/move?offset=20&limit=1000"
    response = requests.get(url).text
    response_text = json.loads(response)

    moves = []
    for key in response_text['results']:
        moves.append([key['name']])
    return render_template("main.html", moves=moves)

@app.route('/location/')
def location():
    url = "https://pokeapi.co/api/v2/location?offset=20&limit=1000"
    response = requests.get(url).text
    response_text = json.loads(response)

    locations = []
    for key in response_text['results']:
        locations.append([key['name']])
    return render_template("main.html", locations=locations)



if __name__ == '__main__':
    app.run(debug=True)
  