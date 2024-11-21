from flask import Flask, render_template
import keys
app = Flask(__name__)
@app.route("/")
def index():
    do_cool_things()
    fruits = [
        {"name": "apples", "quantity": 3},
        {"name": "oranges", "quantity": 2},
        {"name": "strawberries", "quantity": 6}
    ]

    newfruits = []
    for fruit in fruits:
        if fruit["quantity"] <= 3 and fruit["name"].startswith('o'):
            print(fruit["name"])
            newfruits.append(fruit)
            
    return render_template("index.html", fruits=newfruits)

def do_cool_things():
    print("I print the API key here, without having it in this file: ", keys.MY_SECRET_API_KEY_1)
