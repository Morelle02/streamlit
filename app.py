import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Visualisation des données d'un fichier
st.title("Analyse des données Iris")

# Charger les données
uploaded_file = st.file_uploader("Télécharger un fichier CSV", type=["csv"])
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Aperçu des données :", data.head(20))
    
   
    st.write("Informations générales sur les données :")
    st.write(data.describe())
    
    # Sélectionner des colonnes
    columns = data.columns.tolist()
    x_axis = st.selectbox("Sélectionner la colonne pour l'axe X :", columns)
    y_axis = st.selectbox("Sélectionner la colonne pour l'axe Y :", columns)
    
    # Générer un graphique pour mieux comprendre les données
    st.write(f"Graphique : {x_axis} vs {y_axis}")
    fig, ax = plt.subplots()
    sns.scatterplot(data=data, x=x_axis, y=y_axis, ax=ax, hue=data.columns[-1])
    st.pyplot(fig)
    
   
else:
    st.write("Veuillez télécharger un fichier CSV pour commencer.")
