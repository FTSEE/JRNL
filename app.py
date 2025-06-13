from flask import Flask, render_template, request
from nlpUtils import classifyPN

app = Flask(__name__)

@app.route('/')
def initial():
  return(render_template("landing.html"))

@app.route('/journal', methods=['POST'])
def journal():
  return(render_template("index.html"))

@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
  if request.method=="POST":
    response = request.form.get("entryBox")
    emotion, confidence = classifyPN(response)
    return(render_template("results.html", response=response, mood=emotion, confidence=confidence))
  return("response not processed")

app.run('0.0.0.0', 8080)