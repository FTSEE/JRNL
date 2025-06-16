from flask import Flask, render_template, request, jsonify
from nlpUtils import classifyPN, generateReflectionBB, promptCreator, splittingField, weightedAvg

app = Flask(__name__)

@app.route('/')
def initial():
  return(render_template("landing.j2"))

@app.route('/journal', methods=['POST'])
def journal():
  return(render_template("index.j2"))

@app.route('/confirm', methods=['POST'])
def confirm():
  response = request.form.get("entryBox")
  return (render_template("results.j2", response=response))
  
@app.route('/analyze', methods=['POST'])
def responseAnalyze():
  data = request.get_json()
  response = data.get("response", "") #Gets either the value from the response key being sent in the json body of the fetch, or returns an empty string

  emotion, confidence = classifyPN(response)
  prompt = promptCreator(response)
  reflection = generateReflectionBB(prompt)
  sentences = splittingField(response)
  emotionDict = weightedAvg(sentences)

  return jsonify({
    "mood": emotion, 
    "confidence": confidence, 
    "reflection": reflection, 
    "emotionDist": emotionDict
  })

if __name__ == "__main__":
  app.run('0.0.0.0', 8080, debug=True)