import streamlit as st

# Initialize session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login_page():
    st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .login-container {
        max-width: 400px;
        margin: 100px auto;
        padding: 40px;
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
    }
    
    .login-title {
        text-align: center;
        color: white;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 30px;
    }
    
    .stTextInput input {
        background: rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 10px;
        color: white;
        padding: 12px;
    }
    
    .stTextInput input::placeholder {
        color: rgba(255, 255, 255, 0.7);
    }
    
    .stButton button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="login-title">Welcome Back</h1>', unsafe_allow_html=True)
    
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    
    if st.button("Login"):
        if username == "admin" and password == "password":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Invalid credentials")
    
    st.markdown('</div>', unsafe_allow_html=True)

def main_page():
    st.markdown("""
    <style>
    .welcome-header {
        text-align: center;
        color: #667eea;
        font-size: 36px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<h1 class="welcome-header">Dashboard</h1>', unsafe_allow_html=True)
    st.write("You are logged in!")
    
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

# Main app logic
if not st.session_state.logged_in:
    login_page()
else:
    main_page()







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
        

