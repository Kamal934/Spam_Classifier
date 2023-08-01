import streamlit as st

st.set_page_config(page_title='Profile_page', page_icon=':male-office-worker:')

body="""
<style>
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
p {
    display: block;
    color: black;
    width:100px;
    margin-left: 10%;
    font-family: 'Ubuntu',sans-serif;
    font-weight: bold;
}
.stButton button {
        border:0;
        background-color: green;
        color: white;
        align-items:center;
    }
</style>"""
st.markdown(body,unsafe_allow_html=True)
def main():
    st.title("Profile Page")


    # st.write("Your profile information:")
    col1,col2= st.columns(2)
    with st.container():
        with col1:
        # Profile picture and basic info
            st.image("pages\\man.png", width=130)
            st.markdown("@kml_12")
            # st.markdown("deepkamal@gmail.com")
        with col2:
            col_1,col_2,col_3= st.columns([0.4,0.4,0.4])
            with col_1:
        # Friends, Photos, and Comments
                st.subheader(345)
                st.subheader("Friends")
            with col_2:
                st.subheader(43)
                st.subheader("Photos")
            with col_3:
                st.subheader(4546)
                st.subheader("Comments")
            st.button("Edit Profile")

    with st.container():
        # Profile settings form
        st.header("Profile Settings")
        st.subheader("Personal Information")
        username = st.text_input("Username")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        dob = st.date_input("Date of Birth")

        st.subheader("Contact Information")
        mobile = st.text_input("Mobile Number")
        address = st.text_input("Address Line")
        postcode = st.text_input("Postcode")
        state = st.text_input("State")
        country = st.text_input("Country")
        email = st.text_input("Email ID")
        education = st.text_input("Education")
    
    with st.container():
        # Experience form
        st.header("Experience")
        experience_ml = st.text_input("Experience in Machine Learning")
        additional_details = st.text_input("Additional Details")

       
    # Save Profile button
        if st.button("Save Profile ", key="save_button"):
            st.success("Profile saved successfully!")

if __name__ == "__main__":
    main()

hide_st_style="""
<style>
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
</style>"""
st.markdown(hide_st_style,unsafe_allow_html=True)


