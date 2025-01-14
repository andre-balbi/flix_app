import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid
from actors.service import ActorService


def show_actors():
    st.write("Lista de Arores/Atrizes")

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actors_df = pd.DataFrame(actors)

    if actors:
        AgGrid(
            key="actors_grid",
            data=actors_df[["name", "birthday", "nationality"]],  # Não mostra ID
            fit_columns_on_grid_load=True,
            height=400,
            # width=400,
        )
    else:
        st.warning("Nenhum ator/atrizes encontrado.")

    st.title("Cadastrar novo ator/atrizes")
    name = st.text_input("Nome do ator/atrizes")
    birthday = st.date_input(
        label="Data de nascimento",
        value=datetime.today(),
        min_value=datetime(1850, 1, 1),
        max_value=datetime.today(),
        format="DD/MM/YYYY",
    )
    NATIONALITY_DROPDOWN = [
        "United States",
        "Canada",
        "Mexico",
        "Spain",
        "France",
        "Italy",
        "Germany",
        "United Kingdom",
        "Australia",
        "Japan",
        "China",
        "Brazil",
        "Lebanon",
    ]

    nationality = st.selectbox(label="Nacionalidade", options=NATIONALITY_DROPDOWN)

    if st.button("Cadastrar"):  # Se clicar: evento True
        try:
            new_actor = actor_service.create_actor(
                name=name, birthday=birthday, nationality=nationality
            )
            if new_actor:
                st.rerun()
        except Exception as e:
            if "Status code: 400" in str(e):
                st.error("Erro ao cadastrar ator/atrizes. Verifique os campos.")
            else:
                st.error(f"Erro inesperado: {str(e)}")
