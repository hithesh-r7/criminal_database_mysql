import streamlit as st
from create import create
from database import create_table
from delete import delete
from read import read
from update import update

def main():
    st.title("Project")
    menu = ["Add", "View", "Edit", "Remove"]    #add a home page for project
    choice = st.sidebar.selectbox("Menu", menu)
    #create_table()
    if choice == "Add":
        st.subheader("Enter Criminal Details:")
        create()
    elif choice == "View":
        st.subheader("View Criminals")
        read()
    elif choice == "Edit":
        st.subheader("Update Criminals")
        update()
    elif choice == "Remove":
        st.subheader("Delete Criminals")
        delete()
    else:
        st.subheader("About Criminal")

if __name__ == '__main__':
    main()
