import streamlit as st
import os
from PIL import Image

# Set the title with center justification using HTML and Markdown
st.markdown("<h3 style='text-align: center;'>COMING SOON:</h3>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>THEODORA</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>THE AI-POWERED RISK MANAGEMENT PLATFORM</h2>", unsafe_allow_html=True)
# Specify the image file
image_path = 'THEODORA_SYM.jpg'

# Check if the image file exists
if os.path.exists(image_path):
    # Open and display the image file
    image = Image.open(image_path)
    st.image(image, caption='_', use_container_width=True)    
else:
    st.error('Error: Image file not found.')
