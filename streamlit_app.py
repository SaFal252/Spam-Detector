import re
import joblib
import pandas as pd
import streamlit as st


# -----------------------------
# Page configuration
# -----------------------------

st.set_page_config(
    page_title="Spam Detector",
    page_icon="🛡️",
    layout="centered"
)


# -----------------------------
# Load trained model
# -----------------------------

MODEL_PATH = "spam_detector.pkl"

model = joblib.load(MODEL_PATH)


# -----------------------------
# Same features used in training
# -----------------------------

NUM_COLS = [
    "char_len",
    "word_count",
    "digit_count",
    "upper_ratio",
    "exclaim",
    "currency",
    "has_url",
    "long_number",
]


# -----------------------------
# Same cleaning function
# -----------------------------

def clean_v2(t):
    t = t.lower()
    t = re.sub(r"http\S+|www\.\S+", " url ", t)
    t = re.sub(r"\d+", " num ", t)
    t = re.sub(r"[^a-z0-9$£€!?\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


# -----------------------------
# Create model features
# -----------------------------

def make_features(text):

    return pd.DataFrame({
        "clean": [clean_v2(text)],

        "char_len": [len(text)],

        "word_count": [len(text.split())],

        "digit_count": [
            len(re.findall(r"\d", text))
        ],

        "upper_ratio": [
            sum(c.isupper() for c in text) / max(len(text), 1)
        ],

        "exclaim": [
            text.count("!")
        ],

        "currency": [
            len(re.findall(r"[$£€]", text))
        ],

        "has_url": [
            int(bool(re.search(r"http|www\.", text, re.I)))
        ],

        "long_number": [
            int(bool(re.search(r"\d{7,}", text)))
        ],
    })


# -----------------------------
# UI
# -----------------------------

st.title("🛡️ Spam Detector")

st.write(
    "Detect whether an SMS or email message is HAM or SPAM "
    "using a machine learning model."
)

text = st.text_area(
    "Enter your message",
    placeholder="Paste an SMS or email message here...",
    height=200
)


# -----------------------------
# Prediction
# -----------------------------

if st.button("Check Message", type="primary"):

    if not text.strip():

        st.warning("Please enter a message first.")

    else:

        data = make_features(text)

        X = data[["clean"] + NUM_COLS]

        prediction = int(model.predict(X)[0])

        probability = float(
            model.predict_proba(X)[0][1]
        )

        if prediction == 1:

            st.error("🚨 SPAM")

        else:

            st.success("✅ HAM")

        st.metric(
            "Spam Probability",
            f"{probability * 100:.2f}%"
        )