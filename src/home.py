import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import plotly.express as px

st.set_page_config(
    layout='centered',
    page_title='Home - Project Hinge Point',
    page_icon='assets/placeholder_image.png',
)

def spacer() -> None:
    st.markdown('---')

def hero_section() -> None:
    st.title('Project Hinge Point')
    st.markdown('Turn :grey[data] into :grey[impact].', unsafe_allow_html=True)

def description() -> None:
    col1, col2 = st.columns(2, vertical_alignment='center', border=True)
    col1.image('assets/placeholder_image.png', width='stretch')
    col2.markdown(
        '''
        ## What is Project :red[Hinge Point]?
        **Project Hinge Point** is your go-to tool for quickly calculating **Hattie effect sizes**. 
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
        >  "The best thing you can do...
        is reinforce something you have already learnt." <br>
        -- John Hattie (regarding the effect size of specific practices)
        ''',
        unsafe_allow_html=True,
    )

def example_section() -> None:
    st.markdown('> Example Input', unsafe_allow_html=True)
    example_dataframe = pd.DataFrame(
        {
            'student': [
                'Alice', 'Bob', 'Charlie', 'Daniel', 'Elena', 
                'Felix', 'Grace', 'Henry', 'Isla', 'Julian', 
                'Keira', 'Liam', 'Maya', 'Noah', 'Olivia', 
                'Peter', 'Quinn', 'Rachel', 'Samuel', 'Talia', 
                'Uriah', 'Violet', 'William', 'Xander', 'Yara',
            ],
            'score_before': [
                78, 82, 90, 60, 81,
                55, 70, 63, 77, 52,
                68, 85, 74, 61, 88,
                59, 73, 66, 50, 79,
                62, 71, 80, 54, 76,
            ],
            'score_after': [
                85, 88, 93, 72, 91,
                66, 81, 74, 88, 64,
                79, 94, 85, 73, 97,
                70, 85, 77, 61, 89,
                73, 82, 91, 65, 87,
            ],
        }
    )
    st.dataframe(example_dataframe)

    st.markdown('> Example Output', unsafe_allow_html=True)
    pre_test_scores = example_dataframe['score_before']
    post_test_scores = example_dataframe['score_after']

    pre_mean = pre_test_scores.mean()
    post_mean = post_test_scores.mean()
    mean_diff = post_mean - pre_mean
    pre_standard_deviation = pre_test_scores.std()
    post_standard_deviation = post_test_scores.std()
    pooled_standard_deviation = np.sqrt((pre_standard_deviation ** 2 + post_standard_deviation ** 2) / 2)
    if pooled_standard_deviation > 0:
        cohens_d = mean_diff / pooled_standard_deviation 
    else:
        cohens_d = 0
    hinge_point = 0.40
    above_hinge = cohens_d >= hinge_point

    st.markdown('### Key Metrics', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric('Pre-test Mean', f'{pre_mean:.2f}')
    col2.metric('Post-test Mean', f'{post_mean:.2f}')
    col3.metric('Mean Improvement', f'{mean_diff:.2f}')
    col4.metric('Effect Size', f'{cohens_d:.2f}')
    col5, col6, col7 = st.columns(3)
    col5.metric('Pre-test Standard Deviation', f'{pre_standard_deviation:.2f}')
    col6.metric('Post-test Standard Deviation', f'{post_standard_deviation:.2f}')
    col7.metric('Pooled Standard Deviation', f'{pooled_standard_deviation:.2f}')

    if cohens_d < 0.2:
        impact_label = 'Small Effect'
    elif cohens_d < 0.4:
        impact_label = 'Below Hinge Point'
    elif cohens_d < 0.8:
        impact_label = 'Moderate Effect'
    else:
        impact_label = 'Large Effect'
    st.success(f'Impact Category: {impact_label}')
    if above_hinge:
        st.success("This intervention exceeds Hattie's 0.40 hinge point.")
    else:
        st.warning('This intervention falls below the 0.40 hinge point.')

    st.markdown('### Score Distribution Comparison')
    comparison_histogram_labels = ['Pre-test', 'Post-test']
    comparison_histogram_data = [pre_test_scores, post_test_scores]
    comparison_histogram = ff.create_distplot(
        comparison_histogram_data,
        comparison_histogram_labels,
    )
    st.plotly_chart(comparison_histogram)

    st.markdown(
        '''
        > End of example...
        
        ...and get more data visualizations and tools with your own workspaces!
        '''
    )
    if st.button('Create a Workspace'):
        st.write('Redirecting to the workspace')

def call_to_action() -> None:
    st.markdown(
        '''
        ## Get :red[started].
        Ready to see your data come to life? <br>
        Look at this example and click the button below to calculate your Hattie effect size instantly.
        ''',
        unsafe_allow_html=True,
    )

def benefits_section() -> None:
    st.markdown('## Why Use Project :red[Hinge Point]?', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    col1.image('assets/placeholder_image.png', width='stretch')
    col1.markdown('''
        **Instant Insights** <br>
        Calculate effect sizes in seconds.
        ''',
        unsafe_allow_html=True,
    )

    col2.image('assets/placeholder_image.png', width='stretch')
    col2.markdown('''
        **Data-Driven Decisions** <br>
        Make informed choices based on metrics.
        ''',
        unsafe_allow_html=True,
    )

    col3.image('assets/placeholder_image.png', width='stretch')
    col3.markdown('''
        **User-Friendly** <br>
        No prior statistics experience needed.
        ''',
        unsafe_allow_html=True,
    )

    col4.image('assets/placeholder_image.png', width='stretch')
    col4.markdown('''
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
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    hero_section()
    spacer()
    description()
    spacer()
    call_to_action()
    example_section()
    spacer()
    benefits_section()
    spacer()
    contacts_section()