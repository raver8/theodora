
import streamlit as st
 
# Set the title of the Streamlit app
st.title('COMING SOON: THEODORA, THE AI-POWERED RISK MANAGEMENT PLATFORM')

import streamlit as st
import os
from PIL import Image


# Specify the image file
image_path = 'THEODORA_SYM.jpg'

# Open and display the image file
image = Image.open(image_path)
st.image(image, caption='Specified Image', use_column_width=True)
