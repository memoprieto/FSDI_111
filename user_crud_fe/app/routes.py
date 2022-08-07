from flask import (
    Flask,
    render_template
)
import requests

URL = "http://127.0.0.1:5000/users"

app = Flask(__name__)


@app.get("/")
def get_index():
    return render_template("index.html")


@app.get("/users")
def display_users():
    user_list = requests.get(URL)
    render_template("users.html", users=user_list)