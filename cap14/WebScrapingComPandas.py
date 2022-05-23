import pandas as pd
import requests     # Outra biblioteca que faz requisições
from bs4 import BeautifulSoup
from tabulate import tabulate

# Pegando dados
resposta = requests.get("http://www.nationmaster.com/country-info/stats/Media/Internet-users")

# Formatando
soupFormatter = BeautifulSoup(resposta.content, 'lxml')     # Outro formato LXML
# Extraindo a tabela com codigo HTML
tabela = soupFormatter.find_all('table')[0]
print("Tabela Extraida HTML:")
print(tabela)

# Conversão da tabela em DataFrame Pandas
dataFrame = pd.read_html(str(tabela))
print("DataFrame a partir da Tabela HTML:")
print(dataFrame)

# Conversão para formato JSON
dadosJson = dataFrame[0].to_json(orient='records')
print("JSON a partir do DataFrame")
print(dadosJson)

# Conversão para Tabela usando Tabulate
tabelaDados = tabulate(dataFrame[0], headers='keys', tablefmt='psql')
print("Tabela Formatada a partir do DataFrame")
print(tabelaDados)
