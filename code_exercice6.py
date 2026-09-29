import pandas as pd

df = pd.read_csv('ages.csv')
df

###

df.describe()

###

df.groupby('grouping').describe()

###

import matplotlib.pyplot as plt

men = df.query('grouping == "men"')['height']
women = df.query('grouping == "women"')['height']
plt.boxplot([men, women], labels=['Hommes', 'Femmes'])
plt.title('Taille par genre')
plt.ylabel('Taille (cm)')
plt.grid()
plt.show()

###

import scipy.stats as stats

# Question 2 : Vérification de la normalité (test de Shapiro-Wilk)
shapiro_men = stats.shapiro(men)
shapiro_women = stats.shapiro(women)
print(f"Normalité Hommes (Shapiro-Wilk) : p-value = {shapiro_men.pvalue:.4f}")
print(f"Normalité Femmes (Shapiro-Wilk) : p-value = {shapiro_women.pvalue:.4f}")

# Question 3 : Vérification de l'égalité des variances (test de Levene)
levene_test = stats.levene(men, women)
print(f"\nÉgalité des variances (Levene) : p-value = {levene_test.pvalue:.4f}")

# Question 4 : Comparaison des moyennes (Test T de Student indépendant)
# Si les variances sont égales, on peut utiliser le test t classique (equal_var=True)
t_stat, p_val = stats.ttest_ind(men, women, equal_var=True)
print(f"\nComparaison des moyennes (Test t) : p-value = {p_val:.4f}")

if p_val < 0.05:
    print("La différence de moyenne de taille entre les hommes et les femmes est statistiquement significative.")
else:
    print("Il n'y a pas de différence statistiquement significative de taille moyenne entre les hommes et les femmes.")