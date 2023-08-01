import streamlit as st
from PIL import Image
st.set_page_config(page_title='Login_page', page_icon=':bulb:')

custom_css="""
<Style>
/* custom.css */
body {
    display: block;
    position:fiexed;
    margin: 18px;
}
/* header  */
.css-1avcm0n {
  position: fixed;
  top: 0px;
  left: 0px;
  right: 0px;
  height: 2.875rem;
  background-image: linear-gradient(to bottom, #a18cd1 0%, #fbc2eb 100%);
  outline: none;
  z-index: 999990;
  display: block;
}
/* sidebar button*/
.css-aw8l5d {
  position: fixed;
  top: 0.5rem;
  left: 0.25rem;
  z-index: 999990;
  transition: left 300ms ease 0s;
  color: rgb(0, 0, 0);
}
/* sidebar expanded */
.css-1cypcdb {
  position: relative;
  /* top: 2px; */
  background-image: linear-gradient(to left, #cd9cf2 10%, #f6f3ff 90%);  /* max-width: 550px; */
  /* transform: none; */
  transition: transform 300ms ease 0s, min-width 300ms ease 0s, max-width 300ms ease 0s;
}
/* sidebar pages */
style attribute {
  position: relative;
  user-select: auto;
  width: 244px;
  height: 792px;
  box-sizing: border-box;
  flex-shrink: 0;
}
/* page color change */
.css-1m6wrpk {
  color: rgba(0, 0, 0, 1);
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
  display: table-cell;
}
.css-1we6k59:active, .css-1we6k59:visited, .css-1we6k59:hover {
  text-decoration: none;
  font-weight: 500;
  font-style: oblique;
}
.css-lrlib {
  max-height: 100vh;
  list-style: none;
  overflow: overlay;
  margin: 0px;
  padding-top: 6rem;
  padding-bottom: 1rem;
}
ul {
  display: block;
  list-style-type: disc;
  margin-block-start: 1em;
  margin-block-end: 1em;
  margin-inline-start: 0px;
  margin-inline-end: 0px;
  padding-inline-start: 40px;
}
/* right body */
.css-ffhzg2 {
    position: absolute;
    background-image: linear-gradient(to top, #a18cd1 0%, #fbc2eb 100%);
    color: rgb(0, 0, 0);
    inset: 0px;
    overflow: hidden;
}
.css-1y4p8pa {
    width: 100%;
    margin-left: -10%;
    margin-right: -10%;
    margin-top: -1%;
    max-width: 40rem;
}
.css-ocqkz7 {
    display: flex;
    flex-wrap: wrap;
    width: 100%;
    /* -webkit-box-flex: 3; */
    flex-grow: 1;
    -webkit-box-align: stretch;
    align-items: stretch;
    gap: 1rem;
}
.css-11b19b {
    width: 500px;
    # margin:20%;
    position: relative;
    display: flex;
    gap: 1rem;
}
h2{  
    color: black;
    }
p {
    display: block;
    margin-bottom: 0%;
    color:black;
    font-family: 'Ubuntu',sans-serif;
    font-weight: bold;
}
.stButton button {
    background-color: red;
    color: white;
}</style>"""
st.markdown(custom_css, unsafe_allow_html=True)
# Create an empty container
placeholder = st.empty()

actual_email = "email"
actual_password = "password"
# Insert a form in the container
with placeholder.form("login "):
    
    st.markdown("## Enter Your Credentials")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    submit = st.form_submit_button("Login")

if submit and email == actual_email and password == actual_password:
    # If the form is submitted and the email and password are correct,
    # clear the form/container and display a success message
    st.success("Login successful")
    # Read the content of the file "Homepage.py"
    placeholder.empty()
  

    # st.experimental_set_query_params(page="Dasboard")
elif submit and email != actual_email and password != actual_password:
    st.error("Login failed")
else:
    # If the user does not have an account, move them to the registration page
    st.write("You do not have an account. Would you like to create one?")
    st.button("Create Account")
    # Read the content of the file "Homepage.py"
    # with open("registration.py", "r") as file:
    #     markdown_content = file.read()
    #     st.markdown(markdown_content)




# markdown removwe
hide_st_style="""
<style>
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
</style>"""
st.markdown(hide_st_style,unsafe_allow_html=True)