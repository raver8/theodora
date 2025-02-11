import streamlit as st
import os
from PIL import Image

# Set the title with center justification using HTML and Markdown
st.markdown("<h1 style='text-align: center;'>COMING SOON:<br>THEODORA, THE AI-POWERED RISK MANAGEMENT PLATFORM</h1>", unsafe_allow_html=True)


# Specify the image file
image_path = 'THEODORA_SYM.jpg'

# Check if the image file exists
if os.path.exists(image_path):
    # Open and display the image file
    image = Image.open(image_path)
    st.image(image, caption='Specified Image', use_column_width=True)    
else:
    st.error('Error: Image file not found.')
