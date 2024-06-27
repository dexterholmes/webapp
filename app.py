import streamlit as st

# Add custom CSS to hide and disable the GitHub icon
st.markdown(
    """
    <style>
    /* Hide the GitHub icon */
    div[data-testid="stActionButtonIcon"] {
        display: none;
    }

    /* Disable pointer events on the entire footer */
    footer {
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


