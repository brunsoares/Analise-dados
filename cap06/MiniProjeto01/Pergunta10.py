import pandas as pd                                                     # manipulação de dados


def Resposta10(connection):
    print("\nPergunta 10: \n")

    consultaPerg10 = '''
                     Select primary_title as filme, genres, rating
                     From titles
                     Join ratings On titles.title_id = ratings.title_id
                     Where titles.type = \'movie\'
                     And ratings.votes >= 25000
                     Order By rating Asc
                     Limit 10
                     '''

    respostaPerg10 = pd.read_sql_query(consultaPerg10, connection)

    print(respostaPerg10)
