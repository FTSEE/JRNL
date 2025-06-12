# JRNL

JRNL is a web-based journaling application built with Flask that helps users reflect on their thoughts through writing. It leverages natural language processing to extract sentiment and provide thoughtful feedback, turning everyday entries into moments of self-awareness.

# Features:
- Clean and simple journaling interface
- Real-time sentiment analysis using TextBlob
- Foundations for AI-generated reflective feedback
- Modular backend for easy NLP model integration

# Tech Stack:
- Frontend: HTML, CSS (custom styling)
- Backend: Python, Flask, Js
- NLP: TextBlob (OpenAI API integration in progress)
- Version Control: Git, GitHub

# Getting Started!

To run JRNL locally:
- git clone https://github.com/YOUR_USERNAME/jrnl.git
- cd jrnl
- python -m venv venv
# Windows
- venv\Scripts\activate
# macOS/Linux
- source venv/bin/activate

pip install -r requirements.txt
python app.py
Then open your browser and go to http://localhost:8080.

# Project Structure

JRNL/
- ├── app.py                  # Main Flask app
- ├── nlpUtils.py             # NLP utilities
- ├── templates/              # HTML templates (Jinja2)
- │   └── index.html
- ├── static/                 # CSS and assets
- ├── requirements.txt
- └── README.md

# Roadmap for Future:
- Core journaling flow
- Sentiment scoring with TextBlob
- Feedback generation with GPT (optional)
- OAuth-based user accounts
- Hosted deployment
- Feedback collection system

# License:
This project is licensed under the Apache 2.0 License.


