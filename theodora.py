
import streamlit as st
 
st.title('My First Streamlit App')
import streamlit as st
import os
from PIL import Image

# Set the title of the Streamlit app
st.title("Image Gallery")

# Specify the folder containing the images
image_folder = 'images/'

# Get a list of all image files in the folder
image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]

# Display the images
for image_file in image_files:
    # Open and display the image
    image = Image.open(os.path.join(image_folder, image_file))
    st.image(image, caption=image_file, use_column_width=True)
