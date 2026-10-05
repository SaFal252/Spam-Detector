1. Loaded the SMS Spam dataset
   - spam.csv
   - HAM = normal message
   - SPAM = unwanted/promotional message
2. Cleaned the dataset
   - Removed duplicates
   - Removed missing values
   - Converted labels:
     - HAM → 0
     - SPAM → 1
3. Text preprocessing
   - Lowercasing
   - URL handling
   - Number handling
   - Removed unnecessary characters
   - Preserved useful symbols such as !, ?, $, £, €
4. Feature Engineering
   We created:
   - Character count
   - Word count
   - Digit count
   - Uppercase ratio
   - Exclamation count
   - Currency count
   - URL detection
   - Long-number detection
5. TF-IDF
   - Converted text into numerical features.
   - Used unigrams + bigrams.
6. Train/Test Split
   - 80% training
   - 20% testing
   - Used stratification.
7. Logistic Regression
   - Used Logistic Regression as the main classifier.
   - Learned why Logistic Regression works well for binary text classification.
8. Naive Bayes comparison
   - Compared it with Logistic Regression.
   - Logistic Regression performed better for our setup.
9. Hyperparameter tuning
   - Used GridSearchCV
   - Tested different C values.
10. Threshold tuning
    - Tested different probability thresholds.
    - Learned the trade-off between precision and recall.
11. Pipeline
    - Combined preprocessing + model into one ML pipeline.
12. ColumnTransformer
    - Combined:
      - TF-IDF text features
      - numerical engineered features
13. Model evaluation
    - Accuracy
    - Precision
    - Recall
    - F1-score
    - Confusion matrix
14. Model interpretation
    - Examined Logistic Regression coefficients.
    - Learned which words/features pushed predictions toward SPAM or HAM.
15. Manual testing
    - Tested completely new messages.
    - Discovered that good test-set accuracy doesn't guarantee perfect real-world generalization.
16. Joblib
- Learned how to save the trained pipeline as a .pkl model for later use.
Most important thing you learned
The biggest lesson from this project wasn't actually spam detection.
You learned the complete traditional ML workflow:
Raw Data
   ↓
Cleaning
   ↓
Feature Engineering
   ↓
Train/Test Split
   ↓
Preprocessing
   ↓
Model Training
   ↓
Evaluation
   ↓
Tuning
   ↓
Testing on New Data
   ↓
Save Model
