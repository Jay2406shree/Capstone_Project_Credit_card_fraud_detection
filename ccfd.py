import streamlit as st
import pickle
import numpy as np
with open("rf.pkl","rb") as model_file:
    reloaded_model = pickle.load(model_file)


st.title("Credit Card Fraud Detection")
ip = st.text_input("Enter all the features","Type the features")

ip_split = ip.split(",")                    
submit = st.button("Submit")


if submit:
    features = np.asarray(ip_split,dtype=np.float64).reshape(1,-1)
    
    prediction = reloaded_model.predict(features)
    
    if prediction[0] == 0:
        st.write("Legitimate Transaction")
    else:
        st.write("Fradulent Transaction")
    
