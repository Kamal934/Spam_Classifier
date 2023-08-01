import streamlit as st
# Giving a title 
st.set_page_config(page_title='Registration_page', page_icon=':heart_decoration:')

custom="""<style>
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
    background-image: linear-gradient(to top, #9795f0 0%, #fbc8d4 100%);    z-index: 999990;
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
    .st-dn {
    padding-left: 8px;
    color:black;

}
.st-do {
    padding-left: 8px;
    color:black;

}
p {
    display: block;
    margin-bottom: 0%;
    font-family: 'Ubuntu',sans-serif;
    font-weight: bold;
}
</style>
"""

st.markdown(custom,unsafe_allow_html=True)
st.title('Registration Form')

# creating a form
my_form=st.form(key='form-1')
# creating input fields
fname=my_form.text_input('First Name:')
lname=my_form.text_input('Last Name:')
email=my_form.text_input('Email:')
# creating radio button 
gender=my_form.radio('Gender',('Male','Female'))
# creating slider 
age=my_form.slider('Age:',1,60)
# creating date picker
bday=my_form.date_input('Enter Birthdate:')
# creating a text area
address=my_form.text_area('Enter Address:')
# creating a submit button
submit=my_form.form_submit_button('Submit')
# the following gets updated after clicking on submit, printing the details of the fields that are submitted in the form
st.write('Name is '+fname+' '+lname)
st.write('Email is '+email)
st.write('Gender is '+gender)
st.write('Age is '+str(age))
st.write('Birthday is '+str(bday))
st.write('Address is '+address)
