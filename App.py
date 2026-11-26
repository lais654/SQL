import streamlit as st 
import Banco

st.title("Hortifruti")
st.write("Cadastro de Produtos")

with st.form("cadastro", clear_on_submit=True):
    st.text_imput("Nome do Produto")
    categoria=st.selectbox("Categoria", ["Fruta", "Verdura", "Legume"])
    preco = st.number_imput("Preço R$", min_value=0.0, step=0.50)
    envuar = st.form_submit_button("Cadastrar")

#Verificação de Erro
if enviar:
    if nome == "":
        st.warning("Digite o nome do produto")
    else:
        banco.cadastrar(nome, categoria, preco)
        st.success("Cadastrado")
        