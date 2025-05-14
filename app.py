import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, fetch_california_housing

# ============================================
# Visualizador de Dataset com Pandas e Streamlit
# ============================================
# Autor: Gustavo Rodrigues Ribeiro
# Descrição: Este é um aplicativo interativo desenvolvido com
# **Pandas**, **Seaborn**, **Matplotlib** e **Streamlit**. Ele
# permite a análise exploratória de dados com uma interface intuitiva
# e acessível diretamente pelo navegador.
# ============================================

# Configuração inicial da página do Streamlit
st.set_page_config(page_title="Visualizador de Dataset", layout="wide")

# Título da aplicação
st.title("Visualizador de Dataset com Pandas e Streamlit")

# Instruções para o usuário
st.markdown("""
Esta aplicação permite que você:
- Faça upload de arquivos CSV ou Excel;
- Visualize os dados em formato de tabela;
- Gere estatísticas descritivas básicas (média, mediana, desvio padrão, entre outros);
- Crie gráficos (histograma, scatter plot, box plot);
- Filtre dados com base em colunas numéricas.

Utilize os datasets de exemplo (Iris ou California Housing) ou envie seu próprio arquivo.
""")

# Opção de escolha do tipo de dataset
st.sidebar.header("Escolha o tipo de dataset")
tipo_arquivo = st.sidebar.radio("Tipo de Dataset:", ["Upload Manual", "Iris", "California Housing"])

# Inicializa o DataFrame vazio
df = None

# Carregamento do dataset conforme a opção escolhida
if tipo_arquivo == "Upload Manual":
    # Upload de arquivo CSV ou Excel
    arquivo = st.sidebar.file_uploader("Faça o upload de um arquivo CSV ou Excel:", type=["csv", "xlsx"])
    if arquivo is not None:
        if arquivo.name.endswith(".csv"):
            df = pd.read_csv(arquivo)
        else:
            df = pd.read_excel(arquivo)
elif tipo_arquivo == "Iris":
    # Carrega o dataset Iris a partir da sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame
elif tipo_arquivo == "California Housing":
    # Carrega o dataset California Housing
    housing = fetch_california_housing(as_frame=True)
    df = housing.frame

# Processamento do dataset após carregamento
if df is not None:
    st.subheader("🧾 Prévia dos Dados")
    st.dataframe(df)

    # Estatísticas descritivas
    st.subheader("📈 Estatísticas Descritivas para Dados Prévios")
    st.write(df.describe())

    df_filtrado = df.copy()

    # Colunas do DataFrame ou .csv
    colunas_numericas = df_filtrado.select_dtypes(include=['float64', 'int64']).columns
    colunas_categoricas = df_filtrado.select_dtypes(include=['object', 'category']).columns
    colunas_string = df_filtrado.select_dtypes(include=['object']).columns

    # Filtragem de dados em faixa de valores para colunas numéricas
    # -------------------------------------------------
    st.sidebar.subheader("📉 Filtros numéricos")
    filtros = {}

    # Criação e aplicação de sliders para filtrar valores em colunas numéricas
    for col in colunas_numericas:
        min_val, max_val = float(df_filtrado[col].min()), float(df_filtrado[col].max())
        valores = st.sidebar.slider(f"Filtro para {col}", min_val, max_val, (min_val, max_val))
        filtros[col] = valores
    
    # Aplica os filtros ao DataFrame
    for col, (min_val, max_val) in filtros.items():
        df_filtrado = df_filtrado[(df_filtrado[col] >= min_val) & (df_filtrado[col] <= max_val)]

    # -------------------------------------------------


    # Filtros categóricos
    # -------------------------------------------------
    st.sidebar.subheader("🧩 Filtros categóricos")

    # Criação e aplicação de caixas de seleção para filtrar valores em colunas categóricas
    for coluna in colunas_categoricas:
        opcoes = df_filtrado[coluna].dropna().unique().tolist()
        selecionados = st.sidebar.multiselect(f"{coluna}", opcoes, default=opcoes)
        df_filtrado = df_filtrado[df_filtrado[coluna].isin(selecionados)]
    # -------------------------------------------------


    # Filtros textuais
    # -------------------------------------------------
    st.sidebar.subheader("🔍 Busca por texto (colunas textuais)")

    # Criação e aplicação de caixas de texto para filtrar valores em colunas textuais
    if len(colunas_string) > 0:
        coluna_busca = st.sidebar.selectbox("Coluna para busca:", colunas_string)
        valores_possiveis_texto = df[coluna_busca].dropna().unique()
        termo_busca = st.sidebar.selectbox(f"Termo a buscar em '{coluna_busca}':", valores_possiveis_texto, key="valor_unico_texto")
        if st.sidebar.button("Aplicar filtro por texto"):
            df_filtrado = df_filtrado[df_filtrado[coluna_busca].str.contains(termo_busca, case=False, na=False)]
    # -------------------------------------------------


    # ----------------------------------------------
    # Filtro por valor único em colunas numéricas
    st.sidebar.subheader("🔢 Filtro por valor único (colunas numéricas)")
    coluna_valor_unico = st.sidebar.selectbox("Escolha a coluna numérica:", colunas_numericas, key="valor_unico_col")
    
    if coluna_valor_unico:
        valores_possiveis = df[coluna_valor_unico].dropna().unique()
        valores_possiveis.sort()
        valor_escolhido = st.sidebar.selectbox(f"Escolha o valor para '{coluna_valor_unico}':", valores_possiveis, key="valor_unico_val")
        
        if st.sidebar.button("Aplicar filtro por valor único"):
            df_filtrado = df_filtrado[df_filtrado[coluna_valor_unico] == valor_escolhido]
    # ----------------------------------------------


    # Exibe os dados filtrados
    st.subheader("📂 Dados Filtrados")
    st.dataframe(df_filtrado)

    # Estatísticas descritivas
    st.subheader("📈 Estatísticas Descritivas para Dados Filtrados")
    st.write(df_filtrado.describe())

    # Geração de gráficos
    st.subheader("📈 Visualização Gráfica")
    tipo_grafico = st.selectbox("Escolha o tipo de gráfico:", ["Histograma", "Scatter Plot", "Box Plot"])

    # Histograma: distribuição de uma única variável
    if tipo_grafico == "Histograma":
        col = st.selectbox("Escolha a coluna:", df_filtrado.columns)
        fig, ax = plt.subplots()
        sns.histplot(df_filtrado[col], kde=True, ax=ax)
        ax.set_title(f"Histograma de {col}")
        plt.tight_layout()
        ax.tick_params(axis='x', rotation=90)
        st.pyplot(fig)

    # Scatter Plot: relação entre duas variáveis
    elif tipo_grafico == "Scatter Plot":
        x = st.selectbox("Eixo X:", df_filtrado.columns, key="x")
        y = st.selectbox("Eixo Y:", df_filtrado.columns, key="y")
        fig, ax = plt.subplots()
        sns.scatterplot(x=df_filtrado[x], y=df_filtrado[y], ax=ax)
        ax.set_title(f"Scatter Plot entre {x} e {y}")
        st.pyplot(fig)

    # Box Plot: distribuição estatística de uma variável
    elif tipo_grafico == "Box Plot":
        col = st.selectbox("Escolha a coluna:", df_filtrado.columns)
        fig, ax = plt.subplots()
        sns.boxplot(y=df_filtrado[col], ax=ax)
        ax.set_title(f"Box Plot de {col}")
        st.pyplot(fig)

else:
    # Aviso caso nenhum dataset tenha sido carregado
    st.warning("Por favor, envie um arquivo válido ou selecione um dataset de exemplo no menu lateral.")