import streamlit 
import pickle
from nltk.corpus import stopwords
import nltk 
import string
from nltk.stem.porter import PorterStemmer
ps=PorterStemmer()
from sklearn.metrics import  accuracy_score,confusion_matrix,precision_score
import sklearn.metrics as metrics
streamlit.set_page_config(page_title='Testing_page', page_icon=':brain:')

custom_colr="""
<style>
.css-ffhzg2 {
    position: absolute;
    background-image: linear-gradient(to bottom, #c71d6f 0%, #d09693 100%);
    overflow: hidden;
}
h1 {
    color: black;
    font-size: 36px;
  }
h2 {
    color: black;
    font-size: 30px;
  }
 h3 {
    color: black;
    font-size: 30px;
  }
  .css-1avcm0n {
    position: fixed;
    border:0;
    top: 0px;
    left: 0px;
    right: 0px;
    height: 2rem;
    background-image: linear-gradient(to top, #c71d6f 0%, #d09693 100%);
    z-index: 999990;
    display: block;
}
 .container {
    margin-left: 75%;
  }
  p {
    display: block;
    color:black;
    margin-bottom: 0%;
    font-family: sans-serif,14;
}
.css-1cypcdb {
    position: relative;
    top: 2px;
    background-image: linear-gradient(to bottom, #c71d6f 30%, #d09693 70%);
    transform: none;
    transition: transform 300ms ease 0s, min-width 300ms ease 0s, max-width 300ms ease 0s;
}
.stButton button {
        background-color: green;
        color: white;
    }
    .st-dn {
    padding-left: 8px;
    color:black;
}
.st-do {
    padding-left: 8px;
    color:black;
}
</style>
"""
streamlit.markdown(custom_colr,unsafe_allow_html=True)

def transfer_text(text):

    text=text.lower()

    text=nltk.word_tokenize(text)
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text=y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    
    return " ".join(y)

tfidf=pickle.load(open("Sms\\vectorizer.pkl",'rb'))
model_1 = pickle.load(open("Sms/model.pkl",'rb'))

streamlit.title('Email Spam Classifier')
input_Sms= streamlit.text_input('Enter the message')
option= streamlit.selectbox("you Got message from:",["via email","via sms"])

if streamlit.checkbox('check me'):
    # Add the desired functionality when the checkbox is checked
    streamlit.write("The checkbox is checked!")
else:
    # Add the desired functionality when the checkbox is not checked
    streamlit.write("The checkbox is not checked.")
    
if streamlit.button("click to predict"):
    transform_Sms= transfer_text(input_Sms)
    vector_input=tfidf.transform([transform_Sms])
    result = model_1.predict(vector_input)[0]
    print(result)
    if input_Sms == '':
        streamlit.header("Please Enter the Mail or Sms ")
    elif (result == 1):
        streamlit.header(":skull: spam")
    else:
        streamlit.header("ham")




hide_st_style="""
<style>
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
</style>"""
streamlit.markdown(hide_st_style,unsafe_allow_html=True)