## 🧱 **Concrete Strength Prediction App**

This project is a **Machine Learning web application** that predicts the **compressive strength of concrete (in MPa)** based on its ingredient composition.
It uses the **XGBoost Regressor** model and is deployed as an interactive **Streamlit web app**.

👉 **Live Demo:**
🔗 [https://concrete-strength-prediction-app-tejasgholap.streamlit.app/](https://concrete-strength-prediction-app-tejasgholap.streamlit.app/)

---

## 🚀 **Project Overview**

The app allows users to input the following parameters of a concrete mix:

* Cement
* Blast Furnace Slag
* Fly Ash
* Water
* Superplasticizer
* Coarse Aggregate
* Fine Aggregate
* Age (in days)

Based on these inputs, the trained **XGBoost model** predicts the **compressive strength** of the concrete.

---

## ⚙️ **Tech Stack**

| Component | Technology Used                                  |
| --------- | ------------------------------------------------ |
| Frontend  | Streamlit                                        |
| Backend   | Python                                           |
| ML Model  | XGBoost Regressor                                |
| Dataset   | Yeh Concrete Data (Kaggle)                       |
| Libraries | NumPy, Pandas, Scikit-learn, Seaborn, Matplotlib |

---

## 📂 **Project Structure**

```
Concrete-Strength-Prediction-App/
│
├── app.py                # Streamlit app code
├── model.pkl             # Trained XGBoost model
├── requirements.txt      # Required dependencies
└── README.md             # Project documentation
```

---

## 🧠 **How to Run Locally**

1. **Clone this repository**

   ```bash
   git clone https://github.com/tejasgholap45/Concrete-Strength-Prediction-App.git
   cd Concrete-Strength-Prediction-App
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

4. Open your browser and go to `http://localhost:8501`

---

## 📈 **Model Details**

* Algorithm: **XGBoost Regressor**
* Evaluation Metrics: **Mean Squared Error (MSE)** and **R² Score**
* The model is trained using the **Concrete_Data_Yeh.csv** dataset from Kaggle.

---

## 👨‍💻 **Author**

**Tejas Gholap**
📍 Data Science & Machine Learning Enthusiast

* 🌐 [LinkedIn](https://www.linkedin.com/in/tejas-gholap-bb3417300/)
* 💻 [GitHub](https://github.com/tejasgholap45)
* ✉️ **[tejasgholap45@gmail.com](mailto:tejasgholap45@gmail.com)**

---

## ❤️ **Acknowledgements**

Special thanks to:

* [Kaggle - Yeh Concrete Dataset](https://www.kaggle.com/datasets/maajdl/yeh-concret-data)
* [Streamlit](https://streamlit.io/) for simplifying ML model deployment.

---

Would you like me to make this `README.md` even more **stylish with badges, emojis, and screenshots sections** (like “Model Accuracy”, “Liv badges)?
That makes it look premium on GitHub 🚀
