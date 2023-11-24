import streamlit as st
from PIL import Image

# Set the page title and favicon
st.set_page_config(page_title="legal documentation", page_icon="")

# Title and description
st.title("Welcome to  AI powered legal documentation assisstance")
st.write("Upload an Document to get a clear summary")

# Sidebar for user information
st.sidebar.header("User Information")
with st.sidebar.expander("User Information"):
    username = st.sidebar.text_input("Username", key="username")
    password = st.sidebar.text_input("Password", type="password", key="password")

if st.sidebar.button("Login"):
    if username == "user" and password == "password":  # Replace with actual user authentication logic
        st.sidebar.success(f"Logged in as {username}")
    else:
        st.sidebar.error("Invalid credentials. Please try again.")

if st.sidebar.button("Create Account"):
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    if st.button("Create"):
            st.success("Account created successfully. You can now log in.")


# Upload image
uploaded_image = st.file_uploader("Upload a document", type=["pdf", "doc", "pptx"])

if uploaded_image is not None:
    # Display the uploaded image
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    # Placeholder for plant diagnosis logic (replace with your actual diagnosis logic)
    diagnosis = "This is an invalid Doc."

    # Display diagnosis result
    st.subheader("Diagnosis")
    st.write(diagnosis)

    # Placeholder for care instructions (replace with actual care instructions)
    care_instructions = "Water the plant once a week and keep it in indirect sunlight."

    # Display care instructions
    st.subheader("Care Instructions")
    st.write(care_instructions)

# About section
st.subheader("About Legal Documentation")
st.write(
    "This is a web app helps individuals, bussinesses or organizations with the preparation, drafting and management of legal documents"
)

# Disclaimer
st.subheader("Disclaimer")
st.write(
    "This app converts legal documentation into a summary"
)

# Contact information
st.subheader("Contact Us")
st.write("If you have any questions or feedback, please email us at legaldocumentation@example.com")