import streamlit as st
import requests
from login.service import logout


class ReviewsRepository:
    def __init__(self):
        self.__base_url = "https://drebalbi.pythonanywhere.com/api/v1/"
        self.__reviews_url = f"{self.__base_url}reviews/"
        self.__headers = {"Authorization": f"Bearer {st.session_state.token}"}

    def get_reviews(self):
        response = requests.get(self.__reviews_url, headers=self.__headers)
        if response.status_code == 200:  # 200 = Get OK
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            "Failed to get reviews. Status code: " + str(response.status_code)
        )

    def create_review(self, review):
        response = requests.post(
            self.__reviews_url, headers=self.__headers, data=review
        )
        if response.status_code == 201:  # 201 = criada com sucesso!
            return response.json()
        if response.status_code == 401:
            logout()
            return None
        raise Exception(
            "Failed to get reviews. Status code: " + str(response.status_code)
        )
