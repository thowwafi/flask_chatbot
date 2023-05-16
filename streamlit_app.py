import os 
import streamlit as st 


# App framework
st.title('ChatBot - Build Vector Index')
st.markdown('This is a simple app to show the source data for the ChatBot.')
st.markdown('---')


st.header('Vector Index')
st.markdown('Click the button below to rebuild the vector index.')
if st.button('Rebuild Vector Index'):
    os.system('python createVectorIndex.py Store')
    st.info('Vector Index Rebuilded.')
# Add data
st.header('Add Data')
# add file
files = st.file_uploader('Upload file', type=['txt'], accept_multiple_files=True)
for file in files:
    if file:
        # save file
        with open(f'Source/{file.name}', 'w') as f:
            f.write(file.getvalue().decode('utf-8'))
        st.info(f'{file.name} saved.')
# Load data
st.header('Load Data')
# read list of files inside Source folder
files = os.listdir('Source')
# show list of files
if not files:
    st.info('No file found.')
for file in files:
    with st.expander(file):
        if st.button('Delete', key=file):
            os.remove(f'Source/{file}')
            st.info(f'{file} deleted.')
            # check if file exist
        if os.path.isfile(f'Source/{file}'):
            with open(f'Source/{file}', 'r') as f:
                st.info(f.read())
