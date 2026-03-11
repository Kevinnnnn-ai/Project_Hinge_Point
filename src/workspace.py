import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

def header(workspace_name: str) -> None:
    st.markdown(f'# {workspace_name}', unsafe_allow_html=True)

def check_header(workspace_name: str, workspace_id: str) -> None:
    if workspace_name != st.session_state.workspaces[workspace_id]['name']:
        st.rerun() # for matching header/workspace name

def file_upload_and_preview(workspace_id: str) -> None:
    with st.container(border=True):
        st.markdown('# File Upload', unsafe_allow_html=True)

        col_1, col_2 = st.columns([2, 3])
        with col_1:
            with st.container(border=True):
                st.markdown('#### **Expectations & Exceptions**:', unsafe_allow_html=True)
                st.markdown(
                    '''
                    The first three columns must be ordered: student, pre-test score, and post-test score.

                    Note that the *name* of each heading, *number* of headings, and *order* of the headings
                    (past the first three) does not matter.
                    ''',
                    unsafe_allow_html=True,
                )

                st.markdown(
                    '''
                    In the event that you do not have a student column, make a column in place of where the student
                    name column should be and fill it with random values. Student names are *not* needed for
                    functionality.
                    ''',
                    unsafe_allow_html=True,
                )

        with col_2:
            if st.button('Delete dataset', width='stretch', icon=':material/do_not_disturb_on:'):
                st.session_state.workspaces[workspace_id]['dataframe'] = None
                st.session_state['uploader_key'] += 1  # forces uploader to reset
                st.rerun()

            if 'uploader_key' not in st.session_state:
                st.session_state['uploader_key'] = 0

            dataset = st.file_uploader(
                label='Upload dataset. (csv, xlsx, or ods)',
                type=['csv', 'xlsx', 'ods'], # 3 most common dataset types
                accept_multiple_files=False,
                width='stretch',
                key=st.session_state['uploader_key'],  # changing this resets the widget
            )

            dataframe = st.session_state.workspaces[workspace_id]['dataframe']
            dummyframe = {'Student': [], 'Pre-test Scores': [], 'Post-test Scores': []}
            # redundant conditionals are purely to adjust dataframe's height
            if dataset is not None:
                try:
                    if dataset.type == 'text/csv':
                        dataframe = pd.read_csv(dataset)
                    elif dataset.type == 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet':
                        dataframe = pd.read_excel(dataset)
                    elif dataset.type == 'application/vnd.oasis.opendocument.spreadsheet':
                        dataframe = pd.read_excel(dataset, engine='odf')

                    if dataframe is None: # meaning first upload
                        st.dataframe(dataframe, width=400, height=361, hide_index=True)
                    elif dataframe is not None: # meaning another upload
                        st.dataframe(dataframe, width=400, height=304, hide_index=True)
                    st.session_state.workspaces[workspace_id]['dataframe'] = dataframe

                except:
                    st.error('**RUNTIME ERROR**: Dataframe creation error.')
                    st.dataframe(dummyframe, width=400, height=361, hide_index=True)

            elif dataset is None and dataframe is not None: # meaning previously uploaded (either switched pages or deleted)
                st.dataframe(dataframe, width=400, height=361, hide_index=True)
            elif dataset is None and dataframe is None: # meaning no action or re-uploaded and deleted
                st.dataframe(dummyframe, width=400, height=361, hide_index=True)

def calculate(workspace_id: str) -> None:
    dataframe = st.session_state.workspaces[workspace_id]['dataframe']
    if dataframe is not None:
        try:
            pre_heading     = dataframe.columns[1] # columns could be named differently, so define it as a numerical location
            post_heading    = dataframe.columns[2]
            pre_scores      = dataframe[pre_heading]
            post_scores     = dataframe[post_heading]
            sample_size     = len(dataframe)

            st.session_state.workspaces[workspace_id]['dataframe_statistics'].update({'sample_size': sample_size})
        except:
            st.error('**RUNTIME ERROR**: Dataframe scope error.')

        try:
            pre_min     = pre_scores.min()
            pre_max     = pre_scores.max()
            pre_range   = pre_max - pre_min
            pre_mean    = pre_scores.mean()
            pre_q1      = pre_scores.quantile(0.25)
            pre_q3      = pre_scores.quantile(0.75)
            pre_iqr     = pre_q3 - pre_q1
            pre_std     = pre_scores.std()

            st.session_state.workspaces[workspace_id]['pre_score_statistics'].update(
                {
                    'pre_min': pre_max, 'pre_max': pre_max, 'pre_range': pre_range, 'pre_mean': pre_mean,
                    'pre_q1': pre_q1, 'pre_q3': pre_q3, 'pre_iqr': pre_iqr, 'pre_std': pre_std,
                }
            )

        except:
            st.error('**RUNTIME ERROR**: Pre-test calculation error.')

        try:
            post_min    = post_scores.min()
            post_max    = post_scores.max()
            post_range  = post_max - post_min
            post_mean   = post_scores.mean()
            post_q1     = post_scores.quantile(0.25)
            post_q3     = post_scores.quantile(0.75)
            post_iqr    = post_q3 - post_q1
            post_std    = post_scores.std()

            st.session_state.workspaces[workspace_id]['post_score_statistics'].update(
                {
                    'post_min': post_min, 'post_max': post_max, 'post_range': post_range, 'post_mean': post_mean,
                    'post_q1': post_q1, 'post_q3': post_q3, 'post_iqr': post_iqr, 'post_std': post_std,
                }
            )

        except:
            st.error('**RUNTIME ERROR**: Post-test calculation error.')

        try:
            mean_diff               = post_mean - pre_mean
            pooled_std_numerator    = ((sample_size - 1) * pre_std ** 2) + ((sample_size - 1) * post_std ** 2)
            pooled_std_denominator  = sample_size * 2 - 2
            pooled_std              = np.sqrt(pooled_std_numerator / pooled_std_denominator)

            if pooled_std > 0:
                cohens_d = mean_diff / pooled_std 
            else:
                cohens_d = 0
            hinge_point = 0.40
            is_above_hinge = cohens_d >= hinge_point

            st.session_state.workspaces[workspace_id]['dataframe_statistics'].update(
                {
                    'sample_size': sample_size, 'mean_diff': mean_diff, 'pooled_std': pooled_std, 'cohens_d': cohens_d,
                    'hinge_point': hinge_point, 'is_above_hinge': is_above_hinge,
                }
            )

        except:
            st.error("**RUNTIME ERROR**: Effect size (Cohen's d) calculation error.")

    else:
        st.warning('**WARNING**: Dataframe has not been detected.')

def metric_summary(workspace_id: str) -> None:
    with st.container(border=True):
        st.markdown('# Metric Summary', unsafe_allow_html=True)

        dataframe = st.session_state.workspaces[workspace_id]['dataframe']
        col_1, col_2 = st.columns(2)
        if dataframe is not None:
            with col_1:
                st.markdown('#### **Pre-test**:')

                try:
                    st.dataframe(
                        data={
                            'Metric': [
                                'Min',
                                'Max',
                                'Range',
                                'Mean (x̄₁)',
                                '1st Quartile (Q1₁)',
                                '3rd Quartile (Q3₁)',
                                'Interquartile Range (IQR₁)',
                                'Standard Deviation (s₁)',
                            ],
                            'Value': [
                                f'{st.session_state.workspaces[workspace_id]['pre_score_statistics']['pre_min']:.2f}',
                                f'{st.session_state.workspaces[workspace_id]['pre_score_statistics']['pre_max']:.2f}',
                                f'{st.session_state.workspaces[workspace_id]['pre_score_statistics']['pre_range']:.2f}',
                                f'{st.session_state.workspaces[workspace_id]['pre_score_statistics']['pre_mean']:.2f}',
                                f'{st.session_state.workspaces[workspace_id]['pre_score_statistics']['pre_q1']:.2f}',
                                f'{st.session_state.workspaces[workspace_id]['pre_score_statistics']['pre_q3']:.2f}',
                                f'{st.session_state.workspaces[workspace_id]['pre_score_statistics']['pre_iqr']:.2f}',
                                f'{st.session_state.workspaces[workspace_id]['pre_score_statistics']['pre_std']:.2f}',
                            ],
                        }
                    )
                except:
                    st.error('**RUNTIME ERROR**: Pre-test metric summary display error.')

            with col_2:
                st.markdown('#### **Post-test**:')

                try:
                    st.dataframe(
                        data={
                            'Metric': [
                                'Min',
                                'Max',
                                'Range',
                                'Mean (x̄₂)',
                                '1st Quartile (Q1₂)',
                                '3rd Quartile (Q3₂)',
                                'Interquartile Range (IQR₂)',
                                'Standard Deviation (s₂)',
                            ],
                            'Value': [
                                f'{st.session_state.workspaces[workspace_id]['post_score_statistics']['post_min']:.2f}',
                                f'{st.session_state.workspaces[workspace_id]['post_score_statistics']['post_max']:.2f}',
                                f'{st.session_state.workspaces[workspace_id]['post_score_statistics']['post_range']:.2f}',
                                f'{st.session_state.workspaces[workspace_id]['post_score_statistics']['post_mean']:.2f}',
                                f'{st.session_state.workspaces[workspace_id]['post_score_statistics']['post_q1']:.2f}',
                                f'{st.session_state.workspaces[workspace_id]['post_score_statistics']['post_q3']:.2f}',
                                f'{st.session_state.workspaces[workspace_id]['post_score_statistics']['post_iqr']:.2f}',
                                f'{st.session_state.workspaces[workspace_id]['post_score_statistics']['post_std']:.2f}',
                            ],
                        }
                    )
                except:
                    st.error('**RUNTIME ERROR**: Post-test metric summary display error.')

            st.markdown('#### **Effect Size**:')

            try:
                st.dataframe(
                    data={
                        'Metric': [
                            'Effect Size (d)',
                            'Hinge Point',
                            'Is Above Hinge Point',
                            'Sample Size (n)',
                            'Mean Difference (Δx̄)',
                            'Pooled Standard Deviation (sₚ)',
                        ],
                        'Value': [
                            f'{st.session_state.workspaces[workspace_id]['dataframe_statistics']['cohens_d']:.2f}',
                            f'{st.session_state.workspaces[workspace_id]['dataframe_statistics']['hinge_point']:.2f}',
                            f'{st.session_state.workspaces[workspace_id]['dataframe_statistics']['is_above_hinge']}',
                            f'{st.session_state.workspaces[workspace_id]['dataframe_statistics']['sample_size']}',
                            f'{st.session_state.workspaces[workspace_id]['dataframe_statistics']['mean_diff']:.2f}',
                            f'{st.session_state.workspaces[workspace_id]['dataframe_statistics']['pooled_std']:.2f}',
                        ],
                    }
                )
            except:
                st.error('**RUNTIME ERROR**: Effect size metric summary display error.')

        else:
            with col_1:
                st.markdown('#### **Pre-test**:')
                st.dataframe({'Metric': [], 'Value': []}, hide_index=True)
            with col_2:
                st.markdown('#### **Post-test**:')
                st.dataframe({'Metric': [], 'Value': []}, hide_index=True)
            st.markdown('#### **Effect Size**:')
            st.dataframe({'Metric': [], 'Value': []}, hide_index=True)

def key_metrics(workspace_id: str) -> None:
    dataframe = st.session_state.workspaces[workspace_id]['dataframe']
    with st.container(border=True):
        st.markdown('# Key Metrics', unsafe_allow_html=True)
        
        col_1, col_2 = st.columns([1, 3])
        if dataframe is not None:
            post_mean   = st.session_state.workspaces[workspace_id]['post_score_statistics']['post_mean']
            mean_diff   = st.session_state.workspaces[workspace_id]['dataframe_statistics']['mean_diff']
            cohens_d    = st.session_state.workspaces[workspace_id]['dataframe_statistics']['cohens_d']
            hinge_point = st.session_state.workspaces[workspace_id]['dataframe_statistics']['hinge_point']
            is_above_hinge = st.session_state.workspaces[workspace_id]['dataframe_statistics']['is_above_hinge']
            pre_std     = st.session_state.workspaces[workspace_id]['pre_score_statistics']['pre_std']
            post_std    = st.session_state.workspaces[workspace_id]['post_score_statistics']['post_std']
            pooled_std  = st.session_state.workspaces[workspace_id]['dataframe_statistics']['pooled_std']

            try:
                with col_1:
                    st.metric(
                        label='Post-test Mean (x̄₂)',
                        border=True, value=f'{post_mean:.2f}',
                        delta=f'{mean_diff:.2f}',
                    )
                    st.metric(
                        label='Post-test SD (s₂)',
                        value=f'{post_std:.2f}', border=True,
                        delta=f'{post_std - pre_std:-.2f}', delta_color='inverse',
                    )
            except:
                st.error('**RUNTIME ERROR**: Key metrics display 1 error.')
            
            try:
                with col_2:
                    if is_above_hinge:
                        color = '#5ae086'
                    else:
                        color = '#ff6c6c'

                    gauge = go.Figure(
                        go.Indicator(
                            mode='gauge+number+delta',
                            value=cohens_d,
                            number={'prefix': 'Effect Size (d): ','font': {'size': 25}},
                            delta={'reference': hinge_point, 'suffix': ' from hinge'},
                            gauge={
                                'axis': {
                                    'range': [0, 1.5],
                                    'tickvals': [0.2, 0.4, 0.8, 1.2],
                                    'ticktext': ['Small Effect', 'Hinge Point', 'Moderate Effect', 'Large Effect']
                                },
                                'bar': {'color': color},
                                'steps': [
                                    {'range': [0, 0.2],  'color': '#000000'},
                                    {'range': [0.2, 0.4], 'color': '#252525'},
                                    {'range': [0.4, 0.8], 'color': '#444444'},
                                    {'range': [0.8, 1.2], 'color': '#656565'},
                                    {'range': [1.2, 1.5], 'color': '#7c7c7c'},
                                ],
                                'threshold': {
                                    'line': {'color': 'white', 'width': 2},
                                    'thickness': 0.75,
                                    'value': hinge_point,
                                },
                            },
                        )
                    
                    )

                    gauge.update_layout(
                        height=250, margin=dict(t=60, b=0, l=40, r=40),
                        paper_bgcolor='rgba(0,0,0,0)',
                    )
                    
                    with st.container(border=True):
                        st.plotly_chart(gauge, width='stretch', height=255)

            except:
                st.error('**RUNTIME ERROR**: Key metrics display 2 error.')
    
        else:
            with col_1:
                st.metric(
                    label='Post-test Mean (x̄₂)',
                    border=True, value=f'{0:.2f}',
                    delta=f'{0:.2f}', delta_color='off',
                )

                st.metric(
                    label='Post-test SD (s₂)',
                    value=f'{0:.2f}', border=True,
                    delta=f'{0:-.2f}', delta_color='off',
                )

            with col_2:
                gauge = go.Figure(
                    go.Indicator(
                        mode='gauge+number+delta', value=0.00,
                        number={'prefix': 'Effect Size (d): ','font': {'size': 25}},
                        delta={'reference': 0.4, 'suffix': ' from hinge'},
                        gauge={
                            'axis': {
                                'range': [0, 1.5],
                                'tickvals': [0.2, 0.4, 0.8, 1.2],
                                'ticktext': ['Small Effect', 'Hinge Point', 'Moderate Effect', 'Large Effect']
                            },
                            'bar': {'color': '#464646'},
                            'steps': [
                                {'range': [0, 0.2],  'color': '#000000'},
                                {'range': [0.2, 0.4], 'color': '#252525'},
                                {'range': [0.4, 0.8], 'color': '#444444'},
                                {'range': [0.8, 1.2], 'color': '#656565'},
                                {'range': [1.2, 1.5], 'color': '#7c7c7c'},
                            ],
                            'threshold': {
                                'line': {'color': 'white', 'width': 2},
                                'thickness': 0.75,
                                'value': 0.4,
                            },
                        },
                    )
                )

                gauge.update_layout(
                    height=250, margin=dict(t=60, b=0, l=40, r=40),
                    paper_bgcolor='rgba(0,0,0,0)',
                )
                
                with st.container(border=True):
                    st.plotly_chart(gauge, width='stretch', height=255)

def make_workspace_page(workspace_id: str) -> callable:
    def workspace_page(): # convert workspace_id to a callable that can be used as a page
        workspace_name = st.session_state.workspaces[workspace_id]['name']
        workspace_description  = st.session_state.workspaces[workspace_id]['description']

        st.set_page_config(
            layout='centered',
            page_title=f'{workspace_name} - Project Hinge Point',
            page_icon='res/placeholder_image.png',
        )

        header(workspace_name)

        st.session_state.workspaces[workspace_id]['name'] = st.text_area(
            label='Enter workspace name here:',
            height=100, width='stretch',
            placeholder='Enter name here...',
            value=workspace_name,
        )

        st.session_state.workspaces[workspace_id]['description'] = st.text_area(
            label='Enter workspace description here:',
            height='content', width='stretch',
            placeholder='Enter description here...',
            value=workspace_description,
        )

        check_header(workspace_name=workspace_name, workspace_id=workspace_id)
        file_upload_and_preview(workspace_id=workspace_id)
        calculate(workspace_id=workspace_id)
        metric_summary(workspace_id=workspace_id)
        key_metrics(workspace_id=workspace_id)

    return workspace_page