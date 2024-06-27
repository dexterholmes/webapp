import streamlit as st

# Add custom CSS to hide the GitHub icon
st.markdown(
    """
    <style>
    .css-1lsmgbg.e1fqkh3o3 {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Your Streamlit app code goes here
st.title("aMy Streamlit App")
st.write("Welcome to my app!")

# Rest of your app logic...

