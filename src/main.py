import streamlit as st
import uuid # for workspace IDs

def dashboard() -> None:
    st.set_page_config(
        layout='centered',
        page_title='Dashboard - Project Hinge Point',
        page_icon='assets/placeholder_image.png',
    )

    st.title('Dashboard')

def get_pages() -> dict:
    pages = {
        'Navigation': [
            st.Page('home.py', title='Home', default=True),
            st.Page(dashboard, title='Dashboard'),
            st.Page('about.py', title='About'),
        ],
        'Workspaces': [],
    }

    for workspace_id, workspace_data in st.session_state.workspaces.items():
        workspace_name = workspace_data['name']
        pages['Workspaces'].append(
            st.Page(
                make_workspace_page(workspace_id), # all workspaces refer to the workspace_page() callable
                title=workspace_name,
                url_path=f'workspace_{workspace_id}', # thus, workspaces need cutsom URLs
            )
        )
    return pages

def get_workspaces() -> None:
    if 'workspaces' not in st.session_state:
        st.session_state.workspaces = {}

def make_workspace_page(workspace_id: str) -> callable:
    def workspace_page(): # convert workspace_id to a callable that can be used as a page
        workspace = st.session_state.workspaces[workspace_id]
        
        st.markdown('### Score Distribution')

        '''
        histogram_baseline = st.slider(
            "Set Desired Score Baseline",
            min_value=0,
            max_value=100,
            value=50,
            step=1,
        )
        histogram = px.histogram(
            example_dataframe,
            x="score_after",
            nbins=10,
        )
        histogram.add_vline(
            x=baseline,
            line_dash="dash",
            annotation_text=f"Baseline = {baseline}",
            annotation_position="top"
        )
        st.plotly_chart(fig, use_container_width=True)
        '''

    return workspace_page

def workspace_sidebar() -> None:
    with st.sidebar:
        if st.button('Create New Workspace'):
            workspace_id = str(uuid.uuid4())
            workspace_name = f'Workspace {len(st.session_state.workspaces) + 1}'

            st.session_state.workspaces[workspace_id] = {
                'name': workspace_name,
                'data': {},
            }
            st.success(f'Created {workspace_name}')

if __name__ == '__main__':
    get_workspaces()
    workspace_sidebar()
    
    pages = get_pages()
    navigation = st.navigation(pages, position='sidebar', expanded=True)
    navigation.run()