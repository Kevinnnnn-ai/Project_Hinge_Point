import streamlit as st
import main # main.py

st.warning('THIS PAGE IS CURRENTLY UNDER DEVELOPMENT. YOU MAY ENCOUNTER ERRORS.')

st.set_page_config(
    layout='centered',
    page_title='How To Use - Project Hinge Point',
    page_icon='assets/project_hinge_point_logo.png',
)

def header() -> None:
    st.markdown(
        '''
        # How To Project Hinge Point
        From raw scores to actionable insight in three steps.
        ''',
        unsafe_allow_html=True,
    )

def workflow() -> None:
    st.markdown('## Workflow Overview', unsafe_allow_html=True)

    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        with st.container(border=True):
            st.markdown(
                '''
                #### :red[1.] Create a Workspace
                Each workspace holds one dataset — one pre/post assessment cycle.
                Create as many as you need from the sidebar or the buttons on this page.
                ''',
                unsafe_allow_html=True,
            )

    with col_2:
        with st.container(border=True):
            st.markdown(
                '''
                #### :red[2.] Upload Your Data
                Upload a `.csv`, `.xlsx`, or `.ods` file with your student scores.
                The first three columns must follow the required order (see below).
                ''',
                unsafe_allow_html=True,
            )

    with col_3:
        with st.container(border=True):
            st.markdown(
                '''
                #### :red[3.] Read Your Results
                The workspace instantly calculates descriptive statistics, Cohen's d,
                and renders interactive visualizations for your data.
                ''',
                unsafe_allow_html=True,
            )

def data_format_section() -> None:
    st.markdown('## :red[Data] Format Requirements', unsafe_allow_html=True)

    with st.container(border=True):
        col_1, col_2 = st.columns([3, 2], vertical_alignment='top')

        with col_1:
            st.markdown(
                '''
                #### Required Column Order

                Your file's **first three columns** must be structured as follows.
                Column names do not need to match exactly — only position matters.

                | Position | Content |
                |---|---|
                | Column 1 | Student identifier (name, ID, or placeholder) |
                | Column 2 | Pre-test score |
                | Column 3 | Post-test score |

                Additional columns beyond the third are ignored.
                ''',
                unsafe_allow_html=True,
            )

        with col_2:
            st.markdown(
                '''
                #### No Student Names?

                Student names are not required for any calculation.
                If your dataset has no name column, create a placeholder column in
                position 1 and fill it with any values (e.g., participant IDs or random strings).
                ''',
                unsafe_allow_html=True,
            )

    st.markdown(
        '''
        #### Accepted File Types
        `.csv` — Comma-Separated Values &nbsp;|&nbsp;
        `.xlsx` — Excel Workbook &nbsp;|&nbsp;
        `.ods` — OpenDocument Spreadsheet
        ''',
        unsafe_allow_html=True,
    )


def visualizations_section() -> None:
    st.markdown('## :red[Reading] the Charts', unsafe_allow_html=True)

    with st.container(border=True):
        col_1, col_2 = st.columns(2)

        with col_1:
            st.markdown(
                '''
                #### Comparison Histogram
                Overlays pre-test (white) and post-test (red) score distributions
                in 5-point bins. Use the legend to toggle each series on or off independently.
                ''',
                unsafe_allow_html=True,
            )

        with col_2:
            st.markdown(
                '''
                #### Baseline Histograms
                Two independent histograms with adjustable baseline sliders.
                The table beneath each chart counts how many students scored
                below, at, and above your chosen threshold — useful for
                identifying students who may need additional support.
                ''',
                unsafe_allow_html=True,
            )

    spacer()

    with st.container(border=True):
        st.markdown(
            '''
            #### Box Plot Comparison
            Side-by-side box plots display the median, quartile spread, and individual
            score points for both assessments. Hover over each plot to inspect exact values.
            ''',
            unsafe_allow_html=True,
        )

def call_to_action_section() -> None:
    with st.container(border=True):
        col_1, col_2 = st.columns(2, vertical_alignment='center')

        with col_1:
            st.markdown(
                '''
                ## Ready to :red[Begin]?

                Create a workspace, upload your dataset, and get your effect size in seconds.
                ''',
                unsafe_allow_html=True,
            )

        with col_2:
            st.markdown(
                '''
                > ##### Quick Checklist
                > - [ ] Dataset has at least 3 columns
                > - [ ] Column 2 = pre-test scores
                > - [ ] Column 3 = post-test scores
                > - [ ] File is `.csv`, `.xlsx`, or `.ods`
                ''',
                unsafe_allow_html=True,
            )

        button = st.button('Create a Workspace', width='stretch')
        if button:
            main.get_new_workspace()
            st.rerun()

# ============================
# execution logic
# ============================

if __name__ == '__main__':
    header()
    workflow()
    spacer()

    data_format_section()
    spacer()

    visualizations_section()
    spacer()

    call_to_action_section()