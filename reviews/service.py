import streamlit as st
from reviews.repository import ReviewsRepository


class ReviewsService:
    def __init__(self):
        self.__repository = ReviewsRepository()

    def get_reviews(self):
        if "reviews" in st.session_state:
            return st.session_state.reviews
        reviews = self.__repository.get_reviews()
        st.session_state.reviews = reviews
        return reviews

    def create_review(self, movie, stars, comment):
        review = dict(movie=movie, stars=stars, comment=comment)
        new_review = self.__repository.create_review(review)
        st.session_state.reviews.append(new_review)
        return new_review
