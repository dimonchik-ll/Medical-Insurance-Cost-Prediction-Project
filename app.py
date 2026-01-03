import streamlit as st
import requests

st.title("Medical Insurance")

with st.form("Input your data"):
    age = st.number_input("Your age", step=1)
    sex = st.selectbox("Your sex", ["male", "female"])
    bmi = st.number_input("Your BMI", step=0.1)
    children = st.number_input("Number of children", value=0)
    smoker = st.selectbox("Do you smoke", ["no", "yes"])
    region = st.selectbox("Your region", ["northeast", "northwest", "southeast", "southwest"])
    submit = st.form_submit_button("Apply")

if submit:
    data = {
        "age": age, 
        "sex": sex, 
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region,
        }
    proxies = {"http": None, "https": None}
    response = requests.post("http://127.0.0.1:8000/charges", json=data, proxies=proxies)
    st.success(f"Final Medical Bills: {response.json()["charges"]:.2f} USD")