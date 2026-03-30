import streamlit as st
from model import predict_reminder

st.title("AI Smart Health Reminder System")

st.write("Enter your daily routine details:")

study = st.slider("Study Hours", 1, 12)
water = st.selectbox("Water Intake Level", ["low","medium","high"])
sleep = st.slider("Sleep Time", 6, 12)
break_time = st.slider("Break Interval (minutes)", 15, 120)

if st.button("Check Routine"):

    result = predict_reminder(study, water, sleep, break_time)

    if result == 1:
        st.error("Reminder Needed! Improve your routine.")
    else:
        st.success("Your routine looks healthy!")
