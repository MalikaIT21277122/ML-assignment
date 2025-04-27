# 🫀 Heart Disease Prediction Using Machine Learning

This project is a group assignment that applies supervised machine learning models to predict whether a person is at risk of heart disease based on clinical and demographic attributes.

## 📊 Objective

The goal is to compare multiple classification algorithms using a real-world medical dataset and deploy the best-performing model using a Flask backend and a React frontend.

---

## 📁 Dataset

- Source: [UCI Heart Disease Dataset](https://www.kaggle.com/datasets/redwankarimsony/heart-disease-data)
- Instances: 1025
- Features: Clinical and personal attributes (e.g., age, cholesterol, chest pain, etc.)
- Target: Presence (`1`) or absence (`0`) of heart disease

---

## 🤖 Models Used

Each group member implemented a separate supervised learning model:

| Member                 | Model                   |
|------------------------|-------------------------|
| Rovinya Wijerama       | Logistic Regression     |
| Bimsara Weerakoon      | Decision Tree Classifier|
| Malika Degaldoruwa     | Random Forest Classifier|
| Janith Withanagamage   | K-Nearest Neighbors     |

---

## ✅ Best Model: K-Nearest Neighbors (KNN)

- **Accuracy**: 85.5%
- **Precision**: 88%
- **Recall**: 78%
- **AUC**: 0.93

KNN was selected as the best-performing model due to its high accuracy and discriminative ability.

---

## 🧪 Technologies Used

- **Language**: Python (scikit-learn, pandas, matplotlib)
- **Backend**: Flask API (`app.py`) with saved model (`.pkl`)
- **Frontend**: React.js interface to input health details and show predictions
- **Deployment**: Flask + React (local)
- **Model Persistence**: joblib

---

## 🎥 Demo Video

- [Watch the Assignment Demo Video Here](https://www.youtube.com/watch?v=QvCnX3q6_IY&feature=youtu.be)

---

## 📄 License

This project is for educational purposes under [SLIIT's Machine Learning course (IT4060)].

---

## 👥 Contributors

- Rovinya Wijerama  
- Bimsara Weerakoon  
- Malika Degaldoruwa  
- Janith Withanagamage