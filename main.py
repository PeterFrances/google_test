import streamlit as st

# Check if user is logged in by checking if email exists
if st.user.email:
    st.write(f"Hello, {st.user.name}!")
    if st.button("Log out"):
        st.logout()
    
    # Display user info
    st.write("User details:")
    st.write(st.user)
else:
    st.write("Please log in to continue")
    if st.button("Log in with Google"):
        st.login('google')

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
