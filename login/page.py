import streamlit as st
from login.service import login


def show_login():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input(
        "Password", type="password"
    )  # type="password" para ocultar a senha

    if st.button("Login"):  # Se clicar: evento True
        login(username, password)
