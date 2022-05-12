# Imports
import sqlite3          # banco de dados
import warnings         # filtrar alertas / erros
import seaborn as sns   # visualização de dados
# Import das Estruturas do banco
#import EstruturaTabelas
# Import das respostas
#import Pergunta01
#import Pergunta02
#import Pergunta03
#import Pergunta04
#import Pergunta05
#import Pergunta06
#import Pergunta07
import Pergunta08
#import Pergunta09
#import Pergunta10
warnings.filterwarnings("ignore")   # ignora alertas
sns.set_theme(style="whitegrid")    # define thema padrão para gráficos

# Carregar dados do imdb -> terminal = "imdb-sqlite"

connection = sqlite3.connect("../database/imdb.db")    # Conexão ao banco

#EstruturaTabelas.EstruturaTabelasView(connection)
# Import das classes onde cada pergunta foi respondida
#Pergunta01.Resposta01(connection)
#Pergunta02.Resposta02(connection)
#Pergunta03.Resposta03(connection)
#Pergunta04.Resposta04(connection)
#Pergunta05.Resposta05(connection)
#Pergunta06.Resposta06(connection)
#Pergunta07.Resposta07(connection)
Pergunta08.Resposta08(connection)
#Pergunta09.Resposta09(connection)
#Pergunta10.Resposta10(connection)
















