# +-------------------------------------------------------------------------+
# | file is currently archived and not used in the app.                     |
# | login systems are hard to implement and maintain, and may not be worth  |
# | it for the app's intended use case.                                     |
# +-------------------------------------------------------------------------+

import streamlit as st
import streamlit_authenticator as stauth
import yaml 
from yaml.loader import SafeLoader

with open('./.streamlit/config.yaml') as config_file:
    config = yaml.load(config_file, Loader=SafeLoader,)

authenticator = stauth.Authenticate( # autheticator must correspond to ./streamlit/config.yaml
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
)

def Login_Page() -> None:
    try:
        authenticator.login(location='main',) # creates a streamlit-authenticator login widget
    except Exception as e: # in case login system failure
        st.error(e)

    if st.session_state.get('authentication_status'): # successful login
        authenticator.logout(location='sidebar',) # creates a streamlit-authenticator logout widget in the sidebar
    elif st.session_state.get('authentication_status') is False: # unsuccessful login
        st.error('Username or password is incorrect or does not exist.')
    elif st.session_state.get('authentication_status') is None: # unattempted login
        st.warning('Please enter your username and password.')

def Settings_Page() -> None:
    authenticator.logout(location='main',) # creates a streamlit-authenticator logout widget in the sidebar
    st.rerun()

def Main() -> None:
    authentication_status = st.session_state.get('authentication_status')
    if authentication_status: # access to full app if authenticated
        pages = (
            st.Page('home.py', title='Home', default=True,),
            st.Page('dashboard.py', title='Dashboard',),
            st.Page('profile.py', title='Profile',),
            st.Page('about.py', title='About',),
            st.Page(Settings_Page, title='Settings',),
        )
    else:
        pages = (
            st.Page('home.py', title='Home', default=True,),
            st.Page('about.py', title='About',),
            st.Page(Login_Page, title='Login',),
        )

    navigation = st.navigation(pages, position='sidebar', expanded=True,)
    navigation.run()

if __name__ == '__main__':
    Main()