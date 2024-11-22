# Estatistica-Violencia-Rio-
Trabalho para a Aula de Linguagem Python lecionada pelo Prof. Raphael

# Análise de Dados de Violência no Rio de Janeiro - 2023

Este projeto utiliza **Python**, **Streamlit**, e **Flask** para analisar e visualizar dados de violência urbana no Rio de Janeiro em 2023. Ele inclui uma API que fornece estatísticas básicas e um front-end interativo para explorar visualizações dos dados.

---

## ⚙️ Funcionalidades

1. **Carregamento e Processamento de Dados**:
   - Carrega dados de um arquivo Excel contendo informações mensais sobre crimes.
   - Processa os dados, converte meses para o formato datetime e mapeia nomes de meses em português para números.

2. **Estatísticas Básicas**:
   - Calcula média, mediana e desvio padrão para crimes como homicídios, assaltos, roubos de veículos, entre outros.

3. **Visualizações**:
   - **Gráfico de área**: Comparação entre diferentes crimes.
   - **Gráfico de linha**: Evolução mensal de homicídios e assaltos.
   - **Gráfico de barras**: Totais de crimes ao longo do ano.

4. **API REST com Flask**:
   - Endpoint `/api/statistics`: Retorna estatísticas básicas.
   - Endpoint `/api/data`: Retorna os dados carregados.

5. **Interface Interativa com Streamlit**:
   - Exibição de estatísticas, tabelas e gráficos de forma dinâmica.

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- Pipenv ou pip para gerenciar dependências

### Dependências
As seguintes bibliotecas são usadas:
- `pandas`
- `matplotlib`
- `seaborn`
- `flask`
- `streamlit`
- `requests`



Baixe os dados: Certifique-se de ter o arquivo Excel com os dados de violência urbana no caminho especificado:
-violencia_urbana_rio_2023.xlsx

Inicie o Flask e Streamlit: Execute o script principal:
-`python trabalho7.py`

Acesse a API Flask:

    Abra o navegador e vá para: http://127.0.0.1:5000/api/statistics para visualizar as estatísticas.
    Ou acesse http://127.0.0.1:5000/api/data para visualizar os dados.

Acesse a Interface Streamlit:

    No terminal, um link para o Streamlit será gerado. Clique para abrir no navegador.
