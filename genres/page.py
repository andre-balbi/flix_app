from genres.service import GenreService
import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


def show_genres():
    st.header("Gêneros de Filmes")

    genre_service = GenreService()  # <--- Adicionado
    genres = genre_service.get_genres()  # <--- Adicionado
    genres_df = pd.DataFrame(genres)

    if genres:
        AgGrid(
            # read_data=True,
            key="genres_grid",
            data=genres_df,
            fit_columns_on_grid_load=True,
            height=400,
            # width=400,
        )
    else:
        st.warning("Nenhum gênero encontrado.")

    st.title("Cadastrar novo gênero")
    name = st.text_input("Nome do gênero")

    if st.button("Cadastrar"):  # Se clicar: evento True
        new_genre = genre_service.create_genre(name)  # <--- Adicionado
        if new_genre:  # <--- Adicionado
            st.rerun()
        else:
            st.error("Erro ao cadastrar gênero. Verifique os campos.")
    # -----------------------------------------------------------------------------#
    # # Barra de pesquisa
    # search = st.text_input("Pesquisar gênero", "")

    # # Filtrar gêneros
    # filtered_genres = [g for g in genres if search.lower() in g["name"].lower()]

    # # Exibir tabela com estilo
    # genres_df = pd.DataFrame(filtered_genres, columns=["id", "name"])
    # st.dataframe(
    #     genres_df,
    #     column_config={"id": "ID", "name": "Nome do Gênero"},
    #     hide_index=True,
    #     use_container_width=True,
    #     # width=200,
    # )

    # # Mostrar estatísticas
    # st.caption(f"Total de gêneros: {len(filtered_genres)}")
