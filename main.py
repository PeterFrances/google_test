import streamlit as st

# Get the user's email (only works in Streamlit Cloud with invited viewers)
user_info = st.context.cookies
st.write(user_info)

user_email = st.context.headers.get("Cf-Access-Authenticated-User-Email", "")
st.write(user_email)
# For newer Streamlit versions (1.28+):
try:
    user_email = st.experimental_user.email
except:
    user_email = ""
st.write(st.experimental_user.email)

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
