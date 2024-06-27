import streamlit as st

# Add custom CSS to hide the GitHub icon
st.markdown(
    """
    <style>
    .st-emotion-cache-30do4w e3g6aar1 { 
        display: none; 
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Your Streamlit app code goes here
st.title("My Streamlit App")
st.write("Welcome to my app!")

# Rest of your app logic...
