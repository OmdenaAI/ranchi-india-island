import pandas as pd
import numpy as np
import streamlit as st
import os

file_path = 'https://github.com/OmdenaAI/ranchi-india-island/blob/main/src/tasks/task5-visualizationdeployment/Streamlit_presentation/landsat_images_ids.csv'

df = pd.read_csv(file_path)

st.header('Data Collection')
st.markdown(
'''
Landasat  Level 2 Surface Reflectence Data was collected using Google Earth Engine

Below is a list of image IDs
'''
)

st.write(df)