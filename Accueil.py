import streamlit as st
import requests
import html
import pandas as pd
import os

def find_pdf_file(directory):
    # Parcourir le dossier
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Vérifier si le fichier est un fichier PDF
            if file.endswith(".pdf"):
                return os.path.join(root, file)
    return None

def main():
    st.set_page_config(
        initial_sidebar_state="collapsed"
    )

    # Définir l'image de fond
    page_bg_img = f"""
        <style>
        [data-testid="stAppViewContainer"] > .main {{
            background-image: url("https://images3.alphacoders.com/524/52427.jpg");
            background-size: cover;
            background-position: top left;
            background-repeat: no-repeat;
            background-attachment: local;
        }}
        </style>
    """

    # Afficher l'image de fond
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Titre et en-tête
    st.markdown('<h1 style="color: #FF3B24; margin-top: 47px; text-shadow: 2px 2px 5px #FFFB7C; margin-top:125px; text-align: center;">City Fighter - Comparateur de villes</h1>', unsafe_allow_html=True)
    # Sélection des villes
    st.markdown("---")
    st.markdown('<h2 style="color: #FFFB7C; text-shadow: 2px 2px 5px #FF3B24; text-align: center;">Choisissez vos combattants :</h2>', unsafe_allow_html=True)

    # Ajouter du CSS personnalisé pour le contour du menu déroulant
    st.markdown(
        """
        <style>
        .st-af, .st-ax {
            border-color: #FFFB7C !important;
            color: #BADDEC;
            font-weight : bolder;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    data = pd.read_csv("Donnees/outil_decisionnels.csv", delimiter=";")

    # Liste des villes
    liste_villes = data["Ville"]

    # Sélection des villes avec possibilité de saisie manuelle
    ville_1 = st.selectbox("Ville 1", [""] + sorted(liste_villes), index=0, help="Sélectionnez la première ville à comparer.")

    ville_2 = st.selectbox("Ville 2", [""] + sorted(liste_villes), index=0, help="Sélectionnez la deuxième ville à comparer.")

    st.markdown("""
        <style>
            .custom-button {
                color: #FF3B24;
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
                background-color: ##000000;
                box-shadow: 10px 10px 10px #FF3B24;
                font-weight : bolder;
                text-shadow: 2px 2px 5px #FFFFFF;
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Utilisation de la grille de mise en page pour rendre les éléments plus responsives
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f'<a href="https://city-fighting-brahim-ben-gilles.streamlit.app/Menu?city1={ville_1}&city2={ville_2}" class="custom-button" style="color: inherit; text-decoration: none;" target="_self">Fight !</a>', unsafe_allow_html=True)
    
    with col2:
        # Bouton de téléchargement du PDF
        #if st.button("Télécharger le rapport", key="rapport_button"):
            # Trouver le fichier PDF dans le répertoire spécifié
         #   pdf_file_path = find_pdf_file("Donnees/RAPPORT.pdf")

           # if pdf_file_path:
                # Afficher un lien pour télécharger le PDF
               # st.markdown(f'<a href="{pdf_file_path}" download="{os.path.basename(pdf_file_path)}">Cliquez ici pour télécharger le rapport PDF</a>', unsafe_allow_html=True)
         #   else:
              #  st.error("Aucun fichier PDF trouvé dans le dossier spécifié.")

if __name__ == "__main__":
    main()
