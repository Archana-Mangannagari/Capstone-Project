from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# -------------------------
# 1. Prepare dataset
# -------------------------
# For demo, we create a small dataset. You can replace this with 'fake_job_postings.csv'
data = {
    'text': [
        "We are hiring a software engineer",
        "Looking for a data scientist",
        "Congratulations! You won a lottery, send money",
        "Get rich quick scheme, work from home",
        "Join our secret team to transfer funds online",
        "Remote data entry job, earn $4000/week",
        "Become a secret shopper, deposit $100 to start"
    ],
    'fraudulent': [0, 0, 1, 1, 1, 1, 1]  # 0=Real, 1=Fake
}
df = pd.read_csv("../Data Folder/fake_job_postings.csv")

# -------------------------
# 2. Train-test split
# -------------------------
X = df['text']
y = df['fraudulent']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -------------------------
# 3. Vectorize text
# -------------------------
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# -------------------------
# 4. Train model
# -------------------------
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# -------------------------
# Flask routes
# -------------------------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    jobdesc = request.form['jobdesc']
    X_input = vectorizer.transform([jobdesc])
    prediction = model.predict(X_input)[0]
    result = "Fake Job Posting" if prediction == 1 else "Real Job Posting"
    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)