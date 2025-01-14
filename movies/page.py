import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid
from movies.service import MoviesService
from genres.service import GenreService
from actors.service import ActorService


def show_movies():
    st.write("Lista de Arores/Atrizes")

    movie_service = MoviesService()
    movies = movie_service.get_movies()

    if movies:
        movies_df = pd.json_normalize(movies)
        AgGrid(
            key="movies_grid",
            data=movies_df[["title", "genre.name", "rate", "release_date", "resume"]],
            fit_columns_on_grid_load=True,
            height=400,
            # width=400,
        )
    else:
        st.warning("Nenhum filme encontrado.")

    st.title("Cadastrar novo filme")
    title = st.text_input("Titulo do filme")

    # Captura todos os generos
    genres = GenreService().get_genres()
    # Gera um dicionario com o nome (key) e o id (value)
    genres_name = {g["name"]: g["id"] for g in genres}
    # Captura a chave do dicionario (nome do gênero)
    selected_genre_name = st.selectbox(
        label="Selecione um gênero", options=(list(genres_name.keys()))
    )
    # Captura o id do gênero para ser adicionado na API
    genre_id = genres_name[selected_genre_name]

    actors = ActorService().get_actors()
    actors_name = {a["name"]: a["id"] for a in actors}
    selected_actor_names = st.multiselect(
        label="Selecione um ator/atrizes", options=(list(actors_name.keys()))
    )
    # Gera uma lista de atores e atrizes
    actors_ids = [actors_name[name] for name in selected_actor_names]

    release_date = st.date_input(
        label="Data de lançamento",
        value=datetime.today(),
        min_value=datetime(1800, 1, 1),
        format="DD/MM/YYYY",
    )

    resume = st.text_area("Sinopse", max_chars=200)

    if st.button("Cadastrar"):  # Se clicar: evento True
        try:
            new_movie = movie_service.create_movie(
                title=title,
                genre=genre_id,
                release_date=release_date,
                actors=actors_ids,
                resume=resume,
            )
            if new_movie:
                st.rerun()
        except Exception as e:
            if "Status code: 400" in str(e):
                st.error("Erro ao cadastrar o filme. Verifique os campos.")
            else:
                st.error(f"Erro inesperado: {str(e)}")
