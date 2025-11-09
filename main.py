import streamlit as st

# Check if user is logged in
if hasattr(st.user, 'is_logged_in') and st.user.is_logged_in:        
    if st.button("Log out"):
        st.logout()    
else:    
        st.login('google')  # Using named provider




# import streamlit as st

# # Check if user is logged in
# if hasattr(st.user, 'is_logged_in') and st.user.is_logged_in:
#     st.write(f"Hello, {st.user.name}!")
#     st.write("Your email:", st.user.email)
    
#     if st.button("Log out"):
#         st.logout()
    
#     # Display all user info
#     with st.expander("See full user details"):
#         st.write(st.user.to_dict())
# else:
#     st.write("Please log in to continue")
#     if st.button("Log in with Google"):
#         st.login('google')  # Using named provider
        

