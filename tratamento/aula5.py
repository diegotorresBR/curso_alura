import pandas as pd

dados = pd.read_csv("extras/dados/aluguel_residencial.csv", sep=";")
selecao = dados["Tipo"] == "Apartamento"
n1 = dados[selecao].shape[0] #Selecao apenas de apartamentos

#A seguir com mais de um parametro
selecao = (dados["Tipo"] == "Casa") | (dados["Tipo"] == "Casa de Condominio") | (dados["Tipo"] == "Casa de Vila")
n2 = dados[selecao].shape[0] # contando ocorrencias

#Imoveis com area entre 60 e 100
selecao = (dados["Area"] >= 60) & (dados["Area"] <= 100)
n3 = dados[selecao].shape[0]

#Imoveis que tenham 4 quartos e aluguel menor que 2000
selecao = (dados['Quartos'] >= 4) & (dados["Valor"] < 2000)
n4 = dados[selecao].shape[0]

print("Numeros de Apartamentos: {}".format(n1))



