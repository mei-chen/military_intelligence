import streamlit as st
import pandas as pd
import json
import time
st.session_state['loaded'] = 0

st.header('OODAhack')
df = pd.read_csv('data_with_summary.csv')

sum = df['summary'][9]
sum_dict = json.loads(sum)

print(sum_dict['Threat Actions'])

st.sidebar.subheader('Pull in Data')
loaded = st.sidebar.text_input('', help="please enter the URL")

if loaded: 
    st.session_state['loaded']+= 1

if st.session_state['loaded'] == 1:
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)
    my_bar.empty()
    st.session_state['loaded']+= 1
    print(st.session_state['loaded'])

    st.sidebar.title('Documents Loaded')

    for index, row in df.iterrows():
        if st.sidebar.button(row['title']):
            st.sidebar.write(row['url'])

# name = st.sidebar.text_input('Pull in additional data', help="please enter the URL")

uploaded_file = st.sidebar.file_uploader("Add additional PDFs", type=["pdf"])

st.sidebar.button('Filter')

if loaded:
    one, two = st.columns([3,1])
    with one: 
        st.title('Types of Attack')

        but1 = st.button('Data exfiltration and credential access')
        if but1: 
            st.markdown(f"**{df['title'][1]}**")
            st.write(json.loads(df['summary'][1])['Procedures'])
            st.subheader('MITRE ATT&CK Techniques')
            st.write(json.loads(df['summary'][1])['Tactics'])
            st.write(json.loads(df['summary'][1])['Techniques'])

        with two: 
            options = ['Types of Attack', 'Area Impacted', 'Procedure', 'Tactic', 'Time Occurred']
            st.selectbox('View by:', options)

        but2 = st.button('Posting documents containing sensitive information on the dark web') 

        but3 = st.button('Deployment of ALPHV Blackcat ransomware')
        if but3:
            st.markdown(f"**{df['title'][7]}**")
            st.write(json.loads(df['summary'][7])['Procedures'])
            st.subheader('MITRE ATT&CK Techniques')
            st.write(json.loads(df['summary'][1])['Tactics'])
            st.write(json.loads(df['summary'][1])['Techniques'])

    with two:
        st.write('count: 4')
        st.write('')
        st.write('count: 3')
        st.write('')
        st.write('count: 1')

    st.write('')
    st.write('')

    search = st.text_input('Search', '')
    if search == 'health':
        st.markdown(f"**{df['title'][9]}**")
        st.write(json.loads(df['summary'][9])['Procedures'])
        st.subheader('MITRE ATT&CK Techniques')
        st.write(json.loads(df['summary'][9])['Tactics'])
        st.write(json.loads(df['summary'][9])['Techniques'])

    if search == 'web server':
        st.markdown(f"**{df['title'][6]}**")
        st.write(f"https://firebasestorage.googleapis.com/v0/b/ooda-nsec.appspot.com/o/data%2Fweb%20server%20affected.pdf?alt=media&token=8c481e05-9e8d-4f28-b70b-b21eea99cb3a")
        st.write(json.loads(df['summary'][6])['Procedures'])
        st.subheader('MITRE ATT&CK Techniques')
        st.write(json.loads(df['summary'][6])['Tactics'])
        st.write(json.loads(df['summary'][6])['Techniques'])