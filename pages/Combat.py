# Importer les librairies
import streamlit as st
import numpy as np
import pandas as pd
import folium
import requests
from streamlit_folium import folium_static
import json



def load_data():
    with open("Donnees/salle_combat.json", "r") as file:
        data = json.load(file)
    return data

def get_city_coordinates(city, weather_api_key):
    base_url = "http://api.openweathermap.org/geo/1.0/direct?q="
    complete_url = base_url + city + ",FR&limit=1" + "&appid=" + weather_api_key
    response = requests.get(complete_url)
    return response.json()

def recup_data(ville, data) :
    #city_data = data[data["inst_com_nom"] == ville]
    city_data = [entry for entry in data if entry["inst_com_nom"] == ville]
    return city_data 

def define_map(ville, weather_api_key) :
    coordinates_data = get_city_coordinates(ville, weather_api_key)

    m = folium.Map(location=[coordinates_data[0]["lat"], coordinates_data[0]["lon"]], zoom_start=12)

    data_b = load_data()
    data = recup_data(ville, data_b)
    nb_salles = 0
    niv_moy = 0
    for salles in data:
        nb_salles = nb_salles + 1
        lon, lat = salles["equip_x"], salles["equip_y"]
        name = salles["inst_nom"]
        adresse = salles["inst_adresse"]
        niveau = salles["dens_niveau"]
        niv_moy = niv_moy + niveau

        # Créer un marqueur avec une info-bulle
        folium.Marker(
            location=[lat, lon],
            popup=f"<strong>{name}</strong><br>Adresse : {adresse}<br>Niveau : {niveau}",
            icon=folium.Icon(color="blue", icon="home", prefix="fa"),
        ).add_to(m)

    niv_moy = niv_moy/nb_salles

    st.markdown(f"Nombre de salles : {nb_salles}")
    st.markdown(f"Niveau moyen : {niv_moy}", help="La note est sur 7")
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
        st.markdown(f'<a href="http://localhost:8501/Menu?city1={ville_1}&city2={ville_2}" class="custom-button" style="color: inherit; text-decoration: none;" target="_self">Retour au menu</a> ', unsafe_allow_html=True)

    with c2 :
        st.markdown(f'<a href="http://localhost:8501/Accueil?" class="custom-button" style="color: inherit; text-decoration: none;" target="_self">Comparer autres villes</a> ', unsafe_allow_html=True)
   
    st.title("Comparaison des salles de combat")


    liste_villes = ville_1, ville_2
    ville = st.selectbox("Choississez une ville : ", sorted(liste_villes), index=0, help="Sélectionnez la première ville à comparer.")

    define_map(ville, weather_api_key)



if __name__ == "__main__":
    main()
