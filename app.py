import streamlit as st

# Add custom CSS and JavaScript to hide and disable the GitHub icon
st.markdown(
    """
    <style>
    div[data-testid="stActionButtonIcon"] {
        display: none;
        pointer-events: none;
    }
    </style>
    <script>
    document.addEventListener("DOMContentLoaded", function() {
        var githubIcon = document.querySelector('div[data-testid="stActionButtonIcon"]');
        if (githubIcon) {
            githubIcon.style.pointerEvents = 'none';
        }
    });
    </script>
    """,
    unsafe_allow_html=True,
)

# Your Streamlit app code goes here
st.title("My Streamlit App")
st.write("Welcome to my app!")

# Rest of your app logic...
