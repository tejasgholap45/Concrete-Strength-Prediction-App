# 🏗️ Concrete Strength Prediction App  

[![Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)  
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![XGBoost](https://img.shields.io/badge/Model-XGBoost-orange?logo=xgboost&logoColor=white)](https://xgboost.readthedocs.io/en/stable/)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Status](https://img.shields.io/badge/Deployed-Live-success?logo=streamlit)](https://concrete-strength-prediction-app-tejasgholap.streamlit.app/)

---

## 🔗 **Live Demo**
👉 [**Try the App Now on Streamlit Cloud 🚀**](https://concrete-strength-prediction-app-tejasgholap.streamlit.app/)

---

## 🧠 **Project Overview**

This interactive web application predicts the **compressive strength of concrete (in MPa)** using an advanced **XGBoost Regressor model**.  
Users can easily input concrete mix details, and the app instantly provides a strength prediction.

---

## ⚙️ **Tech Stack**

| Component | Technology Used |
|------------|-----------------|
| 💻 Frontend | Streamlit |
| 🧠 Machine Learning | XGBoost Regressor |
| 🐍 Programming Language | Python |
| 📊 Libraries | NumPy, Pandas, Scikit-learn, Seaborn, Matplotlib |
| 🧱 Dataset | Yeh Concrete Data (Kaggle) |

---

## 🧩 **Input Features**

| Feature | Description |
|----------|--------------|
| Cement | Cement content (kg/m³) |
| Slag | Blast furnace slag (kg/m³) |
| Fly Ash | Fly ash content (kg/m³) |
| Water | Water content (kg/m³) |
| Superplasticizer | Chemical admixture (kg/m³) |
| Coarse Aggregate | Coarse aggregate (kg/m³) |
| Fine Aggregate | Fine aggregate (kg/m³) |
| Age | Concrete age (days) |

---

## 🧱 **Model Performance**

| Metric | Value |
|---------|--------|
| Mean Squared Error (MSE) | ~22.45 |
| R² Score | ~0.89 |

> ⚡ The model provides accurate compressive strength predictions for a wide range of concrete mix proportions.

---

## 📂 **Project Structure**

Concrete-Strength-Prediction-App/
│
├── app.py # Streamlit web app
├── model.pkl # Trained XGBoost model
├── requirements.txt # Dependencies
└── README.md # Documentation

---

## 🧭 **Run Locally**
```
1️⃣ Clone the repository:
```bash
git clone https://github.com/tejasgholap45/Concrete-Strength-Prediction-App.git
cd Concrete-Strength-Prediction-App
```
2️⃣ Install the required libraries:
pip install -r requirements.txt
```
3️⃣ Run the app:
streamlit run app.py
```
---

## 👨‍💻 **Author**

**Tejas Gholap**
🎓 Data Science & Machine Learning Enthusiast

🌐 [LinkedIn](https://www.linkedin.com/in/tejas-gholap-bb3417300/)
💻 [GitHub](https://github.com/tejasgholap45)
✉️ [tejasgholap45@gmail.com](mailto:tejasgholap45@gmail.com)

---

## ❤️ **Acknowledgements**

* [Kaggle - Yeh Concrete Dataset](https://www.kaggle.com/datasets/maajdl/yeh-concret-data)
* [Streamlit](https://streamlit.io/) for enabling effortless ML app deployment
* [XGBoost](https://xgboost.readthedocs.io/) for its robust regression capabilities

---

## 🌟 **Screenshots (Optional)**

Add your app screenshots here after deployment 👇
Example:

```
📸 Home Page  
📊 Prediction Result  
```

---

### 🏁 **Result**

🚀 A fully functional and interactive **Concrete Strength Prediction Web App** built using **XGBoost + Streamlit**, showcasing the power of ML in civil engineering and materials science.
---
