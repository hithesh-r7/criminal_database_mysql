import pandas as pd
import streamlit as st
from database import view_all_data, view_only_criminal_names, get_criminal,edit_criminal_data
def update():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['criminal_id','weight', 'eye_color', 'age', 'height', 'gender' , 'national_origin' , 'mother_toungue' , 'body_marks','body_build','criminal_name','address','phonenumber','case_id','past_history_id'])
    with st.expander("Existing Criminals"):
        st.dataframe(df)
    list_of_criminals = [i[0] for i in view_only_criminal_names()]
    selected_result = st.selectbox("Criminal data to Edit", list_of_criminals)
    col1, col2,col3 = st.columns(3)
    with col1:
       # new_criminal_id = st.text_input("Criminal id :")
        new_criminal_name = st.text_input("Criminal Name :")
        new_weight = st.number_input("Weight :")
        new_age = st.number_input("Age : ")
        new_phonenumber = st.number_input('mobile :')
    with col2:
        new_eye_color = st.selectbox("Color of eye", ["Black", "Blue", "Green","Brown"])
        new_gender = st.selectbox("Gender", ["Male", "Female", "Don't want to specify"])
        new_height = st.number_input("Height :")
        new_national_origin = st.text_input("Nationality :")
    with col3:
        new_mother_toungue = st.text_input("Mother tongue :")
        new_body_marks = st.text_input("Desc body marks if any :")
        new_body_build = st.text_input("body build")
        new_address = st.text_input("Enter address :")
        new_case_id=st.number_input("Case id:")
        new_past_history_id=st.number_input("PastHistory id:")
    if st.button("Update Criminal Data"):
        edit_criminal_data(selected_result, new_weight, new_eye_color, new_age, new_height, new_gender , new_national_origin , new_mother_toungue , new_body_marks,new_body_build,new_criminal_name,new_address,new_phonenumber,new_case_id,new_past_history_id)
    st.success("Successfully updated:: {}".format(selected_result))
    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['criminal_id','weight', 'eye_color', 'age', 'height', 'gender' , 'national_origin' , 'mother_toungue' , 'body_marks','body_build','criminal_name','address','phonenumber','case_id','past_history_id'])
    with st.expander("Updated data"):
        st.dataframe(df2)