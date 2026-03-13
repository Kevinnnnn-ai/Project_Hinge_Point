import streamlit as st
from main import get_new_workspace

st.set_page_config(
    layout='centered',
    page_title='About - Project Hinge Point',
    page_icon='res/placeholder_image.png',
)

def value_proposition() -> None:
    st.markdown(
        '''
        # About Project Hinge Point
        ##### Turning educational data into insight.
        ''',
        unsafe_allow_html=True
    )

    with st.container(border=True):
        col_1, col_2, col_3 = st.columns(3)
        with col_1:
            st.image('res/placeholder_image.png')
            st.markdown('#### Instant Analysis', unsafe_allow_html=True)
        with col_2:
            st.image('res/placeholder_image.png')
            st.markdown('#### Clear Benchmarks', unsafe_allow_html=True)
        with col_3:
            st.image('res/placeholder_image.png')
            st.markdown('#### Visual Insights', unsafe_allow_html=True)

def story() -> None:
    col_1, col_2 = st.columns([3,4], vertical_alignment='center')
    with col_1:
        st.image('res/placeholder_image.png', width='stretch')
        st.image('res/placeholder_image.png', width='stretch')

    col_2.markdown(
        '''
        ## The Why

        Teachers collect numerous amounts of classroom data, but turning that data into a clear
        picture of impact has always required specialized statistical tools.

        Most educators don't have the time, training, or access to those tools. In fact, many
        important decisions get made on instinct rather than evidence, as patterns in the data can go unnoticed.

        Project Hinge Point was built to change that, an *accessible* interface that turns
        data into insight directly within the hands of the people who need it most.
        ''',
        unsafe_allow_html=True,
    )

def mission() -> None:
    with st.container(border=True):
        col_1, col_2 = st.columns(2, vertical_alignment='center')
        col_1.markdown(
            '''
            ## Mission & Values

            The mission is to make statistical analysis *accessible*, *interpretable*,
            and *usable* for every teacher.

            We believe that:
            + Data belongs to *teachers*.
            + Good tools should be *simple* and *accurate*.
            ''',
            unsafe_allow_html=True,
        )

        col_2.image('res/placeholder_image.png', width='stretch')

def team() -> None:
    col_1, col_2 = st.columns([7, 5], vertical_alignment='center')
    col_1.image('res/placeholder_image.png', width='stretch')

    col_2.markdown(
        '''
        ## The Creator & Developer

        My name is Kevin Jie, and I built Project Hinge Point to bridge the gap between *educational research*
        and *classroom practices* at Temple High School. I want to focus on combining statistical analysis
        with graphical interfaces that anyone can use.
        ''',
        unsafe_allow_html=True,
    )

def credibility() -> None:
    with st.container(border=True):
        col_1, col_2 = st.columns([2, 1], vertical_alignment='center')
        col_1.markdown(
            '''
            ## The Research Behind It

            *John Hattie's* synthesis of over 800 meta-analyses, published in
            *Visible Learning* (2009), remains one of the most comprehensive
            investigations into what actually drives student achievement.

            His central finding: an *effect size of 0.40* represents the average
            yearly learning growth expected of a student. Practices that exceed
            this threshold are considered above-average contributors to learning.

            Project Hinge Point implements this benchmark so educators can
            measure their own impact against a globally recognized standard.
            ''',
            unsafe_allow_html=True,
        )

        col_2.markdown(
            '''
            > *"The remarkable feature of the evidence is that the greatest effects
            > on student learning occur when teachers become learners of their
            > own teaching."*
            > -- John Hattie, *Visible Learning*
            ''',
            unsafe_allow_html=True,
        )

def call_to_action() -> None:
    col_1, col_2 = st.columns(2, vertical_alignment='center')
    col_1.markdown(
        '''
        ## Ready to Get Started?

        Upload your pre- and post-test data and see your instructional
        impact measured in seconds. No statistics background required.
        ''',
        unsafe_allow_html=True,
    )

    col_2.image('res/placeholder_image.png', width='stretch')

    button = st.button('Create Workspace', width='stretch', icon=':material/add_circle:')
    if button:
        get_new_workspace()
        st.rerun()

if __name__ == '__main__':
    value_proposition()
    story()
    mission()
    team()
    credibility()
    call_to_action()