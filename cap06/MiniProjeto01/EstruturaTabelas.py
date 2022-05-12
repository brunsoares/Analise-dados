import pandas as pd                                                     # manipulação de dados
import os                                                               # limpar console
import time                                                             # usado para pausas


def EstruturaTabelasView(connection):
    print("\nEstrutura de tabelas: \n")
    # Select para listar as tabelas do banco
    tabelas = pd.read_sql_query("Select NAME as 'Table_Name' From sqlite_master Where type = 'table' ", connection)
    print(tabelas.head())

    tabelas = tabelas["Table_Name"].values.tolist()     # Conversão para list

    # Detalhando o esquema de cada tabela do banco
    print("\nDetalhamento de cada tabela:\n")
    for tbl in tabelas:
        consulta = "PRAGMA TABLE_INFO ({})".format(tbl)
        resultado = pd.read_sql_query(consulta, connection)
        print("-*-"*50)
        print("Esquema da tabela: ", tbl)
        print(resultado)
        print("-"*50)
        print("\n")

    # Respondendo as perguntas do Exercicio
    time.sleep(2)
    os.system("cls") or None     # Limpando console poluido