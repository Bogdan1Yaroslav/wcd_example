from flask import Blueprint, render_template, redirect, url_for, request
from jwt import decode, ExpiredSignatureError, InvalidTokenError

from config import SECRET_KEY, VICTIM_USER_PASS

profile_bp = Blueprint("profile", __name__)


@profile_bp.route("/profile", defaults={"extra": ""}, methods=["GET"])
@profile_bp.route("/profile<path:extra>", methods=["GET"])
def profile(extra):
    token = request.cookies.get("jwt")
    if not token:
        return redirect(url_for("auth.login", error="Missing+JWT+Cookie"))

    try:
        payload = decode(token, SECRET_KEY, algorithms=["HS256"])

        context = {
            "user": payload["username"],
            "user_pass": VICTIM_USER_PASS,
            "secret_key": f"{SECRET_KEY}. Very secret key, please store it in secure place!!",
            "financial_data": "Your bank account: $12,977,212.97"
        }

        return render_template("profile.html", **context)

    except ExpiredSignatureError:
        return redirect(url_for("auth.login", error="Token expired"))

    except InvalidTokenError:
        return redirect(url_for("auth.login", error="Invalid token"))
