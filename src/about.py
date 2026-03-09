import streamlit as st
import main # main.py

# ============================
# page setup
# ============================

st.set_page_config(
    layout='centered',
    page_title='About - Project Hinge Point',
    page_icon='assets/project_hinge_point_logo.png',
)

def separator() -> None:
    st.markdown('---', unsafe_allow_html=True)

def spacer() -> None:
    st.markdown('#####', unsafe_allow_html=True)

# ============================
# page sections
# ============================

def value_proposition_section() -> None:
    st.markdown(
        '''
        # About :red[Project Hinge Point]
        Turning :grey[educational data] into :grey[meaningful insight].
        ''',
        unsafe_allow_html=True,
    )

    separator()

    with st.container(border=True):
        col_1, col_2, col_3 = st.columns(3)
        
        with col_1:
            st.image('assets/test_data_2_metric_summary.png')
            st.markdown(
                '''
                #### Instant Analysis
                Upload your data and get statistical results in seconds, no software expertise needed.
                ''',
                unsafe_allow_html=True,
            )

        with col_2:
            st.image('assets/test_data_2_effect_size_interpretation.png')
            st.markdown(
                '''
                #### Clear Benchmarks
                Every result is measured against Hattie's **0.40 hinge point**, giving your data immediate context.
                ''',
                unsafe_allow_html=True,
            )

        with col_3:
            st.image('assets/test_data_2_comp_hist.png')
            col_3.markdown(
                '''
                #### Visual Insights
                Pre- and post-test comparisons are rendered as interactive charts you can explore and share.
                ''',
                unsafe_allow_html=True,
            )

def story_section() -> None:
    col_1, col_2 = st.columns([3,4], vertical_alignment='center')

    with col_1:
        st.image('assets/laptop_on_desk_image.jpg', width='stretch')
        st.image('assets/data_illustration.jpg', width='stretch')

    with col_2:
        st.markdown(
            '''
            ## The :red[Why]

            Teachers collect copius amounts of classroom data, but turning that data into a clear
            picture of impact has always required specialized statistical tools. <br>

            Most educators don't have the time, training, or access to those tools. In fact, many
            important decisions get made on instinct rather than evidence, as  patterns in the data can go unnoticed. <br>

            **Project Hinge Point** was built to change that, an accessible interface that turns
            data into insight directly within the hands of the people who need it most.
            ''',
            unsafe_allow_html=True,
        )

def mission_section() -> None:
    with st.container(border=True):
        col_1, col_2 = st.columns(2, vertical_alignment='center')

        with col_1:
            st.markdown(
                '''
                ## Mission :red[&] Values

                The mission is to make statistical analysis **accessible, interpretable,
                and usable** for every teacher. <br>

                We believe that:
                + Data belongs to **teachers**.
                + Good tools should be **simple** and **accurate**.
                ''',
                unsafe_allow_html=True,
            )

        with col_2:
            st.image('assets/project_hinge_point_logo.png', width='stretch')

def team_section() -> None:
    st.markdown('## The :red[Team]', unsafe_allow_html=True)

    col_1, col_2 = st.columns([14, 10], vertical_alignment='center')

    with col_1:
        st.image('assets/temple_high_school.jpeg', width='stretch')

    with col_2:
        st.markdown(
            '''
            #### The :red[Creator & Developer]

            I built Project Hinge Point to bridge the gap between educational
            research and classroom practices. I want to focus on combining
            statistical analysis with graphical interfaces that anyone can use. <br>

            + **Streamlit:** [Kevin Jie](https://share.streamlit.io/user/kevinnnnn-ai)
            + **GitHub:** [Kevinnnnn-ai](https://github.com/Kevinnnnn-ai)
            + **LinkedIn:** [kevin-jie-21a477368](https://www.linkedin.com/in/kevin-jie-21a477368/)
            ''',
            unsafe_allow_html=True,
        )

def credibility_section() -> None:
    with st.container(border=True):
        col_1, col_2 = st.columns([2, 1], vertical_alignment='center')

        with col_1:
            st.markdown(
                '''
                ## The Research :red[Behind It]

                **John Hattie's** synthesis of over 800 meta-analyses — published in
                *Visible Learning* (2009) — remains one of the most comprehensive
                investigations into what actually drives student achievement. <br>

                His central finding: an **effect size of 0.40** represents the average
                yearly learning growth expected of a student. Practices that exceed
                this threshold are considered **above-average contributors** to learning. <br>

                Project Hinge Point operationalizes this benchmark so educators can
                measure their own instructional impact against a globally recognized standard.
                ''',
                unsafe_allow_html=True,
            )

        with col_2:
            st.markdown(
                '''
                > *"The remarkable feature of the evidence is that the greatest effects
                > on student learning occur when teachers become learners of their
                > own teaching."*
                > -- John Hattie, *Visible Learning*
                ''',
                unsafe_allow_html=True,
            )

def call_to_action_section() -> None:
    col_1, col_2 = st.columns(2, vertical_alignment='center')
    
    with col_1:
        st.markdown(
            '''
            ## Ready to :red[Get Started]?

            Upload your pre- and post-test data and see your instructional
            impact measured in seconds. No statistics background required.
            ''',
            unsafe_allow_html=True,
        )

    with col_2:
        with st.container(border=True):
            st.image('assets/file_upload_section.png', width='stretch')

    button = st.button('Create a Workspace', width='stretch')
    if button:
        main.get_new_workspace()
        st.rerun()

# ============================
# execution logic
# ============================

if __name__ == '__main__':
    value_proposition_section()
    spacer()

    story_section()
    spacer()

    mission_section()
    spacer()

    team_section()
    spacer()

    credibility_section()
    spacer()

    call_to_action_section()