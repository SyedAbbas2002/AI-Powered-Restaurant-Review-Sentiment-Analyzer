# 🍽️ DineSentiment: AI-Powered Restaurant Review Sentiment Analyzer

DineSentiment is a machine learning–driven web application that performs sentiment analysis on restaurant reviews. It leverages Natural Language Processing (NLP) techniques to classify reviews as **positive**, **neutral**, or **negative**, helping restaurant owners and food platforms gain actionable insights from customer feedback.

---

## 🔍 Features

- ✅ Analyze real-world restaurant reviews
- ✅ Predict sentiment in real-time using trained ML models
- ✅ Preprocess text (cleaning, tokenizing, lemmatizing)
- ✅ Data visualizations: Word clouds, sentiment charts
- ✅ Easy-to-use web interface (built with Streamlit)
- ✅ Modular, clean, and reusable codebase

---

## 🧠 Tech Stack

| Component        | Tools Used                                  |
|------------------|----------------------------------------------|
| **Language**     | Python                                       |
| **Libraries**    | `nltk`, `scikit-learn`, `pandas`, `Streamlit`|
| **Model**        | Logistic Regression (or replaceable)         |
| **Frontend**     | Streamlit UI                                 |
| **Visualization**| Matplotlib, Seaborn, WordCloud               |

---

## 📁 Project Structure

```
DineSentiment/
├── data/
│   └── restaurant_reviews.csv
├── models/
│   └── train_sentiment_model.py
├── app/
│   ├── app.py
│   ├── utils.py
│   └── preprocess.py
├── notebooks/
│   └── Sentiment_Analysis_EDA.ipynb
├── requirements.txt
├── .gitignore
└── README.md

```

---

## 📊 Visual Output (Sample)

| Sentiment | Example Review Text                            |
|-----------|------------------------------------------------|
| Positive  | "The food was absolutely delicious!"           |
| Negative  | "Terrible service. I waited for 40 minutes."   |
| Neutral   | "Visited yesterday, had chicken biryani."      |

---

## 💡 How It Works

1. Load and preprocess restaurant reviews
2. Vectorize text using TF-IDF
3. Train classification model (Logistic Regression, SVM, etc.)
4. Predict sentiment from user input or dataset
5. Display prediction and charts in the UI

---

## ⚙️ Installation & Setup

```bash
# Clone the repo
git clone https://github.com/SyedAbbas2002/DineSentiment.git
cd DineSentiment

# Install dependencies
pip install -r requirements.txt

# Run the app (for Streamlit)
streamlit run app/app.py
```

---

## 📈 Future Improvements

- Aspect-Based Sentiment Analysis (e.g., food vs service)
- Multilingual review support
- REST API integration (Flask/FastAPI)
- Deploy on HuggingFace Spaces / Render

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to open a [pull request](https://github.com/SyedAbbas2002/DineSentiment/pulls).

---

## ✨ Acknowledgements

- [NLTK](https://www.nltk.org/)
- [Scikit-learn](https://scikit-learn.org/)
- [Streamlit](https://streamlit.io/)
- Datasets from Yelp, Kaggle, or scraped reviews

---

## 📬 Contact

**Developer:** Syed Abbas  
📧 Email: itsmesyedabbas@gmail.com  
🌐 GitHub: [@SyedAbbas2002](https://github.com/SyedAbbas2002)
