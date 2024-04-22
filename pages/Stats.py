#Importer les librairies
import streamlit as st
import requests
import pandas as pd

def recup_data(ville, data) :
    city_data = data[data["Ville"] == ville]
    return city_data 

def main() :
    st.set_page_config(
        initial_sidebar_state="collapsed"
    )
    
    data = pd.read_csv("Donnees/outil_decisionnels.csv", delimiter=";")
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

    st.markdown(page_bg_img, unsafe_allow_html=True)


    c1,c2,c3 = st.columns(3)
    with c1 :
        st.markdown(f'<a href="http://localhost:8501/Menu?city1={ville_1}&city2={ville_2}" class="custom-button" style="color: inherit; text-decoration: none;" target="_self">Retour au menu</a> ', unsafe_allow_html=True)

    with c2 :
        st.markdown(f'<a href="http://localhost:8501/Accueil?" class="custom-button" style="color: inherit; text-decoration: none;" target="_self">Comparer autres villes</a> ', unsafe_allow_html=True)
   

    st.title("Données générales")

    recup_data(ville_2, data)

    c1,c2 = st.columns(2)
    with c1:
        st.title(ville_1)

    with c2 :
        st.title(ville_2)

    c1,c2 = st.columns(2)
    with c1:
        population = recup_data(ville_1, data)["POP"].values[0]
        superficie = recup_data(ville_1, data)["SUPERF"].values[0]
        naissance = recup_data(ville_1, data)["NAIS1420"].values[0]
        deces = recup_data(ville_1, data)["DECE1420"].values[0]
        menage = recup_data(ville_1, data)["MEN"].values[0]
        logement = recup_data(ville_1, data)["LOG"].values[0]
        emploi = recup_data(ville_1, data)["EMPLT"].values[0]

        st.write(f"Population : {population}")
        st.write(f"Superficie : {superficie} km²")
        st.write(f"Naissance entre 2014 et 2020 : {naissance}")
        st.write(f"Deces entre 2014 et 2020 : {deces}")
        st.write(f"Menage : {menage}")
        st.write(f"Logement : {logement}")
        st.write(f"Emploi : {emploi}")


    with c2 :
        population = recup_data(ville_2, data)["POP"].values[0]
        superficie = recup_data(ville_2, data)["SUPERF"].values[0]
        naissance = recup_data(ville_2, data)["NAIS1420"].values[0]
        deces = recup_data(ville_2, data)["DECE1420"].values[0]
        menage = recup_data(ville_2, data)["MEN"].values[0]
        logement = recup_data(ville_2, data)["LOG"].values[0]
        emploi = recup_data(ville_2, data)["EMPLT"].values[0]

        st.write(f"Population : {population}")
        st.write(f"Superficie : {superficie} km²")
        st.write(f"Naissance entre 2014 et 2020 : {naissance}")
        st.write(f"Deces entre 2014 et 2020 : {deces}")
        st.write(f"Menage : {menage}")
        st.write(f"Logement : {logement}")
        st.write(f"Emploi : {emploi}")


        
if __name__ == "__main__":
    main()