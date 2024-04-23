# Importer les librairies
import streamlit as st
import numpy as np
import pandas as pd
import folium
import requests
from streamlit_folium import folium_static
import json
from folium.plugins import MarkerCluster

# Charger le fichier CSV dans un DataFrame pandas
#df = pd.read_csv("Donnees/logements-2.csv", sep=",")

# Convertir le DataFrame en JSON
#json_data = df.to_json(orient="records")

# Écrire les données JSON dans un fichier
#with open("Donnees/logements.json", "w") as json_file:
    #json_file.write(json_data)

def load_data():
    with open("Donnees/logements.json", "r") as file:
        data = json.load(file)
    return data

def get_city_coordinates(city, weather_api_key):
    base_url = "http://api.openweathermap.org/geo/1.0/direct?q="
    complete_url = base_url + city + ",FR&limit=1" + "&appid=" + weather_api_key
    response = requests.get(complete_url)
    return response.json()

def recup_data(ville, data) :
    #city_data = data[data["inst_com_nom"] == ville]
    city_data = [entry for entry in data if entry["nom_commune"] == ville]
    return city_data 

def define_map(ville, weather_api_key) :
    coordinates_data = get_city_coordinates(ville, weather_api_key)

    m = folium.Map(location=[coordinates_data[0]["lat"], coordinates_data[0]["lon"]], zoom_start=12)

    data_b = load_data()
    data = recup_data(ville, data_b)
    nb_logement = 0
    prix_s = 0
    surface_s = 0
    markers = MarkerCluster().add_to(m)  # Création d'un cluster de marqueurs

    for logement in data:
        nb_logement = nb_logement + 1
        lon, lat = logement["longitude"], logement["latitude"]

    
        nom = logement["nom_commune"]
        surface = logement["surface_reelle_bati"]
        prix = logement["valeur_fonciere"]
        if prix is not None:  
            prix_s = prix_s + prix
        if surface is not None:  
            surface_s = surface_s + surface

        # Créer un marqueur et l'ajouter au cluster
        folium.Marker(
            location=[lat, lon],
            popup=f"{nom}<br>Surface : {surface} m² <br> Prix : {prix}€",
            icon=folium.Icon(color="blue", icon="home", prefix="fa"),
        ).add_to(markers)
        

        if prix_s is not None and surface_s is not None:
            if surface_s != 0: 
                prix_moy = prix_s / surface_s

    st.markdown(f"Nombre de logements : {nb_logement}")
    st.markdown(f"Prix moyen du m² : {round(prix_moy, 2)} €")

    folium_static(m)

def main():
    st.set_page_config(
        initial_sidebar_state="collapsed"
    )

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

    weather_api_key = st.secrets["weather_api_key"]

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
   
    st.title("Comparaison des logements")


    liste_villes = ville_1, ville_2
    ville = st.selectbox("Choississez une ville : ", sorted(liste_villes), index=0, help="Sélectionnez la première ville à comparer.")

    define_map(ville, weather_api_key)

if __name__ == "__main__":
    main()
