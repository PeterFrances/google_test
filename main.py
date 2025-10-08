import streamlit as st

st.set_page_config(layout='wide', initial_sidebar_state="collapsed")

# Try to access user info - if it fails, authentication isn't configured
try:
    # Check if user email exists (indicates logged in)
    if st.user.email:
        # User is logged in
        st.header(f"Welcome, {st.user.name}!")
        st.write(f"Email: {st.user.email}")
        
        # Your main app content here
        st.write("You're logged in!")
        
        if st.button("Log out"):
            st.logout()
    else:
        # Not logged in
        st.header("This app is private.")
        st.subheader("Please log in to continue.")
        if st.button("Log in with Google"):
            st.login('google')
            
except (AttributeError, KeyError):
    # Authentication not configured or user not logged in
    st.header("This app is private.")
    st.subheader("Please log in to continue.")
    
    if st.button("Log in with Google"):
        st.login('google')
