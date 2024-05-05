import streamlit as st
import pandas as pd
import json

df = pd.read_csv('data_with_summary.csv')

sum = df['summary'][7]
sum_dict = json.loads(sum)
print(sum_dict['Threat Actions'])

st.sidebar.title('Documents Loaded')

for index, row in df.iterrows():
    if st.sidebar.button(row['title']):
        st.sidebar.write(row['url'])

name = st.sidebar.text_input('Pull in additional data', help="please enter the URL")

uploaded_file = st.sidebar.file_uploader("Add additional PDFs", type=["pdf"])

st.sidebar.button('Filter')

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
    # space
    # st.write('')
    # st.write('')
   
    st.write('count: 4')
    st.write('')
    st.write('count: 3')
    st.write('')
    st.write('count: 1')
