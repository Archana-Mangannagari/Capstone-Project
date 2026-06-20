from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# -------------------------
# Load pre-trained model and vectorizer
# (These were trained with oversampling + all text columns + bigrams)
# -------------------------
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# -------------------------
# Flask routes
# -------------------------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    jobdesc = request.form['jobdesc']

    # Vectorize and predict
    X_input = vectorizer.transform([jobdesc])
    prediction = model.predict(X_input)[0]
    proba = model.predict_proba(X_input)[0]

    # Get confidence percentage
    if prediction == 1:
        result = "⚠️ Fake Job Posting"
        confidence = round(proba[1] * 100, 2)
    else:
        result = "✅ Real Job Posting"
        confidence = round(proba[0] * 100, 2)

    return render_template('index.html',
                           prediction_text=result,
                           confidence=confidence)

if __name__ == '__main__':
    app.run(debug=True)