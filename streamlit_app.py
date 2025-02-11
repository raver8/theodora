"""
# Import necessary libraries
import streamlit as st

# Set page title and favicon
st.set_page_config(page_title="My Personal Website", page_icon=":rocket:")

# Define the main content of the app
def main():
    st.title("Welcome to My Personal Website")
    st.write("This is a simple Streamlit app for my personal website.")
    st.write("Feel free to customize it with your own content!")

    # Add sections or components as needed
    st.header("yo soy aquel")
    st.write("I am a passionate developer and love creating cool things with code.")
    st.write("In my free time, I enjoy hiking, playing guitar, and exploring new technologies.")

    st.header("Projects")
    st.write("Here are some of my recent projects:")
    st.write("- Project 1: [Link to Project 1](https://github.com/myusername/project1%29)")
    st.write("- Project 2: [Link to Project 2](https://github.com/myusername/project1%29)")

    st.header("Contact")
    st.write("Feel free to reach out to me:")
    st.write("- Email: myemail@example.com")
    st.write("- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/myusername%29)")

# Run the app
if __name__ == "__main__":
    main()
    """
