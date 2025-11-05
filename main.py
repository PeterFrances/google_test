import streamlit as st

st.write("Debugging st.user:")
st.write(st.user)
st.write("Type:", type(st.user))
st.write("Dir:", dir(st.user))

# Try to access available attributes
try:
    st.write("Has email?", hasattr(st.user, 'email'))
except Exception as e:
    st.write("Error checking email:", e)

if st.button("Log in with Google"):
    st.login('google')

if st.button("Log out"):
    st.logout()
# import streamlit as st
# if st.button('press'):
#     st.logout()
# if not st.user.is_logged_in:
#     if st.button("Log in"):
#         st.login('google')
# else:
#     if st.button("Log out"):
#         st.logout()
#     st.write(f"Hello, {st.user.name}!")
# st.write(st.user)
# st.write(f"Hello, {st.user.name}!")
