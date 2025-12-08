from utils import script_exec, log
import traceback
from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/doc")
def doc():
    return ""

@app.route("/api/<action>/<value>")
def api(action, value):
    log.log(f"api_action: {action}, value: {value}")

    return redirect("/")