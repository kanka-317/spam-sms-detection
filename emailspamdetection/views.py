from django.shortcuts import render
import os
import pickle

# Get base project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define model and vectorizer paths
model_path = os.path.join(BASE_DIR, 'spam_detection_model.pkl')
vectorizer_path = os.path.join(BASE_DIR, 'tfidf_vectorizer.pkl')

# Load model and vectorizer once when server starts
try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    with open(vectorizer_path, 'rb') as f:
        vectorizer = pickle.load(f)
except FileNotFoundError:
    model = None
    vectorizer = None

# Home page with prediction
def home(request):
    if request.method == 'POST' and model and vectorizer:
        email_text = request.POST.get('email_text')
        X_input = vectorizer.transform([email_text])
        result = model.predict(X_input)
        prediction = "SPAM" if result[0] == 1 else "HAM"
        return render(request, 'index.html', {'result': prediction, 'email': email_text})
    return render(request, 'index.html')

# About page
def about(request):
    return render(request, 'about.html')

# Contact page
def contact(request):
    return render(request, 'contact.html')
