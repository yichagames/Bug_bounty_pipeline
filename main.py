from utils import script_exec, log
import traceback
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/<action>/<value>")
def api(action, value):
    log.log(f"ts is zaa action: {action}, and hte valu: {value}")
    return "<h1>HMMM APIIIII</h1>"