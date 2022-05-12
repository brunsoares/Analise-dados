import pandas as pd                                                     # manipulação de dados


def Resposta09(connection):
    print("\nPergunta 09: \n")

    consultaPerg09 = '''
                     Select primary_title as filme, genres, rating
                     From titles
                     Join ratings On titles.title_id = ratings.title_id
                     Where titles.type = \'movie\'
                     And ratings.votes >= 25000
                     Order By rating Desc
                     Limit 10
                     '''

    respostaPerg09 = pd.read_sql_query(consultaPerg09, connection)

    print(respostaPerg09)
