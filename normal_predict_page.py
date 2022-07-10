import streamlit as st
import pickle
import numpy as np


def normal_model_function():
  st.subheader("normal model function is called successfully")

def normal_page():
  st.title("Career Dendrogram")
  st.write("### Fill out the form to predict your career")

  st.write("#### 1. Personal Information")
  name = st.text_input('Name', '')
  email = st.text_input('Email', '')
  dob = st.text_input('DOB', '')
  country = st.text_input('Country', '')

  select = st.selectbox(
     'Employee or Student',
     ('None', 'Employee', 'Student'))

  if select == "None":
    st.write("Please skip this section and move to the next section")
  elif select == "Employee":
    st.write("#### 2. Performance at the workplace")
    timeliness = st.slider('Timeliness', 0, 10, 2)
    attention = st.slider('attention to details', 0, 10, 4)
    creative = st.slider('Creativity', 0, 10, 1)
    consistence = st.slider('Consistency', 0, 10, 5)
    salary = st.number_input('Salary')
    # st.write("1.timeliness, 2.attention to details, 3.Creativity, 4.Consistency, 5.Salary")
  else:
    st.write("#### 2. Educational Information")
    option1 = st.selectbox(
    'Highest Degree',
    ('highschool', 'intermediate', 'diploma', 'ug', 'pg', 'phd'))
    option2 = st.selectbox(
     'certifications',
     ('app development', 'distro making', 'full stack', 'hadoop', 'information security', 'machine learning', 'python', 'r programming', 'shell programming'))
    option3 = st.selectbox(
     'workshops',
     ('cloud computing', 'data science', 'database security', 'game development', 'hacking', 'system designing', 'testing', 'web technologies'))
    option4 = st.selectbox(
    'Branch',
    ('cs', 'electrical', 'mechanical', 'civil'))
    csSkills = st.slider('Computer Skills', 0, 10, 5)
    communicationalSkills = st.slider('Communicational Skills', 0, 10, 3)
    # st.write("1.Highest Degree, 2.Certification, 3.Workshops, 4.Branch, 5.Computer Skills, 6.Communicational Skills")
    

  st.write("#### 3. Additional Information")
  hobbies = st.text_input('Hobbies', '')
  interest = st.text_input('Interests', '')

  ok = st.button("Predict career path")
  if ok:
    normal_model_function()