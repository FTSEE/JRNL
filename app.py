from flask import Flask, render_template, request
from nlpUtils import classifyPN, generateReflectionBB, promptCreator, splittingField, weightedAvg

app = Flask(__name__)

@app.route('/')
def initial():
  return(render_template("landing.j2"))

@app.route('/journal', methods=['POST'])
def journal():
  return(render_template("index.j2"))

@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
  if request.method=="POST":
    response = request.form.get("entryBox")
    emotion, confidence = classifyPN(response)
    prompt = promptCreator(response)
    reflection = generateReflectionBB(prompt)
    sentences = splittingField(response)
    emotionDict = weightedAvg(sentences)
    return(render_template(
      "results.j2", response=response, mood=emotion, confidence=confidence, reflection=reflection, emotionDist = emotionDict))
  return("response not processed")

if __name__ == "__main__":
  app.run('0.0.0.0', 8080, debug=True)