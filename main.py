import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

filmes  = pd.read_csv("movies.csv")

notas = pd.read_csv("ratings.csv")
notas.columns = ["IdUsuario", "IdFilme", "Nota", "timestamp"]
# print(notas.head())
# #print(notas['rating'].mean())
#
# #notas.Nota.plot(kind='hist')
# #sns.load_dataset(notas.rating)
# sns.boxplot(x = notas["Nota"])
# plt.show()
#
# print(notas['Nota'].describe())

# print(filmes.head())
print(notas.query("IdFilme==1").Nota.mean())

media_filmes = notas.groupby("IdFilme").mean()["Nota"]

print(media_filmes.head())

media_filmes.plot(kind='hist')
plt.show()