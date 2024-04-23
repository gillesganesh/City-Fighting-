#Importer les librairies
import streamlit as st
import requests
import html

def main():
    st.set_page_config(
        initial_sidebar_state="collapsed"
    )
    
    ville_1 = st.query_params["city1"]
    ville_2 = st.query_params["city2"]

    # Balises HTML pour centrer le contenu et ajuster la taille du texte
    st.write(f"<div style='text-align: center;'><span style='font-size: 34px; color: #FF5733; text-shadow: 2px 2px 5px #FBFF80;'>{ville_1}</span> <img src='https://upload.wikimedia.org/wikipedia/commons/7/70/Street_Fighter_VS_logo.png' width='50px'> <span style='font-size: 34px; color: #FF5733; text-shadow: 2px 2px 5px #FBFF80;'>{ville_2}</span></div>", unsafe_allow_html=True)

    # Définir l'image de fond
    page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
            background-image: url("https://media.eventhubs.com/images/2017/07/14_sf5evostagecostumes03.jpg");
            background-size: cover;
            background-position: top left;
            background-repeat: no-repeat;
            background-attachment: local;
        }}
        </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.markdown("""
        <style>
            .retour-button {
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
            .retour-button:hover {
                color: #FF3B24;
                box-shadow: 10px 10px 10px #FF3B24;
                font-weight : bolder;
                text-shadow: 2px 2px 5px #FFFFFF;
            }
        </style>
    """, unsafe_allow_html=True)

    
    st.markdown("""
        <style>
            .custom-button {
                color: #FFFB7C;
                padding: 60px 120px;
                border-radius: 5px;
                border: none;
                cursor: pointer;
                box-shadow: 2px 2px 5px #FFFB7C;
                font-weight : bolder;
                display: block;
                margin: 0 auto;
                font-size: 22px;
                text-shadow: 2px 2px 5px #000000;
            }
            .custom-button:hover {
                color: #FF3B24;
                box-shadow: 10px 10px 10px #FF3B24;
                font-weight : bolder;
                text-shadow: 2px 2px 5px #FFFFFF;
            }
            .meteo-button {
                background-image: url("https://media.zenfs.com/fr/programme_tv_fr_account_146/5f94c71fcfe8675c6325a9eaae699f5f"); 
                background-size: cover;
            }
            .combat-button {
                background-image: url("https://i.pinimg.com/originals/bc/ad/d8/bcadd85dd7e18e70165bc1fd1fcfc16f.jpg"); 
                background-size: cover;
            }
            .emploi-button {
                background-image: url("https://images.rtl.fr/~c/770v513/rtl/www/1205492-logo-pole-emploi-illustration.jpg"); 
                background-size: cover;
            }
            .logement-button {
                background-image: url("https://mir-s3-cdn-cf.behance.net/project_modules/1400/dd0c0a69578469.5b864c07b31c9.jpg"); 
                background-size: cover;
            }
        </style>
    """, unsafe_allow_html=True)

#    c1,c2,c3 = st.columns(3)
#    with c1 :
#        st.markdown(f'<a href="http://localhost:8501/Stats?city1={ville_1}&city2={ville_2}" class="retour-button" style="color: inherit; text-decoration: none;" target="_self">Données générales</a> ', unsafe_allow_html=True)    
#
#    col1, col2 = st.columns(2)
#    with col1 :
#        st.markdown(f'<a href="http://localhost:8501/Meteo?city1={ville_1}&city2={ville_2}" class="custom-button meteo-button" style="color: inherit; text-decoration: none;" target="_self">Meteo</a> ', unsafe_allow_html=True)
#        st.markdown(f'<a href="http://localhost:8501/Logements?city1={ville_1}&city2={ville_2}" class="custom-button logement-button" style="color: inherit; text-decoration: none;" target="_self">Logement</a>', unsafe_allow_html=True)
#
#    with col2  :
#        st.markdown(f'<a href="http://localhost:8501/Emploi?city1={ville_1}&city2={ville_2}" class="custom-button emploi-button" style="color: inherit; text-decoration: none;" target="_self">Emploi</a>', unsafe_allow_html=True)
#        st.markdown(f'<a href="http://localhost:8501/Combat?city1={ville_1}&city2={ville_2}" class="custom-button combat-button" style="color: inherit; text-decoration: none;" target="_self">Combat</a>', unsafe_allow_html=True)
#
#    c1,c2,c3 = st.columns(3)
#    with c1 :
#        st.markdown(f'<a href="http://localhost:8501/Accueil" class="retour-button" style="color: inherit; text-decoration: none;" target="_self">Comparer autres villes</a> ', unsafe_allow_html=True)    

if __name__ == "__main__":
    main()
