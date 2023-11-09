import streamlit as st
import sentiment

st.title("Sentiment Analysis Tool - AI/ML")
temp="""
<div style= "background-color:#164863; padding:10px";>
<h2 style="color:#9BBEC8; text-align:center;"> Real Time Sentiment Analysis </h2>
</div>
"""
st.markdown(temp, unsafe_allow_html=True)
text=st.text_input("Enter Your Tweets and Posts text here","")

if st.button("Predict the Sentiment"):
    result=sentiment.calculatesentiment(text)
    st.success(result)

