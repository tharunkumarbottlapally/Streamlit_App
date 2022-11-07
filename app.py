import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
from vega_datasets import data

#information
st.set_page_config(layout="wide")
st.title('HR Analytics')
with st.expander('About this app'):
  st.write('HR Analytics helps us with interpreting organizational data.\n It finds the people-related trends in the data and allows the HR Department to take the appropriate steps to keep the organization running smoothly and profitably')
  st.image('https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=870&q=80', width=400)

hr_data=pd.read_csv("HR-Employee-Attrition.csv")

st.write(hr_data)

st.sidebar.header("Pick two variables for your scatterplot")
x_val=st.sidebar.selectbox("Pick your x-axis",hr_data.select_dtypes(include=np.number).columns.tolist())
y_val=st.sidebar.selectbox("Pick your y-axis",hr_data.select_dtypes(include=np.number).columns.tolist())

scatter =alt.Chart(hr_data,title=f"Correlation between {x_val} and {y_val}").mark_point().encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(y_val,title=f"{y_val}"),
    tooltip=[x_val,y_val]
)

st.altair_chart(scatter,use_container_width=True)

corr=round(hr_data[x_val].corr(hr_data[y_val]),2)
st.write(f"The correlation between {x_val} and {y_val} is {corr}")

st.header("Companies Over Department")

barchart=alt.Chart(hr_data).mark_bar().encode(
    x='Age',
    y='sum(NumCompaniesWorked)',
    color='Department',
    tooltip=[x_val,y_val]
)
st.altair_chart(barchart,use_container_width=True)

st.header("Attrition vs Department")
attrition=alt.Chart(hr_data).mark_bar().encode(
    x='Department',
    y='Attrition',
    color='Attrition',
    tooltip=['Department','Attrition']
)
st.altair_chart(attrition,use_container_width=True)

st.header("Hourly pay vs Different Education Fields")
edu=alt.Chart(hr_data).mark_bar().encode(
    x='EducationField',
    y='HourlyRate',
    color='EducationField',
    tooltip=['EducationField','HourlyRate','Department']
)
st.altair_chart(edu,use_container_width=True)

st.header("Martial Status vs Last Promotion")
Martial=alt.Chart(hr_data).mark_bar().encode(
    x='MaritalStatus',
    y='YearsSinceLastPromotion',
    color='JobRole',
    tooltip=['JobRole','YearsSinceLastPromotion','MaritalStatus']
)
st.altair_chart(Martial,use_container_width=True)

st.header("Monthly Income vs Number of Companies Worked")
areachart=alt.Chart(hr_data).mark_area(opacity=0.3).encode(
    x="MonthlyIncome",
    y=alt.Y("NumCompaniesWorked", stack=None),
    color="JobRole",tooltip=['MonthlyIncome','NumCompaniesWorked','JobSatisfaction']
)
st.altair_chart(areachart,use_container_width=True)
