import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

lien = 'https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv'

df = pd.read_csv(lien)

df.continent = df.continent.replace([' Japon.', ' US.', ' Europe.'], ['Japon','USA','Europe'])

color = sns.color_palette("vlag", as_cmap=True)
# print(df.info())
# print(df.columns)
# sns.heatmap(df.drop(columns = 'continent').corr(), annot = True, cmap = color, center = 0)
# plt.show()



# Titre
st.title('Challenge streamlit')

# Ecriture
st.write("Heatmap")

# Affichage du DF
st.write(df)

# Création de la dataviz corrélation
# viz_correlation = sns.heatmap(df.drop(columns = ['continent']).corr(),annot = True, 
# 								center=0,
# 								cmap = sns.color_palette("vlag", as_cmap=True)
# 								)
# st.pyplot(viz_correlation.figure)
# st.write("Sur la heatmap, nous pouvons observer une fortes corrélations entre 'cylinders', 'cubicinches','hp' et 'weightlbs'.")

# # Affichage de la corrélation
# st.pyplot(sns.pairplot(df, hue = 'continent'))

##########################

# Avec changement de date

##########################
annee_min = df.year.min()
annee_max = df.year.max()

# Création slider
annee = st.slider('Quelle année voulez-vous selectionner ?',annee_min , annee_max)
st.write(" On regarde entre :", annee, ' et ', annee_max)

liste_col = ['mpg','cylinders', 'cubicinches', 'hp',  'weightlbs', 'time-to-60','year']

#Création de la dataviz corrélation
viz_correlation = sns.heatmap(df[liste_col][df.year>annee].corr(),annot = True, 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)
st.pyplot(viz_correlation.figure)

st.header("Graphe n°2")

# Création du bouton
options = st.multiselect(
    'Choisissez un ou des continents ?',
    ['USA', 'Europe', 'Japon'])

st.write('You selected:', options)

viz = sns.jointplot(data = df[df.continent.isin(options)], x = 'cubicinches', y='hp', hue = 'continent')
st.pyplot(viz)

# st.header("Test")


# # Création du bouton
# options = st.multiselect(
#     'Choisissez un ou des continents ?',
#     ['USA', 'Europe', 'Japon'])

# st.write('You selected:', options)

# viz2_correlation = sns.jointplot(data = df[df['continent'].isin(options)], x = 'year', y='cylinders', hue = 'continent')
# st.pyplot(viz2_correlation.figure)
