# pip install streamlit
# pip install -U plotly

import streamlit as st
import pickle

# loading the trained model
model = pickle.load(open('model.pkl', 'rb'))

# create the title
st.title('Predicting if massage is spam or not')

message = st.text_input('Enter a message')

submit = st.button('Predict')

if submit:
    prediction = model.predict([message])
    print(prediction)
    st.write(prediction)

    if prediction[0] == 'spam':
        st.write('This is a spam message')
    else:
        st.write('This is a ham message')
st.balloons()