import re
import joblib
import pandas as pd

from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Load trained model
MODEL_PATH = settings.BASE_DIR / "spam_detector.pkl"
model = joblib.load(MODEL_PATH)


# Same numerical features used during training
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


# Same cleaning function used during training
def clean_v2(t):
    t = t.lower()
    t = re.sub(r"http\S+|www\.\S+", " url ", t)
    t = re.sub(r"\d+", " num ", t)
    t = re.sub(r"[^a-z0-9$£€!?\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


# Create the 9 features required by the model
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


@api_view(["POST"])
def predict_spam(request):

    text = request.data.get("text", "").strip()

    if not text:
        return Response(
            {"error": "Text is required."},
            status=400
        )

    # Create features
    data = make_features(text)

    # Predict
    prediction = int(
        model.predict(
            data[["clean"] + NUM_COLS]
        )[0]
    )

    result = "SPAM" if prediction == 1 else "HAM"

    # Get probability
    spam_probability = float(
        model.predict_proba(
            data[["clean"] + NUM_COLS]
        )[0][1]
    )

    return Response({
        "prediction": result,
        "spam_probability": spam_probability
    })