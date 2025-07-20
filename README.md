# 📱 Spam SMS Detection using Machine Learning

This project is a machine learning-based system to detect spam SMS messages. It classifies text messages as **spam** or **ham (not spam)** using natural language processing and traditional ML algorithms.

## 🔍 Features

- SMS preprocessing and cleaning
- Feature extraction using TF-IDF
- Model training using Multinomial Naive Bayes
- Accuracy, precision, recall & F1-score evaluation
- Simple web interface using Flask (or Streamlit)
- Deployable on platforms like PythonAnywhere or Heroku

## 🧠 Algorithms Used

- Multinomial Naive Bayes
- CountVectorizer / TF-IDF for vectorization
- Logistic Regression / SVM (optional extensions)

## 📁 Project Structure

spam-sms-detection/
├── static/ # CSS/images (optional)
├── templates/ # HTML templates
├── model/ # Trained ML model (pickle file)
├── spam_sms_detection.ipynb # Jupyter notebook with training pipeline
├── app.py # Flask/Streamlit app file
├── requirements.txt # List of dependencies
└── README.md # Project documentation
We use the **SMS Spam Collection Dataset** from UCI Machine Learning Repository.  
- 📁 Download:https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset
  

