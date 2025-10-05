# 📦 Amazon Delivery Time Prediction

A machine learning project that predicts **e-commerce delivery times** based on factors like distance, traffic, weather, and order details.  
It includes **data preprocessing, regression model comparison using MLflow, and a Streamlit web app** for real-time predictions.

---

## 🚀 Project Overview
The goal of this project is to accurately predict **delivery time (in minutes)** for online orders.  
Timely delivery is critical for improving customer satisfaction in e-commerce.  

We experimented with multiple regression models and deployed the best-performing one (`XGBoost Regressor`) as a **Streamlit app**.

---

## 🗂️ Project Structure
```
amazon-delivery-time-prediction/
├── Amazon_Delivery_Time_Prediction.ipynb       # Main Jupyter notebook
├── streamlit_app.py                            # Streamlit app
├── xgb_delivery_time.pkl                       # Saved model
├── requirements.txt                            # Dependencies
└── README.md                                   # Project documentation

````

---

## 📊 Key Features
- Comprehensive **EDA** and preprocessing
- Regression models: Linear Regression, Random Forest, Gradient Boosting, XGBoost
- **Model tracking and comparison with MLflow**
- Deployment-ready **Streamlit web app**
- User-friendly prediction interface

---

## ⚙️ Tech Stack
- **Python**, **Pandas**, **NumPy**
- **scikit-learn**, **XGBoost**
- **MLflow** for model tracking
- **Streamlit** for deployment

---

## 📈 Model Performance
| Model                     | RMSE   | MAE   | R²      |
|---------------------------|--------|-------|---------|
| Linear Regression         | 42.75  | 31.93 | 0.31    |
| Random Forest Regressor   | 37.37  | 26.30 | 0.48    |
| Gradient Boosting         | 36.16  | 25.36 | 0.51    |
| **XGBoost Regressor**     | **36.12** | **25.08** | **0.51** |

---

## 💻 Installation & Usage
1. Clone this repository:
```bash
git clone https://github.com/<your-username>/amazon-delivery-time-prediction.git
cd amazon-delivery-time-prediction
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
cd app
streamlit run streamlit_app.py
```

4. (Optional) Launch MLflow UI to explore model runs:

```bash
mlflow ui
```

Access at: `http://127.0.0.1:5000`

---

## 📊 Example Prediction

The web app allows users to enter:

* Distance (km)
* Traffic condition (Low / Medium / Jam / High)
* Weather condition (Sunny / Rainy / Fog / etc.)
* Order size, preparation time, etc.

It then predicts the **expected delivery time in minutes**.

---

## 📌 Problem Statement

This project aims to predict delivery times for e-commerce orders based on factors such as product size, distance, traffic conditions, and shipping method.
The final application enables users to input relevant details and receive estimated delivery times via a simple web interface.

---

## 📦 Future Enhancements

* Incorporate **real-time traffic and weather APIs**
* Experiment with **deep learning models**
* Deploy on **cloud platforms** like AWS/GCP for scalability

---

## 🤝 Contributing

Feel free to fork this repo, open issues, or submit pull requests for improvements!

---

## 👨‍💻 Author

Developed with ❤️ by **Vignesha S**
