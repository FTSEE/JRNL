import torch
import re
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from transformers import pipeline, GPT2Tokenizer, GPT2LMHeadModel, AutoModelForSeq2SeqLM, AutoTokenizer

#gpt2 electric boogaloo
tokenizerGPT = GPT2Tokenizer.from_pretrained("gpt2")
modelGPT = GPT2LMHeadModel.from_pretrained("gpt2")

modelGPT.eval()

def generateReflectionGPT(prompt):
    inputs = tokenizerGPT.encode(prompt, return_tensors="pt")
    
    with torch.no_grad():
        outputs = modelGPT.generate(
            inputs,
            max_new_tokens=20,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            repetition_penalty=1.1,
            pad_token_id=tokenizerGPT.eos_token_id,
            top_k=50,
        )
    
    generated_text = tokenizerGPT.decode(outputs[0], skip_special_tokens=True)
    return generated_text.replace(prompt, "")

#blenderbot
tokenizerBB = AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
modelBB = AutoModelForSeq2SeqLM.from_pretrained("facebook/blenderbot-400M-distill")

modelBB.eval()

#BB chatbot 
def generateReflectionBB(text):
  inputs = tokenizerBB.encode(text, return_tensors='pt', padding=True, truncation=True)

  with torch.no_grad():
    outputs = modelBB.generate(
        inputs,
        max_length=100,
        num_return_sequences=1,
        temperature=0.7,  # controls creativity
        top_k=50,
        top_p=0.95,
        repetition_penalty=1.1,
        early_stopping=False,
        do_sample = True
    )
    
  generated_text = tokenizerBB.decode(outputs[0], skip_special_tokens=True)
  return generated_text

def promptCreator(text):
  text = (f"This is my journal entry for today: {text}. I really want to ask myself")
  return text

# text (str) -> res (dict['label','score'])
def classifyPN(text):
  classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=3)
  res = classifier(text)
  emotion = (res[0][0])['label']
  confidence = (res[0][0])['score']
  return emotion, confidence

def splittingField(text):
  sentences = re.split(r'[.!?;&]', text)
  return sentences

def weightedAvg(sentences):
  sentenceScores = {}
  sentenceScores["Total"] = 0
  for sentence in sentences:
    senEmotion, senConf = classifyPN(sentence)
    sentenceScores["Total"] += senConf
    if senEmotion in sentenceScores:
      sentenceScores[senEmotion] += senConf
    else:
      sentenceScores[senEmotion] = senConf
  return sentenceScores


#testcase
if __name__ == "__main__":
    text = "I saw my ex today, completely by accident—just two strangers on opposite sides of the street pretending not to notice. There was a sudden ache, not sharp like heartbreak, but dull and oddly nostalgic, like remembering a song you once loved but no longer play. Back at home, I stared at the half-folded laundry for twenty minutes, not tired, just suspended—like if I moved, something fragile might shatter. I laughed too hard at a meme someone sent me, and immediately felt guilty, like joy had to be rationed. There’s this weird tension inside me lately—restless, like I need to change everything, and terrified that I’ll ruin the good parts I already have. Mom called and I didn’t pick up, not because I didn’t want to talk, but because I wouldn’t know how to explain the fog in my head. Still, I made soup tonight and lit a candle, and for a few minutes, the world felt small and manageable. I don’t know if I’m getting better, or just getting used to this version of me—but maybe, for now, that’s enough."
    # huggingface classifyPN test
    """
    emotion, confidence = classifyPN(text)
    print(f'emotion:{emotion}, confidence:{confidence}')
    """
    # huggingFace Flan response testing
    prompt = promptCreator(text)
    response = generateReflectionGPT(prompt)
    print(response)

    #splitting field classification testing:
    """sentences = splittingField(text)
    scores = weightedAvg(sentences)
    print(scores)"""

    
    


