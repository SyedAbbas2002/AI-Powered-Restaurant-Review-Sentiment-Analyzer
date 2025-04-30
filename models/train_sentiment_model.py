import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load your actual dataset
df = pd.read_csv('dataset.csv')

# Optional: drop Neutral if doing only binary classification
df = df[df['Sentiment'] != 'Neutral']

# Map labels: Positive = 1, Negative = 0
df['Sentiment'] = df['Sentiment'].map({'Positive': 1, 'Negative': 0})

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(df['Review Text'], df['Sentiment'], test_size=0.2, random_state=42)

# Vectorize review text
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Train model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Save model and vectorizer
with open('sentiment_model.pkl', 'wb') as f:
    pickle.dump((model, vectorizer), f)

print("Updated model trained and saved as sentiment_model.pkl")
