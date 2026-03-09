import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px
import main # main.py

# ============================
# page setup
# ============================

st.set_page_config(
    layout='centered',
    page_title='Home - Project Hinge Point',
    page_icon='assets/project_hinge_point_logo.png',
)

def separator() -> None:
    st.markdown('---', unsafe_allow_html=True)

def spacer() -> None:
    st.markdown('#####', unsafe_allow_html=True)

# ============================
# page sections
# ============================

def hero_section() -> None:
        st.markdown(
            '''
            # Project :red[Hinge Point]
            Turn :grey[data] into :grey[impact].
            ''',
            unsafe_allow_html=True,
        )

def description() -> None:
    with st.container(border=True):
        col_1, col_2 = st.columns(spec=2, vertical_alignment='center')

        with col_1:
            st.image(image='assets/test_data_1_comp_hist.png', width='stretch')

        with col_2:
            st.markdown(
                '''
                ## What is Project :red[Hinge Point]?
                
                **Project Hinge Point** is your go-to tool for quickly calculating **Hattie effect sizes**,
                a measure of your teaching efficacy.
                Simply input your data and get instant insights to gauge your impactful decisions in education.
                ''',
                unsafe_allow_html=True,
            )

    st.markdown(
        '''
        ## Why do :red[Hattie effect sizes] matter?

        Hattie effect sizes help you understand the impact of your educational strategies. 
        With **Project Hinge Point**,
        you can easily calculate these metrics to make informed decisions and guide meaningful change.

        > *"The best thing you can do...*
        > *is reinforce something you have already learnt."* <br>
        > -- John Hattie (regarding the effect size of specific practices)
        ''',
        unsafe_allow_html=True,
    )

def call_to_action() -> None:
    with st.container(border=True):
        col_1, col_2 = st.columns(spec=2, vertical_alignment='center')

        with col_1:
            col_1.markdown(
                '''
                ## Get :red[started].

                Ready to see your data come to life? <br>

                Click the button below to calculate your Hattie effect size instantly.
                ''',
                unsafe_allow_html=True,
            )

        with col_2:
            st.image(image='assets/test_data_1_dataframe_preview.png', width='stretch')
        
        button = st.button('Create a Workspace', width='stretch')
        if button:
            main.get_new_workspace()
            st.rerun()

def benefits_section() -> None:
    st.markdown('## Why Use Project :red[Hinge Point]?', unsafe_allow_html=True)

    col_1, col_2, col_3, col_4 = st.columns(4)

    with col_1:
        st.image(image='assets/test_data_1_effect_size.png', width='stretch')
        st.markdown('''
            **Instant Insights** <br>

            Calculate effect sizes in seconds.
            ''',
            unsafe_allow_html=True,
        )   

    with col_2:
        st.image(image='assets/test_data_1_key_metrics.png', width='stretch')
        st.markdown('''
            **Data-Driven Decisions** <br>

            Make informed choices based on metrics.
            ''',
            unsafe_allow_html=True,
        )

    with col_3:
        st.image(image='assets/test_data_1_metric_summary.png', width='stretch')
        st.markdown('''
            **User-Friendly** <br>

            No prior statistics experience needed.
            ''',
            unsafe_allow_html=True,
        )

    with col_4:
        st.image(image='assets/test_data_1_comp_box_plot.png', width='stretch')
        st.markdown('''
            **Reliable & Accurate** <br>

            Trustworthy calculations for research.
            ''',
            unsafe_allow_html=True,
        )

def contacts_section() -> None:
    st.markdown(
        '''
        ## :red[Connect] with me.

        Have questions or feedback? I'd love to hear from you!  
        + **Streamlit Profile:** [Kevin Jie](https://share.streamlit.io/user/kevinnnnn-ai)
        + **GitHub:** [Kevinnnnn-ai](https://github.com/Kevinnnnn-ai)
        + **LinkedIn:** [kevin-jie-21a477368](https://www.linkedin.com/in/kevin-jie-21a477368/)
        ''',
        unsafe_allow_html=True,
    )

# ============================
# execution logic
# ============================

if __name__ == '__main__':
    hero_section()
    separator()
    
    description()
    spacer()

    call_to_action()
    spacer()

    benefits_section()
    separator()
    
    contacts_section()