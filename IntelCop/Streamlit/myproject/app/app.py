import streamlit as st

# Check if the user is authenticated
if 'authentication_status' in st.session_state and st.session_state['authentication_status']:
    st.title('Home Page')
    st.write(f"Welcome to the home page, {st.session_state['name']}!")
    # Add your home page content here
else:
    st.warning('Please log in to access this page.')
    
