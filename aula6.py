import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

filmes = pd.read_csv('movies.csv')
notas  = pd.read_csv('ratings.csv')

filme_toy_story = notas.query("movieId == 1")
filme_jumanji = notas.query("movieId == 2")

print(len(filme_toy_story), len(filme_jumanji))#total de avaliações

#media de notas
print("Media Filme 1 %.2f"% filme_toy_story.rating.mean())
print("Media Filme 2 %.2f"% filme_jumanji.rating.mean())

#mediana das notas

print("Mediana Filme 1 %.2f"% filme_toy_story.rating.median())
print("Mediana Filme 2 %.2f"% filme_jumanji.rating.median())

#vamos simular varias notas fixas em um valor apenas
varias = np.array([2.5] *10)#repetir 10 vezes o mesmo valor
varias2 = np.array([3.5]*10)
nota_simula = np.append(varias, varias2)

sns.distplot(nota_simula)
plt.show()