import streamlit
import nltk
from streamlit_option_menu import option_menu
from nltk.corpus import stopwords
import pandas as pd
import numpy as np


# with streamlit.sidebar:
#      menu_title='main menu',
    
streamlit.set_page_config(page_title='Homepage', page_icon=':house:')

# Add content to the app
streamlit.header("Welcome to my Spam Detector app!")

with open("style.css", "r") as css_file:
    custom_css = f"<style>{css_file.read()}</style>"
    streamlit.markdown(custom_css, unsafe_allow_html=True)

body="""
<style>
body {
    display: block;
    margin: 28px;
}
.css-ocqkz7 {
    display: flex;
    flex-wrap: wrap;
    width: 100%;
    /* -webkit-box-flex: 3; */
    flex-grow: 1;
    -webkit-box-align: stretch;
    align-items: stretch;
    margin-left:3%;
    gap: 2rem;
}
.css-ffhzg2 {
    position: absolute;
    background-image: linear-gradient(to bottom, #9795f0 0%, #fbc8d4 100%);    inset: 0px;
    overflow: hidden;
}
h1 {
    color: #007bff;
    font-size: 36px;
  }
h2 {
    color: black;
    font-size: 42px;
  }
 h3 {
    color: white;
    font-size: 30px;
  }
  .css-1avcm0n {
    position: fixed;
    border:0;
    top: 0px;
    left: 0px;
    right: 0px;
    height: 2rem;
    background-image: linear-gradient(to top, #9795f0 0%, #fbc8d4 100%);    z-index: 999990;
    display: block;
}
element.style {
    font-size:20px;
}
 .container {
    margin-left: 75%;
  }
  p {
    display: block;
    color:black;
    margin-bottom: 0%;
    font-family: Arial Bold Italic;
    font-size:19;
}
.css-1cypcdb {
    position: relative;
    top: 2px;
background-image: linear-gradient(to bottom, #7028e4 30%, #e5b2ca 70%);    z-index: 999991;
    min-width: 244px;
    max-width: 550px;
    transform: none;
    transition: transform 300ms ease 0s, min-width 300ms ease 0s, max-width 300ms ease 0s;
}
.stButton button {
        background-color: green;
        color: white;
    }
img {
    overflow-clip-margin: content-box;
    overflow: clip;
    margin-left:2%;
}
.stButton button {
        background-color: red;
        color: white;
    }
img {
    overflow-clip-margin: content-box;
    overflow: clip;
    margin-left: 56%;
    margin-right:10%;
    margin-top:5%;
}
.css-1y4p8pa {
    width: 100%;
    margin-left: -10%;
    margin-right: -10%;
    padding-bottom:0%;
    margin-top: -1%;
    max-width: 80rem;
}
element.style {
    width: 1191px;
    height: 2299px;
}
</style>"""
streamlit.markdown(body,unsafe_allow_html=True)

def home_page():
    col1,col2 = streamlit.columns([0.5,1])
    with col1:
        streamlit.header('Fast & Secure to Stop Spamming')
        streamlit.subheader('A spam detector is a software program that is used to identify and filter out spam emails or sms.')
        left_col,right_Col,col1= streamlit.columns([0.5,0.5,1])
        streamlit.markdown(" ")
        with left_col:
            streamlit.button("Read More")
        with right_Col:
            streamlit.button("Conact Me")
    with col2:
        streamlit.image("pages\\spam.png", width=470)

    col3,col4=streamlit.columns([1,1])

    with col3:
        streamlit.header("About Spam Detector")
        streamlit.markdown("A spam detector is a software program that is used to identify and filter out spam emails. Spam is unsolicited or unwanted electronic messages that are typically sent in bulk. Spam detectors use a variety of techniques to identify spam.")
        streamlit.markdown("Spam detectors can be very effective at filtering out spam, but they are not perfect. Some spam messages may still get through, and some legitimate emails may be mistakenly identified as spam.")
        streamlit.markdown("If you are looking for a way to reduce the amount of spam in your email inbox, a spam detector is a good option. There are a number of different spam detectors available, so you can choose one that fits your needs and budget.")
    with col4:
        streamlit.image("pages\\about.png",width=300)
    # streamlit.write('If you are looking for a way to reduce the amount of spam in your email inbox, a spam detector is a good option.')
    streamlit.header(" ")
    streamlit.subheader(" ")
    with streamlit.container():
        col2,col4= streamlit.columns([0.5,1])
        with col2:
            streamlit.header('Get In Touch')
            streamlit.text_input('Your Name', key='name')
            streamlit.text_input('Your Email', key='email')
            streamlit.text_input('Your Phone', key='phone')
            streamlit.text_area('Message', key='message')
            if streamlit.button('Send'):
                # Code to handle sending the message goes here
                ststreamlit.write('Message sent successfully!')
        with col4:
            streamlit.image("pages\\contact.png",width=400)
    

if __name__ == '__main__':
    home_page()

streamlit.header(" ")
streamlit.header(" ")
streamlit.header(" ")
streamlit.header(" ")
streamlit.header(" ")

col_1,col_2,col_3 = streamlit.columns(3)
with col_1:
    col1,col2=streamlit.columns([1.2,1])
    with col1:
        streamlit.subheader("Address")
        streamlit.markdown(":triangular_flag_on_post: Location")
        streamlit.markdown(":e-mail: societyLens@gmail.com")
        streamlit.markdown(":telephone_receiver: +91-9844697440")
    with col2:
        streamlit.subheader("Links")
        # streamlit.markdown(":gogle:")
        streamlit.markdown(":ice_cube: Dashboard")
        streamlit.markdown(":gear: Setting")

with col_2:
    col_1,col_2= streamlit.columns([1,1])
    with col_1:
        streamlit.subheader(" Subscribe ")
        streamlit.text_input('Your Email')
        streamlit.button("Subscribe")
 




hide_st_style="""
<style>
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
</style>"""
streamlit.markdown(hide_st_style,unsafe_allow_html=True)



