import streamlit as st
import plotly.express as px
from movies.service import MoviesService


def show_home():
    st.title("Estatística de Filmes")

    movies_service = MoviesService()
    movies_stats = movies_service.get_movie_stats()

    if len(movies_stats["movies_by_genre"]) > 0:
        st.subheader("Filmes por Gênero")
        fig = px.pie(
            movies_stats["movies_by_genre"],
            values="count",
            names="genre__name",
            title="Filmes por Gênero",
            color_discrete_sequence=px.colors.sequential.RdBu,
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Total de Filmes")
    st.write(movies_stats["total_movies"])

    st.subheader("Total de Avaliações por Gênero")
    for i in movies_stats["movies_by_genre"]:
        st.write(f"{i['genre__name']}: {i['count']}")

    st.subheader("Média de Avaliações")
    st.write(round(movies_stats["average_total_stars"], 1))
