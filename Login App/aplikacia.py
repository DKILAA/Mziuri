from flask import Flask
from database import *

app = Flask(__name__)
init_db()


@app.route("/register/<username>/<password>")
def register(username, password):
    user = insert_user(username, password)
    return user


@app.route("/login/<username>/<password>")
def login(username, password):
    if validate_user(username, password):
        return "AUTHENTICATED"
    return "NOT FOUND"

@app.route("/users")
def get_users():
    return {"users": get_all_users()}

@app.route("/users/<int:id>")
def get_user(id):
    user = get_user_by_id(id)
    if user:
        return user
    return {"message": "User not found"}


@app.route("/delete/<int:id>")
def delete_user(id):
    if delete_user_by_id(id):
        return {"message": "Success"}
    return {"message": "Not found"}

@app.route("/update/<int:id>/<username>/")
def update_username(id, username):
    result = update_username_by_id(id, username)
    if result == True:
        return {"message": "Username updated"}
    elif result == "Username already exists":
        return {"message": "Username already exists"}
    return {"message": "Not found"}

if __name__ == "__main__":
    app.run(debug=True)