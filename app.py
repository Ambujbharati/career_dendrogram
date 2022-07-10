import streamlit as st
from cs_predict_page import cs_page
from normal_predict_page import normal_page
from data_explore_page import data_page

page = st.sidebar.selectbox("Select the predictor", ("For CS Students", "For Others", "Explore the data"))

if page == "For CS Students":
  cs_page()
elif page == "For Others":
  normal_page()
else:
  data_page()
