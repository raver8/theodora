import streamlit as st
import os
from PIL import Image

# Set the title of the Streamlit app
st.title('COMING SOON: /p
THEODORA, /p
THE AI-POWERED RISK MANAGEMENT PLATFORM')

# Specify the image file
image_path = 'THEODORA_SYM.jpg'

# Check if the image file exists
if os.path.exists(image_path):
    # Open and display the image file
    image = Image.open(image_path)
    
else:
    st.error('Error: Image file not found.')
