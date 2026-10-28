# Credit Card Fraud Detection System 🛡️

An end-to-end Machine Learning project that detects potentially fraudulent credit card transactions using Logistic Regression and Random Forest, with an interactive Streamlit web application.

## 🚀 Live Demo
https://credit-card-fraud-detection-m8juyefcryogelevfvqxrm.streamlit.app/

## 🎯 Project Objectives
- Analyze transaction data and identify fraudulent transactions.
- Train and compare two Machine Learning classification models.
- Handle imbalanced data using class weighting.
- Evaluate performance using Precision, Recall, F1-score, and PR-AUC.
- Deploy an interactive web application using Streamlit.

## 🛠️ Technologies Used
- Python
- Pandas and NumPy
- Scikit-learn
- Joblib
- Streamlit
- Git and GitHub

## 📊 Dataset
The dataset contains 10,000 transactions with 10 columns.

- Genuine transactions: 9,849 (98.49%)
- Fraudulent transactions: 151 (1.51%)

Features include transaction amount, transaction hour, merchant category, foreign transaction status, location mismatch, device trust score, transaction velocity, and cardholder age.

The dataset source has not been independently verified.

## 🤖 Models Used
1. Logistic Regression
2. Random Forest Classifier

## 📈 Model Results

| Metric | Logistic Regression | Random Forest |
|---|---:|---:|
| Accuracy | 95.80% | 99.30% |
| Precision | 25.89% | 100.00% |
| Recall | 96.67% | 53.33% |
| F1-score | 40.85% | 69.57% |
| PR-AUC | 0.7364 | 1.0000 |

Results are from one stratified train-test split. The unusually high Random Forest PR-AUC requires further validation and does not guarantee performance on unseen real-world data.

## ⚙️ Project Workflow
1. Data exploration and preprocessing
2. Feature selection
3. Training and testing split
4. Model training
5. Performance evaluation
6. Model comparison
7. Interactive web application development
8. Deployment using Streamlit Community Cloud

## 💻 Run Locally

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd credit-card-fraud-detection
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

## 🔮 Future Improvements
- Hyperparameter tuning and cross-validation
- Classification threshold optimization
- Feature importance and explainability
- Testing with a verified real-world fraud dataset
- Improved visualizations and model monitoring

## ⚠️ Disclaimer
This project is for educational purposes only. Predictions may be incorrect and must not be used as the sole basis for real financial decisions.

## 👩‍💻 Author
B.Tech Artificial Intelligence and Data Science Student

GitHub: Add your GitHub profile URL here.
