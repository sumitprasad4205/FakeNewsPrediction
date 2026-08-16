# 📰 Fake News Prediction

A machine learning and NLP project that predicts whether a news article is **Real or Fake** using **TF-IDF Vectorization** and classification algorithms.

## 📊 Model Performance

| Model                    |  Accuracy |
| ------------------------ | --------: |
| Logistic Regression      | **98.5%** |
| Random Forest Classifier | **99.1%** |

**Random Forest** achieved the highest accuracy of 99.1%, while **Logistic Regression** was selected for the Flask deployment due to its strong performance and efficiency.

## 🛠️ Tech Stack

* **Python**
* **Pandas, NumPy**
* **Scikit-learn**
* **TF-IDF Vectorization**
* **Logistic Regression & Random Forest**
* **Flask**
* **HTML & CSS**

## 🌐 Flask Deployment

The trained **Logistic Regression model** is deployed using Flask. Users can enter news article text through a web interface and receive a **Real/Fake** prediction.

## 📁 Project Structure

```text
FakeNewsPrediction/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── app.py
├── main.ipynb
├── news.pkl
└── README.md
```

## ✨ Features

* Fake news classification using NLP.
* TF-IDF text vectorization.
* Multiple model comparison.
* **98.5% accuracy with Logistic Regression.**
* Flask-based web application.
* Real-time news prediction.

## 🚀 Conclusion

This project demonstrates an end-to-end machine learning workflow, from **text preprocessing and model training to Flask deployment**, for detecting fake news articles.

