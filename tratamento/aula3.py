import pandas as pd

aluguel = pd.read_csv("aluguel.csv", sep=";")
# print(aluguel["Tipo"].unique())#como array
# print(aluguel["Tipo"].drop_duplicates())#como indice de Series

s_aluguel = aluguel["Tipo"].drop_duplicates()
tipo = pd.DataFrame(s_aluguel)

tipo.index =  range(tipo.index.shape[0])
print(tipo)