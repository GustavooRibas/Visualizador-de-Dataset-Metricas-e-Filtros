# Visualizador de Dataset com Pandas e Streamlit

## Autor: Gustavo Rodrigues Ribeiro

Este é um aplicativo interativo desenvolvido com **Pandas**, **Seaborn**, **Matplotlib** e **Streamlit**. Ele permite a análise exploratória de dados com uma interface intuitiva e acessível diretamente pelo navegador.

---

## Funcionalidades

- **Upload de arquivo** (CSV ou Excel)
- **Carregamento de datasets de exemplo**: Iris e California Housing
- **Visualização dos dados em tabela**
- **Estatísticas descritivas** (média, mediana, desvio padrão, etc.)
- **Filtragem interativa por:**
  - Faixa de valores
  - Texto
  - Valor único
  - Categoria
- **Geração de três tipos de gráficos**:
  - Histograma
  - Scatter Plot
  - Box Plot

---

## Como Executar o Projeto

Certifique-se de que você possui o Python instalado (recomendado Python 3.10+).

No repositório do projeto:

### 1. Crie um ambiente virtual (opcional, mas recomendado)

Criando ambiente virtual:

```bash
python -m venv venv
```

Acessando ambiente virtual:

Em Sistemas Unix:

```bash
source venv/bin/activate
```

Em Sistemas Windows (CMD):

```bash
venv\Scripts\activate
```

### 2. Instale as dependências

Utilize o arquivo `requirements.txt` incluso:

```bash
pip install -r requirements.txt
```

### 3. Execute a aplicação

```bash
streamlit run app.py
```

A aplicação será aberta automaticamente no navegador padrão.

---

## Sobre os Datasets

- **Iris Dataset**: Dataset clássico de classificação de flores, com quatro atributos numéricos.
- **California Housing**: Dataset sobre preços de casas na California.

Ambos estão disponíveis diretamente via `sklearn.datasets`.

---

## 📄 requirements.txt

```txt
streamlit>=1.30.0
pandas>=2.2.0
matplotlib>=3.8.0
seaborn>=0.13.0
scikit-learn>=1.4.0
openpyxl>=3.1.0
```

---

## 💡 Objetivo

Este projeto foi desenvolvido como parte de um **exercício técnico de processo seletivo** para demonstrar habilidades em:

- Manipulação e análise de dados com Pandas
- Desenvolvimento de interfaces com Streamlit
- Visualização de dados com Seaborn e Matplotlib
- Boas práticas de codificação, organização e documentação