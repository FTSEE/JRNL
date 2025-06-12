from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier

def sentimentScore(text):
  sample = TextBlob(text)
  score = sample.sentiment.polarity
  return score

def classifyPN(score):
  if score < -0.2:
      mood = 'negative'
  elif -0.2 <= score <= 0.2:
     mood = 'neutral'
  elif score > 0.2:
     mood = 'positive'
  return mood

#testcase
if __name__ == "__main__":
    score = sentimentScore("You're pretty alright dude")
    mood = classifyPN(score)
    print(f"SentScore={score}, feel={mood}")
