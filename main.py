import streamlit as st
st.user
if not st.user.is_logged_in:
    if st.button("Log in"):
        s=st.login()
else:
    if st.button("Log out"):
        st.logout()
    st.write(f"Hello, {st.user.name}!")
