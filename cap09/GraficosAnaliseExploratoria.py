import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import colorsys
import warnings
plt.style.use('seaborn-talk')
warnings.filterwarnings('ignore')


def listaCores(numeroDados):
    listaHSV = [(x * 1.0 / numeroDados, 0.5, 0.5) for x in range(numeroDados)]
    listaRGB = list(map(lambda x: colorsys.hsv_to_rgb(*x), listaHSV))
    return listaRGB


def distribuicaoIdade(dados):
    dados.Age.hist(bins=60)     # pegando dados
    plt.xlabel("Idade")
    plt.ylabel("Número de Profissionais")
    plt.title("Distribuição de Idade")
    plt.show()


def distribuicaoSexo(dados):
    # Definindo quantidade dos dados
    labelsGeneros = dados.Gender.value_counts().index
    numeroGeneros = len(dados.EmploymentField.value_counts().index)
    # Criando lista de cores para gráfico
    listaRGB = listaCores(numeroGeneros)

    # Criação do gráfico
    fatias, texto = plt.pie(dados.Gender.value_counts(), colors=listaRGB, startangle=90)
    plt.axes().set_aspect('equal', 'datalim')
    plt.legend(fatias, labelsGeneros, bbox_to_anchor=(1.05, 1))
    plt.title("Distribuição por Sexo")
    plt.show()


def distribuicaoInteresseJob(dados):
    numeroJob = len(dados.JobRoleInterest.value_counts().index)  # Pegando dados
    labels = dados.JobRoleInterest.value_counts().index
    # Lista de cores
    listaRGB = listaCores(numeroJob)

    # Criação do Gráfico
    fatias, texto = plt.pie(dados.JobRoleInterest.value_counts(), colors=listaRGB, startangle=90)
    plt.axes().set_aspect('equal', 'datalim')
    plt.legend(fatias, labels, bbox_to_anchor=(1.25, 1))
    plt.title("Distribuição por Interesse Profissional")
    plt.show()


def distribuicaoEmpregrabilidade(dados):
    numeroEmpregabilidade = len(dados.EmploymentField.value_counts().index)     # Pegando dados
    labels = dados.EmploymentField.value_counts().index
    # Lista de cores
    listaRGB = listaCores(numeroEmpregabilidade)

    # Criação do Gráfico
    fatias, texto = plt.pie(dados.EmploymentField.value_counts(), colors=listaRGB, startangle=90)
    plt.axes().set_aspect('equal', 'datalim')
    plt.legend(fatias, labels, bbox_to_anchor=(1.3, 1))
    plt.title("Distribuição por Empregabilidade")
    plt.show()


def distribuicaoPreferenciaTrabalhoIdade(dados):
    dadosAgrupandoIdade = dados.copy()  # Criando backup dos dados
    valoresColuna = [0, 20, 30, 40, 50, 60, 100]
    # Tratamento coluna nova
    dadosAgrupandoIdade['AgeRanges'] = pd.cut(dadosAgrupandoIdade['Age'],
                                              valoresColuna,
                                              labels=["< 20", "20-30", "30-40", "40-50", "50-60", "60 >"])
    dadosAgrupados = pd.crosstab(dadosAgrupandoIdade.AgeRanges,
                                 dadosAgrupandoIdade.JobPref).apply(lambda r: r/r.sum(), axis=1)

    # Quantidade dados
    numeroTrabalhoIdade = len(dadosAgrupandoIdade.AgeRanges.value_counts().index)
    # Lista cores
    listaRGB = listaCores(numeroTrabalhoIdade)

    # Criando Gráfico
    eixo = dadosAgrupados.plot(kind='bar', stacked=True, color=listaRGB, title="Distribuição de Preferência de Trabalho por Idade")
    lines, labels = eixo.get_legend_handles_labels()
    eixo.legend(lines, labels, bbox_to_anchor=(1.51, 1))
    plt.show()

def distribuicaoRealocacaoIdade(dados):
    dadosAgrupandoIdade = dados.copy()  # Criando backup dos dados
    valoresColuna = [0, 20, 30, 40, 50, 60, 100]
    # Tratamento coluna nova
    dadosAgrupandoIdade['AgeRanges'] = pd.cut(dadosAgrupandoIdade['Age'],
                                              valoresColuna,
                                              labels=["< 20", "20-30", "30-40", "40-50", "50-60", "60 >"])
    dadosAgrupados = pd.crosstab(dadosAgrupandoIdade.AgeRanges,
                                 dadosAgrupandoIdade.JobRelocateYesNo).apply(lambda r: r / r.sum(), axis=1)

    # Quantidade
    numeroRealocacao = len(dadosAgrupandoIdade.AgeRanges.value_counts().index)
    # Lista Cor
    listaRGB = listaCores(numeroRealocacao)

    # Criando Gráfico
    eixo = dadosAgrupados.plot(kind='bar', stacked=True, color=listaRGB, title="Distribuição de Realocação por Idade")
    lines, labels = eixo.get_legend_handles_labels()
    eixo.legend(lines, ["Não", "Sim"], loc='best')
    plt.show()

def distribuicaoHorasIdade(dados):
    dadosHorasIdade = dados.copy()
    dadosHorasIdade = dadosHorasIdade.dropna(subset=["HoursLearning"])
    dadosHorasIdade = dadosHorasIdade[dados['Age'].isin(range(0, 70))]  # Alimentando coluna com range de idade

    # Valores eixos
    eixoX = dadosHorasIdade.Age
    eixoY = dadosHorasIdade.HoursLearning

    # Criando Gráfico
    m, b = np.polyfit(eixoX, eixoY, 1)
    plt.plot(eixoX, eixoY, '.')
    plt.plot(eixoX, m*eixoX + b, '-', color='red')
    plt.xlabel("Idade")
    plt.ylabel("Horas de Treinamento")
    plt.title("Distribução Idade por Horas de Treinamento")
    plt.show()


def distribuicaoInvestimentoSalario(dados):
    dadosInvestimentoSalario = dados.copy()
    dadosInvestimentoSalario = dadosInvestimentoSalario.dropna(subset=['ExpectedEarning'])
    dadosInvestimentoSalario = dadosInvestimentoSalario[dados['MoneyForLearning'].isin(range(0, 60000))]

    # Valores eixos
    eixoX = dadosInvestimentoSalario.MoneyForLearning
    eixoY = dadosInvestimentoSalario.ExpectedEarning

    # Criando Gráfico
    m, b = np.polyfit(eixoX, eixoY, 1)
    plt.plot(eixoX, eixoY, '.')
    plt.plot(eixoX, m*eixoX + b, '-', color='red')
    plt.xlabel("Investimento do Treinamento")
    plt.ylabel("Expectativa Salarial")
    plt.title("Distribuição Investimento por Expectativa Salarial")
    plt.show()
