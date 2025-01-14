import streamlit as st
import pandas as pd
from reviews.service import ReviewsService
from movies.service import MoviesService
from st_aggrid import AgGrid


def show_reviews():
    st.write("Lista de reviews")
    reviews_service = ReviewsService()
    reviews = reviews_service.get_reviews()

    if reviews:
        reviews_df = pd.json_normalize(reviews)
        # O dataframe retorna o numero do filme e nao o nome
        # # Substituir os valores na coluna 'movie' pelos valores do dicionário
        movies_service = MoviesService().get_movies()
        # Dicionario com os filmes {ïd:nome}
        movies_dict = {i["id"]: i["title"] for i in movies_service}
        # Substituir os valores na coluna 'movie' pelos valores do dicionário
        reviews_df["movie"] = reviews_df["movie"].map(movies_dict)

        AgGrid(
            key="reviews_grid",
            data=reviews_df[["movie", "stars", "comment"]],
            fit_columns_on_grid_load=True,
            height=400,
            # width=400,
        )
    else:
        st.warning("Nenhum filme encontrado.")

    st.title("Cadastrar nova avaliação")

    movie_service = MoviesService()
    movies = movie_service.get_movies()
    movie_name = {m["title"]: m["id"] for m in movies}
    selected_movie_name = st.selectbox(
        label="Selecione um gênero", options=(list(movie_name.keys()))
    )
    movie_id = movie_name[selected_movie_name]

    stars = st.slider("Avaliação", min_value=0, max_value=5, value=3)

    comment = st.text_input("Comentario", max_chars=200)

    if st.button("Cadastrar"):  # Se clicar: evento True
        try:
            new_review = reviews_service.create_review(
                movie=movie_id, stars=stars, comment=comment
            )
            if new_review:
                st.rerun()
        except Exception as e:
            if "Status code: 400" in str(e):
                st.error("Erro ao cadastrar o filme. Verifique os campos.")
            else:
                st.error(f"Erro inesperado: {str(e)}")
