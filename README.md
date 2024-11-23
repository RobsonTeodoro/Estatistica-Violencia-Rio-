Análise de Dados de Violência no Rio de Janeiro - 2023

Este é um projeto de exemplo criado para demonstrar o uso do Streamlit em um contexto de análise de dados de segurança pública. 
Ele foi desenvolvido para visualizar dados de violência urbana no Rio de Janeiro em 2023.

Descrição

Este projeto utiliza Streamlit para criar uma aplicação web interativa que permite visualizar dados de violência urbana, como homicídios, assaltos, roubos de veículos, furtos, entre outros. Além disso, oferece uma API construída com Flask para disponibilizar estatísticas básicas dos dados.

Funcionalidades

•	Carregar dados de um arquivo Excel.

•	Gerar estatísticas básicas (média, mediana, desvio padrão).

•	Visualizar dados através de gráficos interativos utilizando matplotlib e seaborn.

•	API Flask para fornecer dados e estatísticas em formato JSON.

Estrutura do Projeto
plaintext
Copiar código


├── data_handler.py

├── statistics.py

├── visualization.py

├── app.py

├── main.py

└── README.md

•	data_handler.py: Contém a classe DataHandler para carregamento e processamento dos dados.

•	statistics.py: Contém a classe Statistics para cálculo de estatísticas básicas.

•	visualization.py: Contém a classe Visualization para geração de gráficos.

•	app.py: Script principal que executa a aplicação Flask.

•	main.py: Script principal que executa a aplicação Streamlit.

•	README.md: Documento explicativo do projeto.



Pré-requisitos

•	Python 3.13

•	pip para gerenciar dependências

Dependências

As seguintes bibliotecas são usadas:

•	pandas

•	matplotlib

•	seaborn

•	flask

•	streamlit

•	requests


Instalação
1.	Clone o repositório:
bash

Copiar código

git clone https://github.com/seu-usuario/nome-do-repositorio.git

cd nome-do-repositorio

3.	Crie um ambiente virtual e ative-o:
   
bash

Copiar código

python -m venv venv

source venv/bin/activate  # No Windows, use `venv\Scripts\activate`

5.	Instale as dependências:
bash

Copiar código

pip install -r

requirements.txt

Executando a Aplicação

1.	Certifique-se de que o arquivo violencia_urbana_rio_2023.xlsx está no diretório correto.
   
3.	Execute o script principal com o Streamlit:
   
bash

Copiar código

python main.py

5.	Acesse a aplicação no seu navegador através do endereço indicado pelo Streamlit (geralmente http://localhost:8501).
   
Exemplo de Uso

A aplicação apresenta várias visualizações dos dados de violência urbana no Rio de Janeiro em 2023. Os gráficos incluem histogramas, gráficos de área, gráficos de linha e gráficos de barras, permitindo uma análise detalhada dos diferentes tipos de crimes ao longo do ano.

Detalhes do Código

Manipulação de Dados (data_handler.py)

O manipulador de dados é responsável por carregar e preparar os dados.

•	Classe DataHandler:

o	__init__(self, file_path): Inicializa a classe com o caminho para o arquivo Excel.


o	load_data(self): Carrega os dados do arquivo Excel e mapeia os meses em português para números.


o	get_data(self): Retorna o DataFrame de dados mais atualizado.


Estatísticas (statistics.py)

A classe de estatísticas calcula estatísticas básicas a partir dos dados.

•	Classe Statistics:

o	__init__(self, data_handler): Inicializa a classe com o manipulador de dados.

o	get_basic_statistics(self): Calcula e retorna estatísticas básicas (média, mediana, desvio padrão) dos dados.

Visualização (visualization.py)

A classe de visualização gera gráficos interativos.

•	Classe Visualization:

o	plot_histogram(self, column, bins=30): Gera um histograma para a coluna especificada.

o	plot_area(self, col1, col2): Gera um gráfico de área entre duas colunas.

o	plot_line_comparison(self): Gera um gráfico de linhas para comparar a evolução dos homicídios ao longo do tempo.

o	plot_line_assaults(self): Gera um gráfico de linhas para a evolução dos assaltos.

o	plot_totals_bar_chart(self): Gera um gráfico de barras mostrando os totais das colunas numéricas.

API Flask (app.py)

A API Flask fornece dados e estatísticas básicas.

•	Endpoint /api/statistics: Retorna estatísticas básicas dos dados.

•	Endpoint /api/data: Retorna os dados mais recentes em formato JSON.

Aplicação Streamlit (main.py)

O script principal que configura e executa a aplicação Streamlit.

Executando o Streamlit

O script principal para executar o Streamlit está em main.py. Ele configura a interface do usuário, carrega os dados, exibe as estatísticas básicas e gera gráficos interativos.

Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.


ScreenShot

Gráfico de Linha - Evolução de Homicídios no Rio de Janeiro.png

Gráficos de Área - Homicídios x Assaltos.png

Gráfico de Linha - Evolução de Assaltos no Rio de Janeiro.png

Gráfico de Barras - Totais de Incidentes no Ano de 2023.png


