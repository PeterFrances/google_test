import streamlit as st

import streamlit as st

# Define allowed emails
allowed_emails = ['p.romany@cleolaboratorie.com', 'email2@example.com', 'email3@gmail.com']

# Check if user is logged in
if not (hasattr(st.user, 'is_logged_in') and st.user.is_logged_in):
    st.login('google')  # Using named provider
    st.stop()

# User is logged in - now check if email is authorized
if hasattr(st.user, 'is_logged_in') and st.user.is_logged_in:
    user_email = st.user.email  # Get the logged-in user's email
    
    if user_email not in allowed_emails:
        # Email NOT in allowed list - show access denied
        st.error("🚫 Access Denied")
        st.warning(f"Your email **{user_email}** is not authorized to access this application.")
        st.info("Please contact the administrator if you believe this is an error.")
        
        # Show logout button for unauthorized users
        with st.sidebar:
            if st.button("🚪 Log out", type="primary", use_container_width=True):
                st.logout()
        
        st.stop()  # CRITICAL - Stop here, don't show any app content
    
    # Email IS in allowed list - show logout button in sidebar
    with st.sidebar:
        if st.button("🚪 Log out", type="primary", use_container_width=True):
            st.logout()

st.write('hello to my world ')
st.write('hello to my world ')
# ============================================================================
# If code reaches here, user is LOGGED IN and AUTHORIZED
# Your full app code continues below...
# ============================================================================

# if not (hasattr(st.user, 'is_logged_in') and st.user.is_logged_in):
#     st.login('google')  # Using named provider

# if hasattr(st.user, 'is_logged_in') and st.user.is_logged_in:
#     with st.sidebar:
#         if st.button("🚪 Log out"):
#             st.logout()

# # Check if user is logged in
# if hasattr(st.user, 'is_logged_in') and st.user.is_logged_in:        
#     with st.sidebar:
#         if st.button("Log out"):
#             st.logout()    
# else:    
#         st.login('google')  # Using named provider



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
        

