import pickle
from preprocess import preprocess_text

def load_model(path):
    with open(path, 'rb') as f:
        model, vectorizer = pickle.load(f)
    return model, vectorizer

def predict_sentiment(text, model, vectorizer):
    text = preprocess_text(text)
    vec = vectorizer.transform([text])
    prediction = model.predict(vec)[0]
    return 'Positive' if prediction == 1 else 'Negative'
