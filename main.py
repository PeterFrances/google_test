import streamlit as st


if not st.user.is_logged_in:
    st.header("This app is private.")
    st.subheader("Please log in.")
    st.button("Log in with Google", on_click=st.login)
else:
    st.header(f"Welcome, {st.user.name}!")
    st.button("Log out", on_click=st.logout)


# import streamlit as st
# import pandas as pd

# st.set_page_config(layout='wide', initial_sidebar_state="collapsed")

# def login_screen():
#     st.header("This app is private.")
#     st.subheader("Please log in.")
#     st.button("Log in with Google", on_click=st.login('google'))
# if not st.user.is_logged_in:
#     login_screen()
# else:
#     st.user
#     st.header(f"Welcome, {st.user.name}!")
#     st.button("Log out", on_click=st.logout)
