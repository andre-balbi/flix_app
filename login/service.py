import streamlit as st
from api.service import Auth


def login(username, password):
    auth = Auth()
    response = auth.get_token(username, password)
    if response.get("error"):
        st.error(f' Failed to login: {response.get("error")}')
    else:
        st.session_state.token = response.get("access")
        st.rerun()
        return response.get("access")


# Limpando todas as chaves salvas no session_state
def logout():
    for i in st.session_state:
        del st.session_state[i]
    st.rerun()
