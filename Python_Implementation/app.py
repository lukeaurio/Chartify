from flask import Flask
import spotify_service as s
app = Flask(__name__)

@app.route("/")
def root_route():
    return "Hello Wurld!"

