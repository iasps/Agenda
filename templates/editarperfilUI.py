import streamlit as st
from views import View

class EditarPerfilUI:
    def main():
        st.header("Editar perfil")
        EditarPerfilUI.editar()

    def editar():
        op = View.cliente_listar_id(st.session_state["cliente_id"])
        nome = "admin"
        if op.get_nome() != "admin":
            nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        fone = st.text_input("Informe o novo fone", op.get_fone())
        senha = st.text_input("Informe a nova senha")
        if st.button("Editar"):
            id = op.get_id()
            View.cliente_editar(id, nome, email, fone, senha)
            st.success("Perfil atualizado com sucesso")