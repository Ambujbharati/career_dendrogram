import streamlit as st
import pickle
import numpy as np


def cs_model_function():
  st.subheader("cs model function is called successfully")

def cs_page():
  st.title("Career Dendrogram")
  st.write("### Fill out the form to predict your career")

  st.write("#### 1. Personal Information")
  name = st.text_input('Name', '')
  email = st.text_input('Email', '')

  st.write("#### 2. Educational Information")
  os = st.number_input('Acedamic percentage in Operating Systems')
  algo = st.number_input('percentage in Algorithms')
  pc = st.number_input('Percentage in Programming Concepts ')
  se = st.number_input('Percentage in Software Engineering')
  cn = st.number_input('Percentage in Computer Networks')
  es = st.number_input('Percentage in Electronics Subjects')
  ca = st.number_input('Percentage in Computer Architecture')
  maths = st.number_input('Percentage in Mathematics')
  cs = st.number_input('Percentage in Communication skills')
  hackathon = st.number_input('hackathons')

  workinghours = st.slider('Hours working per day', 0, 12, 4)
  logic = st.slider('Logical quotient rating', 0, 10, 5)
  codingskills = st.slider('coding skills rating', 0, 10, 6)
  speakingskills = st.slider('public speaking points', 0, 10, 2)

  st.write("#### 3. Additional Information")

  option1 = st.selectbox(
     'can work long time before system?',
     ('no', 'yes'))
  option2 = st.selectbox(
     'self-learning capability?',
     ('no', 'yes'))
  option3 = st.selectbox(
     'Extra-courses did',
     ('no', 'yes'))
  option4 = st.selectbox(
     'certifications',
     ('app development', 'distro making', 'full stack', 'hadoop', 'information security', 'machine learning', 'python', 'r programming', 'shell programming'))
  option5 = st.selectbox(
     'workshops',
     ('cloud computing', 'data science', 'database security', 'game development', 'hacking', 'system designing', 'testing', 'web technologies'))

  option6 = st.selectbox(
     'talenttests taken? ',
     ('no', 'yes'))
  option7 = st.selectbox(
     'olympiads',
     ('no', 'yes'))
  option8 = st.selectbox(
     'reading and writing skills',
     ('excellent', 'medium', 'poor'))
  option9 = st.selectbox(
     'memory capability score',
     ('excellent', 'medium', 'poor'))
  option10 = st.selectbox(
     'Interested subjects',
     ('Computer Architecture', 'IOT', 'Management', 'Software Engineering', 'cloud computing', 'data engineering', 'hacking', 'networks', 'parallel computing', 'programming'))

  option11 = st.selectbox(
     'interested career area ',
     ('Business process analyst', 'cloud computing', 'developer', 'security', 'system developer', 'testing'))
  option12 = st.selectbox(
     'Job/Higher Studies?',
     ('higherstudies', 'job'))
  option13 = st.selectbox(
     'Type of company want to settle in?',
     ('BPA', 'Cloud Services', 'Finance', 'Product based', 'SAaS services', 'Sales and Marketing', 'Service Based', 'Testing and Maintainance Services', 'Web Services', 'product development'))
  option14 = st.selectbox(
     'Taken inputs from seniors or elders',
     ('no', 'yes'))
  option15 = st.selectbox(
     'interested in games',
     ('no', 'yes'))

  option16 = st.selectbox(
     'Interested Type of Books',
     ('Action and Adventure', 'Anthology', 'Art', 'Autobiographies', 'Biographies', 'Childrens', 'Comics', 'Cookbooks', 'Diaries', 'Dictionaries', 'Drama', 'Encyclopedias', 'Fantasy', 'Guide', 'Health', 'History', 'Horror', 'Journals', 'Math', 'Mystery', 'Poetry', 'Prayer books', 'Religion-Spirituality', 'Romance', 'Satire', 'Science', 'Science fiction', 'Self help', 'Series', 'Travel', 'Trilogy'))
  option17 = st.selectbox(
     'Salary Range Expected',
     ('Work', 'salary'))
  option18 = st.selectbox(
     'In a Realtionship?',
     ('no', 'yes'))
  option19 = st.selectbox(
     'Gentle or Tuff behaviour?',
     ('gentle', 'stubborn'))
  option20 = st.selectbox(
     'Management or Technical',
     ('Management', 'Technical'))

  option21 = st.selectbox(
     'Salary/work',
     ('salary', 'work'))
  option22 = st.selectbox(
     'hard/smart worker',
     ('hard worker', 'smart worker'))
  option23 = st.selectbox(
     'worked in teams ever?',
     ('no', 'yes'))
  option24 = st.selectbox(
     'Introvert',
     ('no', 'yes'))

  ok = st.button("Predict career path")
  if ok:
    cs_model_function()


Suggested_Job_Role = ['Applications Developer', 'Business Intelligence Analyst',
 'Business Systems Analyst', 'CRM Business Analyst',
 'CRM Technical Developer', 'Data Architect', 'Database Administrator',
 'Database Developer', 'Database Manager', 'Design & UX',
 'E-Commerce Analyst', 'Information Security Analyst',
 'Information Technology Auditor', 'Information Technology Manager',
 'Mobile Applications Developer', 'Network Engineer',
 'Network Security Administrator', 'Network Security Engineer',
 'Portal Administrator', 'Programmer Analyst', 'Project Manager',
 'Quality Assurance Associate', 'Software Developer', 'Software Engineer',
 'Software Quality Assurance (QA) / Testing', 'Software Systems Engineer',
 'Solutions Architect', 'Systems Analyst', 'Systems Security Administrator',
 'Technical Engineer', 'Technical Services/Help Desk/Tech Support',
 'Technical Support', 'UX Designer', 'Web Developer']