import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


notas = pd.read_csv("ratings.csv")
notas.columns = ["IdUsuario", "IdFilme", "Nota", "timestamp"]
print(notas.head())
#print(notas['rating'].mean())

#notas.Nota.plot(kind='hist')
#sns.load_dataset(notas.rating)
sns.boxplot(x = notas["Nota"])
plt.show()

print(notas['Nota'].describe())
