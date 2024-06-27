import streamlit as st

# Add custom CSS to hide the GitHub icon
hide_github_icon = """
<style>
#GithubIcon {
    visibility: hidden;
}
</style>
"""
st.markdown(hide_github_icon, unsafe_allow_html=True)

# Your app code goes here

