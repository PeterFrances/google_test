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
        st.warning(f"Your email **{user_email}** is not authorized to access multistore portal.")
        st.info("Please contact the administrator if you believe this is an error.")
        
        # Show logout button for unauthorized users
        with st.sidebar:
            if st.button("🚪 Log out", type="primary", use_container_width=True):
                st.logout()
        st.write('hi')
        st.stop()  # CRITICAL - Stop here, don't show any app content
        st.write('hi')
    
    # Email IS in allowed list - show logout button in sidebar
    with st.sidebar:
        if st.button("🚪 Log out", type="primary", use_container_width=True):
            st.logout()

st.write('hello to my world ')
st.write('hello to my world ')
