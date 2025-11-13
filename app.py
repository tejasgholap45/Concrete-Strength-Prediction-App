import streamlit as st
import numpy as np
import pickle

# ---------------------------------------------------
# 🔹 Load Trained XGBoost Model
# ---------------------------------------------------
model = pickle.load(open("model.pkl", "rb"))

# ---------------------------------------------------
# 🔹 Streamlit Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Concrete Strength Prediction | Tejas Gholap",
    page_icon="🏗️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------
# 🔹 Header Section
# ---------------------------------------------------
st.markdown("""
    <div style="text-align:center; padding:10px;">
        <h1 style="color:#FF4B4B;">🏗️ Concrete Strength Prediction App</h1>
        <h4 style="color:grey;">Predict the compressive strength (MPa) of concrete using XGBoost</h4>
    </div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# 🔹 Sidebar (Profile Info)
# ---------------------------------------------------
with st.sidebar:
    st.image("https://avatars.githubusercontent.com/u/216306511?v=4", width=150)
    st.markdown("## 👨‍💻 Tejas Gholap")
    st.markdown("[🌐 LinkedIn](https://www.linkedin.com/in/tejas-gholap-bb3417300/)")
    st.markdown("[💻 GitHub](https://github.com/tejasgholap45)")
    st.markdown("📧 tejasgholap45@gmail.com")
    st.markdown("---")
    st.info("This app uses a trained XGBoost model to predict concrete compressive strength.")

# ---------------------------------------------------
# 🔹 Input Form
# ---------------------------------------------------
st.subheader("🧱 Enter Concrete Mix Details")

col1, col2, col3 = st.columns(3)

with col1:
    cement = st.number_input("Cement (kg/m³)", min_value=0.0, value=200.0)
    slag = st.number_input("Blast Furnace Slag (kg/m³)", min_value=0.0, value=100.0)
    flyash = st.number_input("Fly Ash (kg/m³)", min_value=0.0, value=120.0)

with col2:
    water = st.number_input("Water (kg/m³)", min_value=0.0, value=150.0)
    superplasticizer = st.number_input("Superplasticizer (kg/m³)", min_value=0.0, value=2.6)
    coarseagg = st.number_input("Coarse Aggregate (kg/m³)", min_value=0.0, value=850.0)

with col3:
    fineagg = st.number_input("Fine Aggregate (kg/m³)", min_value=0.0, value=925.0)
    age = st.number_input("Age (days)", min_value=1.0, value=28.0)

# Combine all features
features = np.array([[cement, slag, flyash, water, superplasticizer, coarseagg, fineagg, age]])

# ---------------------------------------------------
# 🔹 Predict Button
# ---------------------------------------------------
st.markdown("<br>", unsafe_allow_html=True)

if st.button("🚀 Predict Strength", use_container_width=True):
    prediction = model.predict(features)
    st.success(f"💪 Predicted Compressive Strength: **{prediction[0]:.2f} MPa**")
    st.balloons()

# ---------------------------------------------------
# 🔹 Footer
# ---------------------------------------------------
st.markdown("""
    <hr>
    <div style='text-align: center; color: grey;'>
        <p>Developed by <b>Tejas Gholap</b> |
        <a href='https://github.com/tejasgholap45'>GitHub</a> |
        <a href='https://www.linkedin.com/in/tejas-gholap-bb3417300/'>LinkedIn</a></p>
    </div>
""", unsafe_allow_html=True)
