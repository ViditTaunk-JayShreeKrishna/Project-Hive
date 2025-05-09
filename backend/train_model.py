import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression  # Example model
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, 'project_dataset.csv')
MODEL_PATH = os.path.join(BASE_DIR, 'project_suggestion_model.pkl')

# Load dataset
df = pd.read_csv(CSV_PATH)

# Combine relevant columns
df['combined_text'] = df['skills'] + ' ' + df['interests'] + ' ' + df['difficulty']

# Vectorize
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(df['combined_text'])

# Create dummy labels (adjust this based on your dataset)
y = df['project_title']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model and vectorizer together
joblib.dump((tfidf, model), MODEL_PATH)

print("Model and vectorizer saved at:", MODEL_PATH)
