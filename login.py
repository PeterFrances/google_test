import streamlit as st

# Check if user is logged in
if hasattr(st.user, 'is_logged_in') and st.user.is_logged_in:        
    if st.button("Log out"):
        st.logout()    
else:    
        st.login('google')  # Using named provider
