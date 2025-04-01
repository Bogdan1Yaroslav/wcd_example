import datetime
from flask import Blueprint, request, redirect, url_for, render_template, jsonify, make_response
from jwt import encode

from config import SECRET_KEY, USERS, TOKEN_EXPIRE_PERIOD

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")

        if USERS.get(username) == password:
            access_token = encode(
                {
                    "username": username,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=TOKEN_EXPIRE_PERIOD)
                },
                SECRET_KEY,
                algorithm="HS256"
            )

            response = make_response(jsonify({"message": "Successful login"}))
            response.set_cookie("jwt", access_token, httponly=False, path="/")

            return response

        return jsonify({"error": "Invalid login or password"}), 401

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    response = redirect(url_for("auth.login"))
    response.set_cookie("jwt", "", expires=0)
    return response
