import streamlit as st
import uuid
from workspace import make_workspace_page

def get_pages() -> dict:
    pages = {
        'The Project': [
            st.Page('home.py', title='Home', default=True, icon=':material/home:'),
            st.Page('dashboard.py', title='Dashboard', icon=':material/dashboard:'),
            st.Page('about.py', title='About', icon=':material/error:'),
        ],
        'Using The Project': [
            st.Page('how_to_use.py', title='How To Use', icon=':material/table:'),
            st.Page('what_is_effect_size.py', title='What Is Effect Size', icon=':material/insert_chart:'),
            st.Page('terms_of_service.py', title='Terms of Service', icon=':material/article:'),
        ],
        'Your Workspaces': [],
    }

    for workspace_id, workspace_data in st.session_state.workspaces.items():
        workspace_name = workspace_data['name']
        pages['Your Workspaces'].append(
            st.Page(
                make_workspace_page(workspace_id),
                title=workspace_name,
                url_path=f'workspace_{workspace_id}', # because all workspaces reference workspace_page()
                icon=':material/widgets:'
            )
        )
        
    return pages

def get_workspaces() -> None:
    if 'workspaces' not in st.session_state: # possible if user has no workspace history
        st.session_state.workspaces = {}

def get_new_workspace() -> None:
    id = str(uuid.uuid4()) # effectively infinite workspaces
    name = f'Workspace {len(st.session_state.workspaces) + 1}'
    st.session_state.workspaces[id] = {
        'name': name,
        'description': '',
        'dataframe': None,
        'dataframe_statistics': {
            'sample_size': None, 'mean_diff': None, 'pooled_std': None, 'cohens_d': None,
            'hinge_point': None, 'is_above_hinge': None, 'students_improved': None, 'students_unchanged': None,
            'students_regressed': None,
        },
        'pre_score_statistics': {
            'pre_min': None, 'pre_max': None, 'pre_range': None, 'pre_mean': None,
            'pre_q1': None, 'pre_q3': None, 'pre_iqr': None, 'pre_std': None,
        },
        'post_score_statistics': {
            'post_min': None, 'post_max': None, 'post_range': None, 'post_mean': None,
            'post_q1': None, 'post_q3': None, 'post_iqr': None, 'post_std': None,
        },
    }

def sidebar_funtionality() -> None:
    with st.sidebar:
        if st.button('Create Workspace', icon=':material/add_circle:'):
            get_new_workspace()

if __name__ == '__main__':
    get_workspaces()
    sidebar_funtionality()
    
    pages = get_pages()
    navigation = st.navigation(pages=pages, position='sidebar', expanded=True)
    navigation.run()