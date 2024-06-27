import streamlit as st

# Add custom CSS to hide the GitHub icon
st.markdown(
    """
    <style>
    .viewerBadge_container__1QSob { 
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
