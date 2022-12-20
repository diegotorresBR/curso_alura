import pandas as pd

dados  = pd.read_csv("extras/dados/aluguel_residencial.csv", sep=";")

#print(dados.isnull())#valores nulos no DataFrame
#print(dados.notnull())#valores nao nulos
#print(dados.info())#obter infos de  tipo de variavel das colunas

nulos = dados[dados["Valor"].isnull()]#dados com Valor nulos

#eliminando valores Nulos do DF

tam_antes = dados.shape[0]
print(tam_antes)
dados.dropna(subset=["Valor"], inplace=True)#inplace irá sobreescrever o df
tem_depois = dados.shape[0]
print(tem_depois)
print(tam_antes - tem_depois)

#vamos verificar quantos condominios estao com o valor de imovel nulos
print(dados[dados["Condominio"].isnull()].shape[0])
selecao = (dados["Tipo"] == "Apartamento") & (dados["Condominio"].isnull())

tam_antes = dados.shape[0]
print(tam_antes)
dados = dados[~selecao]#inverte a seleção
tem_depois = dados.shape[0]
print(tem_depois)
print(tam_antes - tem_depois)

dados.fillna(0, inplace = True)#todos os valores nulos recebem 0

#dados.to_csv("extras/dados/aluguel_residencial.csv", sep=";", index = False)#Reescreve o arquivo

#Extra - Interpolação

data2 = [.5, None, None, .52, .54, None, None, .59, .6, None, .7]
s = pd.Series(data2)
print(s)
print(s.fillna(0))#metodo 1

print(s.fillna(method="ffill"))#met2, replica o valor anterior no valor nulo
print(s.fillna(method="bfill"))#met2, replica o valor posterior no valor nulo
print(s.fillna(s.mean()))#met3, media de todos os valores no valor nulo
print(s.fillna(method="ffill", limit=1))#met4, replica o valor anterior no valor nulo mas somente 1 vez