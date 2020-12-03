##Foi utilizado a biblioteca Pandas para a manipulação do arquivo CSV
##e após isso transformar em um DataFrame
import pandas as pd

# Feita a leitura do CSV a partir de uma função do pandas
doc = pd.read_csv('./dataset/notas.csv')

# Cálculo do tamanho total do documento
tamTotal = int(doc.size/doc.columns.size)

# Criação do DataFrame proporcionado pelo pandas
def criarDataFrame():
    COLUNAS = ['MATRICULA', 'COD_DISCIPLINA', 'COD_CURSO',
               'NOTA', 'CARGA_HORARIA', 'ANO_SEMESTRE']
    data = pd.DataFrame(columns=COLUNAS)
    return data
