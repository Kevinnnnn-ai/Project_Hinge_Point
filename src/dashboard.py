import streamlit as st
import pandas as pd

st.warning('THIS PAGE IS CURRENTLY UNDER DEVELOPMENT. YOU MAY ENCOUNTER ERRORS.')

# ============================
# page setup
# ============================

st.set_page_config(gi
    layout='centered',
    page_title='Dashboard - Project Hinge Point',
    page_icon='assets/project_hinge_point_logo.png',
)

def separator() -> None:
    st.markdown('---', unsafe_allow_html=True)

def header() -> None:
    st.markdown('# :red[Dash]board')

def combine_dataframes() -> list:
    dataframes = []
    for id, data in st.session_state.workspaces.items():
        dataframe = st.session_state.workspaces[id]['dataset']
        if dataframe is not None:
            dataframes.append(dataframe)

    if dataframes:
        combined_dataframe = pd.concat(dataframes)
    else:
        combined_dataframe = []
        
    return combined_dataframe

# ============================
# page displays
# ============================

'''
def aggregate_calculations(combined_dataframe: pd.Dataframe) -> dict:

def aggregate_metrics_panel(datasets: list) -> None:
    with st.container(border=True):
        
def effect_size_visual_panel() -> None:
    with st.container(border=True):

def workspace_comparison_panel() -> None:
    with st.container(border=True):
'''

# ============================
# execution logic
# ============================

if __name__ == '__main__':
    header()
    separator()
    
    dataframes = combine_dataframes()
    aggregate_calculations(dataframes)