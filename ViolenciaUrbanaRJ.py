'''
202405000749 Rondinele da Conceição Barbalho
202405500731 Robson Teodoro Rodrigues da Silva
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, jsonify, request
import threading
import streamlit as st
import requests
import time
import matplotlib.dates as mdates

# 1. Alterando o caminho do arquivo
class DataHandler:
    def __init__(self, file_path=None):
        self.file_path = file_path

    def load_data(self):
        if self.file_path is None:
            raise ValueError("O caminho para o arquivo Excel não foi fornecido.")

        try:
            # Carregar o arquivo Excel
            data = pd.read_excel(self.file_path)

            # Mapeamento de meses em português para números (Janeiro = 1, Fevereiro = 2, etc.)
            meses_portugues = {
                "Janeiro": 1, "Fevereiro": 2, "Março": 3, "Abril": 4, "Maio": 5, "Junho": 6,
                "Julho": 7, "Agosto": 8, "Setembro": 9, "Outubro": 10, "Novembro": 11, "Dezembro": 12
            }

            # Criar uma nova coluna 'Data' com o primeiro dia de cada mês
            data['Mês'] = data['Mês'].map(meses_portugues)
            data['Data'] = pd.to_datetime(data['Mês'].astype(str) + '-2023', format='%m-%Y')

            print("Dados carregados com sucesso do arquivo Excel:")
            print(data.head())  # Imprime as primeiras linhas dos dados para debug

            return data
        except Exception as e:
            raise ValueError(f"Erro ao carregar os dados do arquivo Excel: {e}")

    def get_data(self):
        """Retorna o DataFrame de dados mais atualizados (sempre recarrega do Excel)."""
        print("Recarregando os dados...")
        return self.load_data()  # Recarrega os dados sempre que necessário


# 2. Atualizando a classe Statistics
class Statistics:
    def __init__(self, data_handler):
        self.data_handler = data_handler

    def get_basic_statistics(self):
        """Calcula estatísticas básicas (média, mediana, desvio padrão) a partir dos dados mais recentes."""
        data = self.data_handler.get_data()  # Recarregar os dados mais recentes diretamente do arquivo Excel

        print("Calculando estatísticas com os dados mais recentes:")
        print(data.head())  # Verificando os dados que estão sendo usados para calcular as estatísticas

        # Filtrar apenas as colunas numéricas relevantes:
        relevant_columns = ['Homicídios', 'Assaltos', 'Roubos de Veículos', 'Furtos', 
                            'Latrocínios', 'Lesão Corporal', 'Violência Doméstica']
        numeric_data = data[relevant_columns]  # Filtra somente as colunas de interesse

        # Calcular as estatísticas
        stats = {
            'mean': numeric_data.mean().to_dict(),
            'median': numeric_data.median().to_dict(),
            'std': numeric_data.std().to_dict()
        }
        return stats


# 3. Atualizando a classe Visualization
class Visualization:
    def __init__(self, data):
        self.data = data

    def plot_histogram(self, column, bins=30):
        """Gera um histograma para a coluna especificada."""
        if column in self.data.select_dtypes(include=['number']).columns:
            plt.figure(figsize=(8, 6))
            ax = sns.histplot(self.data[column], kde=True, bins=bins)
            plt.title(f'Histograma de {column}')
            plt.xlabel(column)
            plt.ylabel('Frequência')

            # Ajustar as datas na parte inferior (eixo X) para o formato brasileiro
            plt.xticks(rotation=45)
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))  # Formatação da data

            st.pyplot(plt)
        else:
            st.warning(f'A coluna "{column}" não é numérica.')

    def plot_area(self, col1, col2):
        """Gera um gráfico de área entre duas colunas com cores distintas para cada dado."""
        if col1 in self.data.select_dtypes(include=['number']).columns and col2 in self.data.select_dtypes(
                include=['number']).columns:
            plt.figure(figsize=(10, 6))

            # Plotando a área para 'col1' com cor azul:
            area1 = plt.fill_between(self.data['Data'], self.data[col1], color='blue', alpha=0.5, label=col1)

            # Plotando a área para 'col2' com cor vermelha:
            area2 = plt.fill_between(self.data['Data'], self.data[col2], color='red', alpha=0.5, label=col2)

            plt.title(f'Gráfico de Área entre {col1} e {col2}')
            plt.xlabel('Mês')
            plt.ylabel('Quantidade')

            # Ajustar as datas na parte inferior (eixo X) para o formato brasileiro:
            plt.xticks(rotation=45)
            plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))  # Formatação da data

            plt.legend(title='Tipo de Dado')

            st.pyplot(plt)
        else:
            st.warning(f'Uma ou ambas as colunas "{col1}" e "{col2}" não são numéricas.')

    def plot_line_comparison(self):
        """Gera um gráfico de linhas para comparar a evolução dos valores ao longo dos meses."""
        plt.figure(figsize=(10, 6))

        # Plotando o gráfico de linhas comparando 'Homicídios' ao longo do tempo
        line = sns.lineplot(x='Data', y='Homicídios', data=self.data, label='Homicídios', color='blue', marker='o')

        # Adicionando títulos e labels
        plt.title('Evolução de Homicídios ao Longo do Ano', fontsize=14)
        plt.xlabel('Mês', fontsize=12)
        plt.ylabel('Número de Homicídios', fontsize=12)

        # Ajustar as datas na parte inferior (eixo X) para o formato brasileiro
        plt.xticks(rotation=45)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))  # Formatação da data

        plt.legend(title='Tipo de Dado')

        st.pyplot(plt)

    def plot_line_assaults(self):
        """Gera um gráfico de linha para a evolução dos assaltos acumulados."""
        plt.figure(figsize=(10, 6))

        # Plotando o gráfico de linhas comparando 'Assaltos' ao longo do tempo
        line = sns.lineplot(x='Data', y='Assaltos', data=self.data, label='Assaltos', color='red', marker='o')

        # Adicionando títulos e labels
        plt.title('Evolução de Assaltos ao Longo do Ano', fontsize=14)
        plt.xlabel('Mês', fontsize=12)
        plt.ylabel('Número de Assaltos', fontsize=12)

        # Ajustar as datas na parte inferior (eixo X) para o formato brasileiro
        plt.xticks(rotation=45)
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))  # Formatação da data

        plt.legend(title='Tipo de Dado')

        st.pyplot(plt)

    def plot_totals_bar_chart(self):
        """Gera um gráfico de barras mostrando os totais das colunas numéricas."""
        # Identificando a linha de totais (última linha)
        total_row = self.data.iloc[-1]

        # Selecionando apenas as colunas numéricas
        relevant_columns = ['Homicídios', 'Assaltos', 'Roubos de Veículos', 'Furtos', 
                            'Latrocínios', 'Lesão Corporal', 'Violência Doméstica']
        totals = total_row[relevant_columns]

        # Plotando o gráfico de barras
        plt.figure(figsize=(10, 6))
        sns.barplot(x=totals.index, y=totals.values, palette="Blues_d")

        # Títulos e labels
        plt.title('Totais de Incidentes ao Longo de 2023', fontsize=14)
        plt.xlabel('Tipo de Crime', fontsize=12)
        plt.ylabel('Total', fontsize=12)

        st.pyplot(plt)


# 4. API Flask
app = Flask(__name__)

# _Camin_ho para o arquivo Excel com os dados
file_path = "C:\\Users\\Robson\\Documents\\PÓS\\Linguagem Python\\Aula 2\\violencia_urbana_rio_2023.xlsx"

# Instanciando as classes
data_handler = DataHandler(file_path=file_path)
statistics = Statistics(data_handler)


@app.route('/api/statistics', methods=['GET'])
def get_statistics():
    """API que retorna as estatísticas básicas."""
    stats = statistics.get_basic_statistics()
    return jsonify(stats)


@app.route('/api/data', methods=['GET'])
def get_data():
    """API que retorna os dados mais recentes."""
    data = data_handler.get_data()
    return jsonify(data.to_dict(orient='records'))


# Função para rodar o Streamlit
def run_streamlit():
    time.sleep(2)  # Delay para garantir que o Flask inicie primeiro
    st.title("Análise de Dados de Violência no Rio de Janeiro - 2023")

    # Carregar os dados
    data = data_handler.get_data()
    st.write(data.head())

    # Exibir estatísticas básicas da API Flask
    response = requests.get('http://127.0.0.1:5000/api/statistics')
    if response.status_code == 200:
        stats = response.json()
        st.subheader("Estatísticas Básicas")
        st.write(stats)

    # Visualizações:
    st.subheader("Gráficos de Área - Homicídios x Assaltos")
    visualization = Visualization(data)
    visualization.plot_area('Homicídios', 'Assaltos')

    # Exibir o gráfico de comparação de evolução de homicídios:
    st.subheader("Evolução de Homicídios no Rio de Janeiro:")
    visualization.plot_line_comparison()

    # Exibir o gráfico de evolução de assaltos:
    st.subheader("Evolução de Assaltos no Rio de Janeiro:")
    visualization.plot_line_assaults()

    # Dentro do run_streamlit(), logo após a exibição dos gráficos principais
    st.subheader("Totais de Incidentes no Ano de 2023:")
    visualization.plot_totals_bar_chart()


def run_flask():
    app.run(debug=False, use_reloader=False)


if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    run_streamlit()