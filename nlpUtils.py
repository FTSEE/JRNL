from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from transformers import pipeline
import re


# text (str) -> res (dict['label','score'])
def classifyPN(text):
  classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)
  res = classifier(text)
  emotion = (res[0][0])['label']
  confidence = (res[0][0])['score']
  return emotion, confidence

def splittingField(text):
  sentences = re.split(r'[.!?;&]', text)
  return sentences

def weightedAvg(sentences):
  pass


#testcase
if __name__ == "__main__":
    # huggingface classifyPN test
    text = "I think im getting worse"
    emotion, confidence = classifyPN(text)
    print(f'emotion:{emotion}, confidence:{confidence}')
    


