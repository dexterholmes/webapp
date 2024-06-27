import streamlit as st

# Add custom CSS to hide and disable the GitHub icon
st.markdown(
    """
    <style>
    /* Hide the GitHub icon */
    div[data-testid="stActionButtonIcon"] {
        display: none;
    }

    /* Disable clicks on the parent container of the GitHub icon */
    div[data-testid="stDecoration"] {
        pointer-events: none;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Your Streamlit app code goes here
st.title("My Streamlit App")
st.write("Welcome to my app!")

# Rest of your app logic...


