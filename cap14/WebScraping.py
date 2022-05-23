import urllib.request   # Requisição
from bs4 import BeautifulSoup   # Tratamento do HTML

with urllib.request.urlopen("https://www.python.org") as url:   # Faz a requisição em alguma url
    page = url.read()

print(page)

# Tratamento do HTML da Pagina
soupFormatter = BeautifulSoup(page, 'html.parser')       # Formato BeautifulSoup
# Pegando dados pela TAG HTML
print(soupFormatter.title)
print(soupFormatter.title.string)

