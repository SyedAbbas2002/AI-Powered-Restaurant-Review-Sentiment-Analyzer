import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Sample dataset (replace with your actual restaurant review dataset)
data = {
    'review': [
        "The food was great and the service was excellent",
        "Horrible experience, I will never come back",
        "Loved the ambiance and the food was tasty",
        "Very disappointing, food was cold and bland",
        "Absolutely fantastic service and delicious food",
        "The place was dirty and the food was awful"
    ],
    'sentiment': [1, 0, 1, 0, 1, 0]  # 1 = Positive, 0 = Negative
}

df = pd.DataFrame(data)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(df['review'], df['sentiment'], test_size=0.2, random_state=42)

# Text vectorization
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Train sentiment model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Save model and vectorizer as a single pickle file
with open('sentiment_model.pkl', 'wb') as f:
    pickle.dump((model, vectorizer), f)

print("Model saved successfully as sentiment_model.pkl")
