from flask import (
    Flask,
    request
)

from datetime import datetime

from app.database import user

VERSION = "1.0.0"

app = Flask(__name__)

@app.get("/ping")
def get_ping():
    response = {
        "status":"ok",
        "message":"pong"
    }
    return response




@app.get("/version")
def get_version():
    response = {
        "status": "ok",
        "version": VERSION,
        "server_time": datetime.now().strftime("%F %H:%M:%S")
    }
    return response


@app.get("/users")
def get_all_users():
    user_list=user.scan()
    out={
        "status":"ok",
        "users": user_list
    }
    return out


@app.get("/users/<int:pk>")
def get_user_by_id(pk):
    user_obj = user.select_by_id(pk)
    out={
        "status": "ok",
        "user": user_obj
    }
    return out


@app.post("/users")
def create_user():
    raw_data =request.json
    user.insert(raw_data)
    out={
        "status":"ok",
        "message":"created"
    }
    return out, 201

@app.put("/users/<int:pk>")
def update_user(pk):
    raw_data=request.json
    user.update(pk, raw_data)
    return "", 204

@app.delete("/users/<int:pk>")
def deactivate_user(pk):
    user.deactivate(pk)
    return "", 204

