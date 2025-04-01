from flask import Flask, render_template

from blueprints import auth_bp, profile_bp
from config import SECRET_KEY, DEBUG

app = Flask(__name__)

app.register_blueprint(auth_bp)
app.register_blueprint(profile_bp)

app.config["SECRET_KEY"] = SECRET_KEY


@app.route('/', methods=('GET',))
def get_home_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, DEBUG=DEBUG)
