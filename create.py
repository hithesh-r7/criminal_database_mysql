import streamlit as st
from database import add_data
def create():
    col1, col2, col3 = st.columns(3)
    with col1:
        
        criminal_id = st.text_input("Criminal id :")
        criminal_name = st.text_input("Criminal Name :")
        weight = st.number_input("Weight :")
        age = st.number_input("Age : ")
        phonenumber = st.number_input('mobile :')
    with col2:
        eye_color = st.selectbox("Color of eye", ["Black", "Blue", "Green","Brown"])
        gender = st.selectbox("Gender", ["Male", "Female", "Don't want to specify"])
        height = st.number_input("Height :")
        national_origin = st.text_input("Nationality :")
    with col3:
        mother_toungue = st.text_input("Mother tongue :")
        body_marks = st.text_input("Desc body marks if any :")
        body_build = st.text_input("body build")
        address = st.text_input("Enter address :")
        case_id=st.number_input("Case id:")
        past_history_id=st.number_input("PastHistory id:")

    if st.button("Add Criminal"):
        add_data(criminal_id, weight, eye_color, age, height, gender , national_origin , mother_toungue , body_marks,body_build,criminal_name,address,phonenumber,case_id,past_history_id)
        st.success("Successfully added crminal with id: {}".format(criminal_id))
