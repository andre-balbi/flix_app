import streamlit as st
from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews
from login.page import show_login
from home.page import show_home


def main():
    # Verifica se a funcao ja esta logada
    if "token" not in st.session_state:
        show_login()
    else:

        st.title("Flix App")
        # Adicionando menu lateral
        menu_option = st.sidebar.selectbox(
            "Selecione uma opção",
            ["Inicio", "Genero", "Atores/Atrizes", "Filmes", "Avaliações"],
        )

        if menu_option == "Inicio":
            show_home()

        if menu_option == "Genero":
            show_genres()

        if menu_option == "Atores/Atrizes":
            show_actors()

        if menu_option == "Filmes":
            show_movies()

        if menu_option == "Avaliações":
            show_reviews()


if __name__ == "__main__":
    main()
