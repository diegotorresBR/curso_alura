import pandas as pd

dados = pd.read_csv("aluguel.csv", sep=";")
residencial = ['Quitinete', 'Casa', 'Apartamento', 'Casa de Condomínio', 'Casa de Vila']
df_residencial = dados[dados['Tipo'].isin(residencial)]#obter somente os dados nessa seleção
print(df_residencial)