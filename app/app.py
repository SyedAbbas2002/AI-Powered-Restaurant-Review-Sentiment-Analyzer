from flask import Flask, render_template, request
from utils import load_model, predict_sentiment
import os

app = Flask(__name__)

# Load model and vectorizer once
model, vectorizer = load_model(os.path.join(os.path.dirname(__file__), '../sentiment_model.pkl'))

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = ''
    if request.method == 'POST':
        review = request.form['review']
        sentiment = predict_sentiment(review, model, vectorizer)
    return render_template('index.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)
