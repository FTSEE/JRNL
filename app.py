from flask import Flask, render_template, request
from nlpUtils import sentimentScore, classifyPN

app = Flask(__name__)

@app.route('/')
def initial():
  return(render_template("index.html"))

@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
  if request.method=="POST":
    response = request.form.get("entryBox")
    # vauge classification of entry leaning.
    userScore = sentimentScore(response)
    userMood = classifyPN(userScore)
    return(f"response:{response}. The NLP processor has detected that the user Response is: {userMood}")
  return("response not processed")
  

app.run('0.0.0.0', 8080)