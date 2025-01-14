from actors.repository import ActorsRepository
import streamlit as st


class ActorService:
    def __init__(self):
        self.actor_repository = ActorsRepository()

    def get_actors(self):
        # Verifica se 'actors' ja existe no session state para evitar chamadas de API redundantes.
        if "actors" in st.session_state:
            # Se 'actors' existir, retorna imediatamente.
            return st.session_state.actors
        # Caso contrario, chama o repositorio para buscar os atores da API.
        actors = self.actor_repository.get_actors()
        # Armazena os atores buscados no session state para futuras requisicoes.
        st.session_state.actors = actors
        # Retorna os atores buscados recentemente.
        return actors

    def create_actor(self, name, birthday, nationality):
        # Cria um dicionario com as informacoes do ator.
        actor = dict(name=name, birthday=birthday, nationality=nationality)
        # Chama o repositorio para criar o ator na API.
        new_actor = self.actor_repository.create_actor(actor)
        # Adiciona o ator recem criado na lista de atores do session_state.
        st.session_state.actors.append(new_actor)
        # Retorna o ator criado recentemente.
        return new_actor
