# Arquivo de funções uteis
from sklearn.feature_extraction.text import CountVectorizer             # machine learn (Cálculos)


def retornarGeneros(listaValores):
    listaValores['genres'] = listaValores['genres'].str.lower().values
    semValoresNA = listaValores['genres'].dropna()
    vetor = CountVectorizer(token_pattern='(?u)\\b[\\w-]+\\b', analyzer='word').fit(semValoresNA)
    generosUnicos = vetor.get_feature_names()
    generosUnicos = [genre for genre in generosUnicos if len(genre) > 1]
    return generosUnicos