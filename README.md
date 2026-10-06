# 🛡️ Spam Detector — SMS & Email Spam Classification

An end-to-end machine learning application that classifies SMS and email messages as **HAM** or **SPAM**.

The project combines text classification, feature engineering, model evaluation, a Django REST API, a React frontend, and a Streamlit deployment.

## 🚀 Live Demo

**Streamlit App:**  
https://safal-spam-detector.streamlit.app/

**GitHub Repository:**  
https://github.com/SaFal252/Spam-Detector

---

## 📌 Project Overview

The goal of this project is to build a machine learning system capable of detecting unwanted spam messages from both SMS and email data.

The final model was trained using a combined dataset containing:

- SMS spam/ham messages
- Enron email spam/ham messages

The model uses **TF-IDF text features combined with engineered numerical features** and Logistic Regression for classification.

---

## 📊 Model Performance

The final model was evaluated on a stratified test set.

| Metric | Score |
|---|---:|
| Accuracy | **97.43%** |
| Precision | **97.29%** |
| Recall | **96.68%** |
| F1-Score | **96.98%** |

### Confusion Matrix

```text
[[4004   82]
 [ 101 2940]]
```

The model correctly classified the majority of both HAM and SPAM messages while maintaining a strong balance between precision and recall.

---

## 🧠 Machine Learning Approach

### 1. Data Preparation

Two datasets were combined:

- SMS Spam Collection dataset
- Enron Spam Dataset

The data was cleaned, duplicates were removed, and labels were converted into binary values:

```text
HAM  → 0
SPAM → 1
```

The final combined dataset contained approximately **35,632 messages**.

### 2. Text Preprocessing

Messages were cleaned by:

- Converting text to lowercase
- Replacing URLs
- Replacing numbers
- Removing unnecessary characters
- Normalizing whitespace

### 3. Feature Engineering

In addition to TF-IDF text features, the model uses:

- Character count
- Word count
- Digit count
- Uppercase ratio
- Exclamation mark count
- Currency symbol count
- URL presence
- Long-number presence

### 4. Text Vectorization

The project uses:

```text
TfidfVectorizer
```

with:

```text
ngram_range=(1, 2)
```

This allows the model to learn from both individual words and two-word combinations.

### 5. Classification

The final classifier is:

```text
Logistic Regression
```

The complete preprocessing and model pipeline is saved using:

```text
joblib
```

---

## 🏗️ Project Architecture

```text
                    ┌─────────────────────┐
                    │   User Message      │
                    └──────────┬──────────┘
                               │
                ┌──────────────┴──────────────┐
                │                             │
        Streamlit App                 React Frontend
                │                             │
                │                         Django REST API
                │                             │
                └──────────────┬──────────────┘
                               │
                        ML Pipeline
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
             TF-IDF                  Numerical Features
                 │                           │
                 └─────────────┬─────────────┘
                               │
                    Logistic Regression
                               │
                         HAM / SPAM
```

---

## 🛠️ Technologies Used

### Machine Learning

- Python
- Pandas
- NumPy
- Scikit-learn
- TF-IDF
- Logistic Regression
- Joblib

### Backend

- Django
- Django REST Framework
- django-cors-headers

### Frontend

- React
- Vite
- JavaScript
- CSS

### Deployment

- Streamlit Community Cloud
- GitHub

---

## 📂 Project Structure

```text
Email-Spam-Detection/
│
├── backend/
│   ├── predictor/
│   │   ├── views.py
│   │   └── urls.py
│   │
│   ├── spam_api/
│   │   ├── settings.py
│   │   └── urls.py
│   │
│   ├── manage.py
│   └── spam_detector.pkl
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   ├── package.json
│   └── vite.config.js
│
├── streamlit_app.py
├── spam_detector.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/SaFal252/Spam-Detector.git
cd Spam-Detector
```

### 2. Create and activate a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run streamlit_app.py
```

The application will open in your browser.

---

## 🔌 Django REST API

The project also includes a Django REST API.

Start the backend:

```bash
cd backend
python manage.py runserver
```

Prediction endpoint:

```text
POST /api/predict/
```

Example request:

```json
{
    "text": "Congratulations! You have won a free prize. Click here now!"
}
```

Example response:

```json
{
    "prediction": "SPAM",
    "spam_probability": 0.8879
}
```

---

## 🎨 React Frontend

The React frontend communicates with the Django REST API.

Run the frontend:

```bash
cd frontend
npm install
npm run dev
```

The frontend allows users to enter a message and receive:

- HAM/SPAM prediction
- Spam probability

---

## 🌐 Deployment

The Streamlit version of this project is deployed using **Streamlit Community Cloud**.

### Live Application

https://safal-spam-detector.streamlit.app/

The deployed application loads the trained `spam_detector.pkl` model and performs predictions directly.

---

## 📚 What I Learned

Through this project, I practiced:

- Text preprocessing
- TF-IDF vectorization
- N-gram features
- Feature engineering
- Binary classification
- Logistic Regression
- Precision, Recall and F1-score
- Confusion Matrix
- Model pipelines
- Hyperparameter tuning
- Model serialization with Joblib
- Building a Django REST API
- Connecting React with a backend API
- Deploying an ML application with Streamlit
- Git and GitHub project management

---

## 🔮 Future Improvements

Possible future improvements include:

- Testing additional NLP models
- Trying Naive Bayes and Linear SVM
- Improving false-positive/false-negative handling
- Adding probability threshold controls
- Adding email-specific preprocessing
- Adding more real-world spam datasets
- Containerizing the application with Docker

---

## 👨‍💻 Author

**Safal Shrestha**

BSc CSIT — Prime College

Interested in:

- Artificial Intelligence
- Machine Learning
- Data Science
- Python
- Backend Development

---

⭐ If you find this project useful, feel free to explore the repository and try the live demo.