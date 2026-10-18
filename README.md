
# Cynbit AI/ML Engineer Intern Assessment

## Project: Customer Inquiry Classification

This project demonstrates how machine learning can classify customer inquiries into categories and help route them to the appropriate team.

## Live Demo

https://cynbit-ai-classifier.streamlit.app/

## GitHub Repository

https://github.com/Rishikeshvats/Cynbit-AI-Assessment

## Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF
- Logistic Regression
- Streamlit
- Joblib
- Jupyter Notebook

## How It Works

1. The user enters a customer inquiry.
2. TF-IDF converts the text into numerical features.
3. Logistic Regression predicts the inquiry category.
4. The Streamlit application displays the prediction.

## Run Locally

Install the required libraries:

```bash
pip install -r requirements.txt
```

Start the application:

```bash
python -m streamlit run app.py
```

Open http://localhost:8501 in your browser.

## Project Files

- `app.py` — Streamlit application
- `cynbit_model.pkl` — trained classification model
- `cynbit_vectorizer.pkl` — TF-IDF vectorizer
- `requirements.txt` — required Python libraries
- `Cynbit_AI_ML_Assessment.ipynb` — training and evaluation notebook
- `AI_Opportunity_Report.docx` — business opportunity analysis
- `Technical_Approach_Report.docx` — technical design and execution plan

## Limitations

The current prototype uses a small synthetic dataset.
Its evaluation results should not be treated as evidence of
production performance. A larger, representative, labeled
dataset is needed for reliable evaluation.
