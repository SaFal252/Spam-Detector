import { useState } from "react";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const predictSpam = async () => {
    if (!text.trim()) return;

    setLoading(true);
    setResult(null);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/predict/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ text }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Something went wrong");
      }

      setResult(data);
    } catch (error) {
      setResult({
        error: error.message,
      });
    } finally {
      setLoading(false);
    }
  };

  const clearMessage = () => {
    setText("");
    setResult(null);
  };

  const probability = result?.spam_probability
    ? (result.spam_probability * 100).toFixed(2)
    : "0.00";

  return (
    <div className="app">
      <div className="container">

        <div className="header">
          <div className="icon">🛡️</div>

          <h1>Spam Detector</h1>

          <p>
            Detect whether an SMS or email message is{" "}
            <strong>HAM</strong> or <strong>SPAM</strong>.
          </p>
        </div>

        <div className="card">

          <label htmlFor="message">
            Enter your message
          </label>

          <textarea
            id="message"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Paste an SMS or email message here..."
            rows="9"
          />

          <div className="actions">
            <button
              className="predict-btn"
              onClick={predictSpam}
              disabled={loading || !text.trim()}
            >
              {loading ? "Analyzing..." : "Check Message"}
            </button>

            <button
              className="clear-btn"
              onClick={clearMessage}
              disabled={!text && !result}
            >
              Clear
            </button>
          </div>

          {result && !result.error && (
            <div
              className={`result ${
                result.prediction === "SPAM"
                  ? "spam"
                  : "ham"
              }`}
            >
              <div className="result-icon">
                {result.prediction === "SPAM" ? "⚠️" : "✓"}
              </div>

              <div>
                <p className="result-label">
                  Prediction
                </p>

                <h2>{result.prediction}</h2>

                <p className="probability">
                  Spam Probability:{" "}
                  <strong>{probability}%</strong>
                </p>
              </div>
            </div>
          )}

          {result?.error && (
            <div className="error">
              {result.error}
            </div>
          )}

        </div>

        <div className="footer">
          <p>
            Powered by Machine Learning •
            TF-IDF + Logistic Regression
          </p>
        </div>

      </div>
    </div>
  );
}

export default App;