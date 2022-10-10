import pandas as pd

aluguel = pd.read_csv("aluguel.csv", sep=';')#separador ';'
# print(aluguel.head())
# print(type(aluguel))
# print(aluguel.info())#verifica cada tipo de dado de cada coluna
# print(aluguel.dtypes)
dados = pd.DataFrame(aluguel.dtypes, columns=['Tipos de Dados'])
dados.columns.name = 'Variáveis'
print(dados)
print(aluguel.shape)#qtd de obs. qtd de linhas e colunas
print("nessa base temos {} registros e {} variaveis".format(aluguel.shape[0], aluguel.shape[1]))