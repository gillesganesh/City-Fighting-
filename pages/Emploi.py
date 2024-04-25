# Importer les librairies
import streamlit as st
import numpy as np
import pandas as pd

def load_data():
    data = pd.read_csv("Donnees\Emploi_France.csv")  
    return data
def main():
    st.set_page_config(
        initial_sidebar_state="collapsed"
    )

    ville_1 = st.query_params["city1"]
    ville_2 = st.query_params["city2"]    

    page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
            background-image: url("https://i.imgur.com/ZYhQ5fP.jpeg");
            background-size: cover;
            background-position: top left;
            background-repeat: no-repeat;
            background-attachment: local;
        }}
        </style>
    """


    # Afficher l'image de fond
    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.markdown("""
        <style>
            .custom-button {
                color: #FFFB7C;
                padding: 10px 20px; /* Réduire la taille du padding */
                border-radius: 5px;
                border: none;
                cursor: pointer;
                box-shadow: 2px 2px 5px #FFFB7C;
                font-weight : bolder;
                display: block;
                margin: 0 auto;
                font-size: 16px; /* Réduire la taille de la police */
                text-shadow: 2px 2px 5px #000000;
                text-align: center; /* Centrer le texte */
            }
            .custom-button:hover {
                color: #FF3B24;
                box-shadow: 10px 10px 10px #FF3B24;
                font-weight : bolder;
                text-shadow: 2px 2px 5px #FFFFFF;
            }
        </style>
    """, unsafe_allow_html=True)

    c1,c2,c3 = st.columns(3)
    with c1 :
        st.markdown(f'<a href="https://city-fighting-brahim-ben-gilles.streamlit.app/Menu?city1={ville_1}&city2={ville_2}" class="custom-button" style="color: inherit; text-decoration: none;" target="_self">Retour au menu</a> ', unsafe_allow_html=True)

    with c2 :
        st.markdown(f'<a href="https://city-fighting-brahim-ben-gilles.streamlit.app/Accueil?" class="custom-button" style="color: inherit; text-decoration: none;" target="_self">Comparer autres villes</a> ', unsafe_allow_html=True)
   
    st.title("Comparaison Emploi")
    data = load_data()

    # Définir le style de la page
    st.markdown(
        """
        <style>
        /* Définir la couleur du texte */
        .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
            color: #FFFB7C;
            text-shadow: 2px 2px 5px #C70039;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    

    if ville_1 == "" or ville_2 == "" :
        st.error("Veuillez sélectionner deux villes depuis la page d'accueil.")
    else:
        # Filtrer les données pour les villes sélectionnées
        data_ville1 = data[data["Ville"] == ville_1]
        data_ville2 = data[data["Ville"] == ville_2]

        # Calculer les indicateurs statistiques
        indicateurs_ville1 = {
            "Nombre de demandeurs d'emploi": f"{int(data_ville1['Sum_Nbr_demandeur_emploi'].sum()) if not pd.isnull(data_ville1['Sum_Nbr_demandeur_emploi'].sum()) else 'N/A'}",
            "Taux de satisfaction moyen": f"{round(data_ville1['Avg_Taux_satisfaction'].mean()) if not pd.isnull(data_ville1['Avg_Taux_satisfaction'].mean()) else 'N/A'}%",
            "Nombre moyen de retours à l'emploi": f"{round(data_ville1['Avg_Nombre_retours_emploi'].mean()) if not pd.isnull(data_ville1['Avg_Nombre_retours_emploi'].mean()) else 'N/A'}",
            "Taux de notification moyen": f"{round(data_ville1['Avg_Taux_notification'].mean()) if not pd.isnull(data_ville1['Avg_Taux_notification'].mean()) else 'N/A'}%"
        }

        indicateurs_ville2 = {
            "Nombre de demandeurs d'emploi": f"{int(data_ville2['Sum_Nbr_demandeur_emploi'].sum()) if not pd.isnull(data_ville2['Sum_Nbr_demandeur_emploi'].sum()) else 'N/A'}",
            "Taux de satisfaction moyen": f"{round(data_ville2['Avg_Taux_satisfaction'].mean()) if not pd.isnull(data_ville2['Avg_Taux_satisfaction'].mean()) else 'N/A'}%",
            "Nombre moyen de retours à l'emploi": f"{round(data_ville2['Avg_Nombre_retours_emploi'].mean()) if not pd.isnull(data_ville2['Avg_Nombre_retours_emploi'].mean()) else 'N/A'}",
            "Taux de notification moyen": f"{round(data_ville2['Avg_Taux_notification'].mean()) if not pd.isnull(data_ville2['Avg_Taux_notification'].mean()) else 'N/A'}%"
        }

        # Afficher les indicateurs statistiques
        c1, c2 = st.columns(2)
        with c1:
            st.title(ville_1 + " :")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Demandeurs d'emploi", indicateurs_ville1["Nombre de demandeurs d'emploi"])
                st.metric("Taux de satisfaction moyen", indicateurs_ville1["Taux de satisfaction moyen"])
                st.metric("Retours à l'emploi", indicateurs_ville1["Nombre moyen de retours à l'emploi"])
                st.metric("Taux de notification moyen", indicateurs_ville1["Taux de notification moyen"])
        with c2:
            st.title(ville_2 + " :")
            col3, col4 = st.columns(2)
            with col3:
                st.metric("Demandeurs d'emploi", indicateurs_ville2["Nombre de demandeurs d'emploi"])
                st.metric("Taux de satisfaction moyen", indicateurs_ville2["Taux de satisfaction moyen"])
                st.metric("Retours à l'emploi", indicateurs_ville2["Nombre moyen de retours à l'emploi"])
                st.metric("Taux de notification moyen", indicateurs_ville2["Taux de notification moyen"])

if __name__ == "__main__":
    main()
