import pandas as pd
import streamlit as st
# import plotly.express as px
from database import view_all_data
def read():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['criminal_id','weight', 'eye_color', 'age', 'height', 'gender' , 'national_origin' , 'mother_toungue' , 'body_marks','body_build','criminal_name','address','phonenumber','case_id','past_history_id'])
    with st.expander("View all Criminals"):
        st.dataframe(df)
