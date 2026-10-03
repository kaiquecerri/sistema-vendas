import streamlit as st
import pandas as pd
import plotly.express as px

tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")

#FORMULARIO DE CADASTRO

st.sidebar.write("## Cadastrar Venda")

data = st.sidebar.date_input("Data da venda", max_value="today")
vendedor =  st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook","Celular","Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor", 0)
cadastrar = st.sidebar.button("Cadastrar Venda")

## FUNCAO DO BOTAO

if cadastrar:
    erro_cadastrar = False

    if quantidade <= 0:
        st.error("O campo 'Quantidade' precisa ser maior que 0")
        erro_cadastrar = True
    
    if valor <= 0:
        st.error("O campo 'Valor' precisa ser maior que 0")
        erro_cadastrar = True

    if not erro_cadastrar:
        nova_venda = [str(data),vendedor,produto,quantidade,valor]
        ultima_linha = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("vendas.csv", index=False)
        st.success("Venda cadastrada")


#TABELA DE VENDAS

st.write("## Vendas Cadastradas")

st.dataframe(tabela_vendas)

#DASHBOARD (GRAFICOS)

st.write("## Dashboard")

faturamento_total  = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento_total}")

grafico_barra = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico_barra)

grafico_pizza = px.pie(tabela_vendas, names="produto", values="valor", hole=0.4)
st.plotly_chart(grafico_pizza)
