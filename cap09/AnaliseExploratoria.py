import pandas as pd
import matplotlib.pyplot as plt
import warnings
import GraficosAnaliseExploratoria as graficos
plt.style.use('seaborn-talk')
warnings.filterwarnings('ignore')

dados = pd.read_csv("arquivos/Dados-Pesquisa.csv", sep=",", low_memory=False)
print(dados.head())     # Resumo
print(list(dados))      # Colunas

#graficos.distribuicaoIdade(dados)
#graficos.distribuicaoSexo(dados)
#graficos.distribuicaoInteresseJob(dados)
#graficos.distribuicaoEmpregrabilidade(dados)
#graficos.distribuicaoPreferenciaTrabalhoIdade(dados)
#graficos.distribuicaoRealocacaoIdade(dados)
#graficos.distribuicaoHorasIdade(dados)
graficos.distribuicaoInvestimentoSalario(dados)


