import pandas as pd
import streamlit as st
from database import view_all_data, view_only_criminal_names, delete_data
def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['criminal_id','weight', 'eye_color', 'age', 'height', 'gender' , 'national_origin' , 'mother_toungue' , 'body_marks','body_build','criminal_name','address','phonenumber','case_id','past_history_id'])
    with st.expander("Current data"):
        st.dataframe(df)
    list_of_criminals = [i[0] for i in view_only_criminal_names()]
    selected_criminal = st.selectbox("Criminal file to Delete", list_of_criminals)
    st.warning("Do you want to delete ::{}".format(selected_criminal))
    if st.button("Delete Criminal"):
        delete_data(selected_criminal)
    st.success("Criminal has been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['criminal_id','weight', 'eye_color', 'age', 'height', 'gender' , 'national_origin' , 'mother_toungue' , 'body_marks','body_build','criminal_name','address','phonenumber','case_id','past_history_id'])
    with st.expander("Updated data"):
        st.dataframe(df2)
