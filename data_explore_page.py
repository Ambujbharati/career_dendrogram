import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def data_page():
  st.title("Explore the data used in this model")
  df = pd.read_csv("roo_data.csv")
  st.write(df.head(10))
