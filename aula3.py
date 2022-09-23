import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


filmes = pd.read_csv("tmdb_5000_movies.csv")

# print(filmes.head())#5 primeiros
# print(filmes.original_language.unique())#uso do unique pra "agrupar" os tipos de idiomas

#contar valores
# print(filmes["original_language"].value_counts().to_frame())#transformar de "serie" para dataframe
# print(filmes["original_language"].value_counts().to_frame().reset_index())#transformar o indice em coluna

linguas_contagem = filmes["original_language"].value_counts().to_frame().reset_index()
linguas_contagem.columns = ["lingua_original", "total"]#renomeando as colunas
# print(linguas_contagem.head())

#plotar os graficos para categorias. Usando o grafico tipo barra. Usando x e y pro grafico
# sns.barplot(x = "lingua_original", y = "total", data = linguas_contagem)

#usando o seaborn para plotar o mesmo grafico porém usando o modelo de categoria.
#Aqui usaremos os dados não tratados
# sns.catplot(x="original_language", kind = "count",data = filmes)

#usando o grafico de pizza(pie chart)
# plt.pie(linguas_contagem["total"], labels=linguas_contagem["lingua_original"])
# plt.show()

# print(filmes["original_language"].value_counts().loc["en"])#contar por parametro passado

#para plotar um grafico de melhor visualização. É melhor isolar o Ingles que tem muitas ocorrências e comparas ao total das demais
# ingles = filmes["original_language"].value_counts().loc["en"]
# demais_linguas = filmes["original_language"].value_counts().sum() - ingles

#vamos criar um dataFrame. Usando dictionary do Python
# dados = {
#     'lingua' : ['ingles', 'outros'],
#     'total' : [ingles, demais_linguas]
# }
# df_dados = pd.DataFrame(dados)
# sns.barplot(x = "lingua", y="total", data = df_dados)
# plt.show()


#obter e plotar os dados sem o idioma ingles
outras_liguas = filmes.query("original_language != 'en'")
sns.catplot(x="original_language", kind="count", data = outras_liguas)
plt.show()