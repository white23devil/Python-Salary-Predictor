#Salary Predictor App - Code by Abhivandit Sharma!

#Step1 : Installing all the necessary libraries including pandas , streamlit mnumpy etc
import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np


data = pd.read_csv("Data//Salary_Data.csv")
x = np.array(data['Years of Experience']).reshape(-1,1)
lr = LinearRegression()
lr.fit(x,np.array(data['Salary']))


st.title("Salary Predictor App")

nav = st.sidebar.radio("Navigation",["Home","Prediction","Contribute"])

# Step 2: Creating Home Area
if nav =="Home":
    st.image("Data//salary.png" , width=300)
if st.checkbox("Show Table"):
    st.table(data)

graph = st.selectbox("What kind of graph?" , ["Non-interative", "Interative"])

val = st.slider("Filter data using years",0,35)
data = data.loc[data["Years of Experience"]>=val]
if graph == "Non-interative":
    plt.figure(figsize=(10,5))
    plt.scatter(data["Years of Experience"],data["Salary"])
    plt.ylim(0)
    plt.xlabel("Year of Experience")
    plt.ylabel("Salary")
    plt.tight_layout()
    st.pyplot()

if graph =="Interative":
    layout= go.Layout(
        xaxis = dict(range=[0,32]),
        yaxis = dict(range=[0,2200000])
    )

    fig = go.Figure(data=go.Scatter(x=data["Years of Experience"],y = data["Salary"],mode='markers'),layout=layout)
    st.plotly_chart(fig)

#Step2: Creating Navigation Area
if nav == "Prediction":
    st.header("Knowing your salary")
    val = st.number_input("Enter Your Experience",0.00,32.00,step=0.25)
    val = np.array(val).reshape(1,-1)
    pred = lr.predict(val)[0]

    if st.button("Predict"):
        st.success(f"Your Predicted Salary is : {round(pred)} ")

#Step3: Creating Contribute Area 
if nav == "Contribute":
    st.header("Primary Data Contribuion")
    ex = st.number_input("Enter Your Experience for Work",0.00,20.00)
    sal = st.number_input("Enter Your Salary for Your Work",0.00,8000000.00,step= 1000.00)

    if st.button("Submit"):
        to_add ={"Years of Experience":ex,"Salary":sal}
        to_add = pd.DataFrame(to_add,index=[0])
        to_add.to_csv("Data//Salary_Data.csv",mode = 'a' ,header= False,index=False)
        st.success("Data Submitted Successfully")


#   --------------------------Finally Did It!-------------------------------------#