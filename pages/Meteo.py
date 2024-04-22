#Importer les librairies
import streamlit as st
import requests

def get_weather_data(lat, lon, weather_api_key) :
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    lat,lon = str(lat), str(lon)
    complete_url = base_url + "lat=" + lat + "&lon=" + lon + "&units=metric" + "&lang=fr" + "&appid=" + weather_api_key
    response = requests.get(complete_url)
    return response.json()

def get_city_coordinates(city, weather_api_key):
    base_url = "http://api.openweathermap.org/geo/1.0/direct?q="
    complete_url = base_url + city + ",FR&limit=1" + "&appid=" + weather_api_key
    response = requests.get(complete_url)
    return response.json()

def get_image_url(data) :
    iconid = data['weather'][0]['icon']
    base_url = f"https://openweathermap.org/img/wn/{iconid}@2x.png"
    return base_url


def main() :
    st.set_page_config(
        initial_sidebar_state="collapsed"
    )
    
    weather_api_key = st.secrets["weather_api_key"]
    ville_1 = st.query_params["city1"]
    ville_2 = st.query_params["city2"]

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
   
    st.title("Comparaison de la météo")

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
    #API
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Définir le style de la page
    st.markdown(
        """
        <style>
        /* Définir la couleur du texte */
        .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6 {
            color: #FFFB7C;
            text-shadow: 2px 2px 5px #C70039;
        }

        .blur-background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            filter: blur(80px);
            background-color: rgba(255, 255, 255, 0.5); /* Couleur de fond semi-transparente */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="blur-background"></div>', unsafe_allow_html=True)

    if ville_1 == "" or ville_2 == "" :
        st.error("Veuillez sélectionner deux villes depuis la page d'accueil.")
    else :
        with st.spinner("Chargement des données météo..."):
            coordinates_data = get_city_coordinates(ville_1, weather_api_key)
            weather_data = get_weather_data(coordinates_data[0]["lat"],coordinates_data[0]["lon"], weather_api_key)

            coordinates_data2 = get_city_coordinates(ville_2, weather_api_key)
            weather_data2 = get_weather_data(coordinates_data2[0]["lat"],coordinates_data2[0]["lon"], weather_api_key)

        #Voir si la ville a été trouvé et afficher les données météo
        if weather_data.get("cod") != 404 and weather_data2.get("cod") != 404:
            c1,c2 = st.columns(2)
            with c1:
                st.title(ville_1)
                st.image(get_image_url(weather_data))
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Température ", f"{weather_data['main']['temp']:.2f} °C")
                    st.metric("Humidité ", f"{weather_data['main']['humidity']} %")
                with col2:
                    st.metric("Pression ", f"{weather_data['main']['pressure']} hPa")
                    st.metric("Vitesse du vent ", f"{weather_data['wind']['speed']} m/s")
            with c2 :
                st.title(ville_2)
                st.image(get_image_url(weather_data2))
                col1, col2 = st.columns(2)
                with col1:
                    st.metric("Température ", f"{weather_data2['main']['temp']:.2f} °C")
                    st.metric("Humidité ", f"{weather_data2['main']['humidity']} %")
                with col2:
                    st.metric("Pression ", f"{weather_data2['main']['pressure']} hPa")
                    st.metric("Vitesse du vent ", f"{weather_data2['wind']['speed']} m/s")

        #Generer et afficher une description
        #weather_description = generate_weather_description(weather_data, openai_api_key)
        #st.write(weather_description)
        else :
            #Afficher un message d'erreur si la ville n'a pas été trouvé
            st.error("Ville non trouvé")


if __name__ == "__main__":
    main()
