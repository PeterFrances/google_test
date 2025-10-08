import streamlit as st
import pandas as pd

st.set_page_config(layout='wide', initial_sidebar_state="collapsed")
st.write('hello')

def login_screen():
    st.header("This app is private.")
    st.subheader("Please log in.")
    if not st.user.is_logged_in:
        st.write(st.user)
    # st.button("Log in with Google", on_click=st.login('google'))
# if not st.user.is_logged_in:
login_screen()
# else:
#     st.user
#     st.header(f"Welcome, {st.user.name}!")
#     st.button("Log out", on_click=st.logout)
