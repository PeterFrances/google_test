import streamlit as st
if st.button('press'):
    st.logout()
if not st.user.is_logged_in:
    if st.button("Log in"):
        st.login('google')
else:
    if st.button("Log out"):
        st.logout()
    st.write(f"Hello, {st.user.name}!")
