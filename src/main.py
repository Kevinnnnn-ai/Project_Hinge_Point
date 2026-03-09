import streamlit as st
import uuid # for workspace IDs
import workspace # workspace.py

# ============================
# primary app functionality
# ============================

def get_pages() -> dict:
    pages = {
        'Navigation': [
            st.Page('home.py', title='Home', default=True),
            st.Page('how_to_use.py', title='How To Use'),
            st.Page('what_is_effect_size.py', title='What Is Effect Size'),
            st.Page('dashboard.py', title='Dashboard'),
            st.Page('about.py', title='About'),
            st.Page('terms_of_service.py', title='Terms of Service'),
        ],
        'Workspaces': [],
    }

    for workspace_id, workspace_data in st.session_state.workspaces.items():
        workspace_name = workspace_data['name']
        pages['Workspaces'].append(
            st.Page(
                workspace.make_workspace_page(workspace_id),
                # def make_workspace_page(workspace_id: str) -> callable:
                #   def workspace_page():
                #   ...
                #   return workspace_page
                #
                # all workspaces refer to the workspace_page() callable
                # thus, workspaces need custom URLs to prevent overlap
                title=workspace_name,
                url_path=f'workspace_{workspace_id}',
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
        'dataset': None,
    }

    st.success(f'Created {name}')

def sidebar_funtionality() -> None:
    with st.sidebar:
        if st.button('Create New Workspace'):
            get_new_workspace()

# ============================
# execution logic
# ============================

if __name__ == '__main__':
    get_workspaces()
    sidebar_funtionality()
    
    pages = get_pages()
    navigation = st.navigation(pages=pages, position='sidebar', expanded=True)
    navigation.run()