from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def initial():
  return(render_template("index.html"))

@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
  if request.method=="POST":
    response = request.form.get("entryBox")
    return(f"response:{response}")
  return("response not processed")
  

app.run('0.0.0.0', 8080)