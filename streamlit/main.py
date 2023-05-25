# -*- coding: utf-8 -*-
# pylint: disable=
"""
Created by Jean-François Subrini on the 1st of April 2023.
Creation of a semantic segmentation using a HRNetV2 + OCR model (created in the Notebook 2 Scripts).
"""
import time
import streamlit as st
import numpy as np
from matplotlib import pyplot as plt


# Creating the title for all pages.
st.title(":blue[PROJET 10 - Développez une POC]")

# Creating the side bar with the logos and the pages to select.
st.sidebar.title(":blue[TABLEAU DE BORD]")
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.image("img_notebook/logo_dataspace.png", width=250)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
page_sel = st.sidebar.radio(
    "Pages", options=("Bienvenue", "Jeu de données", "Segmentation sémantique", "A propos du model SOTA"))
st.sidebar.markdown("<br><br><br><br>", unsafe_allow_html=True)
st.sidebar.image("img_notebook/streamlit_logo.png", width=150)

# Deleting the hamburger and the footer.
st.markdown("""
            <style>
            .css-nqowgj.edgvbvh3
            {
                visibility: hidden;
            }
            .css-h5rgaw.egzxvld1
            {
                visibility: hidden;
            }
            </style>
            """, unsafe_allow_html=True)

if page_sel == "Segmentation sémantique":
    st.header(":orange[Segmentation sémantique d'une image]")
    st.markdown("<br>", unsafe_allow_html=True)
    form = st.form("Form 1")
    img_selected = form.selectbox("Sélectionner une image : ",
                                  options=("img1", "img2", "img3"))
    submit_state = form.form_submit_button("Valider")
    if submit_state:
        st.success(f"Vous avez sélectionné l'image {img_selected} pour réaliser une \
            segmentation sémantique avec notre nouveau modèle.")
        st.success("Attendez 4 secondes pour compléter le processus.")
        # Progress bar completed in 4 seconds.
        bar = st.progress(0)
        progress_status = st.empty()
        for i in range(100):
            bar.progress(i + 1)
            progress_status.write(str(i + 1) + "%")
            time.sleep(4 / 100)
        time.sleep(3)
        bar.progress(0)

elif page_sel == "Jeu de données":
    st.header(":orange[Jeu de données]")
    st.image("img_notebook/logo_cityscapes.png", width=200)
    st.markdown("""
                Nous utilisons le **jeu de données de Cityscapes** du projet 10.<br>
                Il se concentre sur la compréhension sémantique des scènes de rue urbaines, 
                avec ses 5 000 images et masques de haute qualité.
                """, unsafe_allow_html=True)
    opt = st.radio("Sélectionner un graphique", options=(
        "Diagramme à bâtons", "Diagramme à bâtons horizontal", "Diagramme Camembert"))
    URL = "https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle"
    if opt == "Diagramme à bâtons":
        st.markdown("<h3 style='text-align: center;'>Diagramme à bâtons</h3>", unsafe_allow_html=True)
        fig = plt.figure()
        plt.style.use(URL)
        plt.bar(np.array([1,2,3,4,5]), np.array([1,2,3,4,5]) * 10)
        st.write(fig)
    elif opt == "Diagramme à bâtons horizontal":
        st.markdown("<h3 style='text-align: center;'>Diagramme à bâtons horizontal</h3>", unsafe_allow_html=True)
        fig = plt.figure()
        plt.style.use(URL)
        plt.barh(np.array([1,2,3,4,5]) * 10, np.array([1,2,3,4,5]))
        st.write(fig)
    elif opt == "Diagramme Camembert":
        st.markdown("<h3 style='text-align: center;'>Diagramme Camembert</h3>", unsafe_allow_html=True)
        fig = plt.figure()
        plt.style.use(URL)
        plt.barh(np.array([1,2,3,4,5]) * 10, np.array([1,2,3,4,5]))
        st.write(fig)

elif page_sel == "A propos du model SOTA":
    st.header(":orange[Références bibliographiques et autres]")
    st.subheader(":orange[Articles de recherche]")
    st.markdown("""
                [**High-Resolution Representations for Labeling Pixels and Regions**](https://arxiv.org/pdf/1904.04514.pdf), 
                publié le 9 avril 2019.<br>
                [**Deep High-Resolution Representation Learning for Visual Recognition**](https://arxiv.org/pdf/1908.07919.pdf), 
                publié le 13 mars 2020.<br>
                [**Segmentation Transformer: Object-Contextual Representations for Semantic Segmentation**](https://arxiv.org/pdf/1909.11065.pdf), publié le 30 avril 2021.
                """, unsafe_allow_html=True)
    st.subheader(":orange[Site web de Jingdong Wang]")
    st.image("img_notebook/Jingdong_Wang.png", width=100)
    st.markdown("""
                [Site web de Jingdong Wang](https://jingdongwang2017.github.io/Projects/HRNet/), 
                Principal Research Manager de Microsoft Research Lab - Asia, à l’origine des modèles HRNet.
                """)
    st.subheader(":orange[Implémentation PyTorch des différents modèles HRNet]")
    st.markdown("""
                Site GitHub [HRNet-Semantic-Segmentation](https://github.com/HRNet/HRNet-Semantic-Segmentation)
                """)
    st.markdown("----")
    st.subheader(":orange[TensorFlow Advanced Segmentation Models]")
    st.markdown("<br>", unsafe_allow_html=True)
    st.image("img_notebook/tasm.png", width=250)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
                Nous avons utilisé 
                [TASM, de Jan Marcel Kezmann](https://github.com/JanMarcelKezmann/TensorFlow-Advanced-Segmentation-Models), 
                « ***A Python Library for High-Level Semantic Segmentation Models*** », 
                pour la création du modèle HRNetV2 + OCR.
                """)
    st.markdown("----")
    st.markdown("***[Mon repository GitHub du projet 10](https://github.com/jfsubrini/ai-project-10)***")


else:
    st.header(":orange[Test d’un nouveau modèle de segmentation sémantique]")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
              Pour cette **preuve de concept (POC)**, nous reprenons le **Projet 8** du parcours de formation 
              « Ingénieur IA » d’OpenClassrooms : **Participez à la conception d'une voiture autonome**.
              """)
    st.markdown("""
              Suite à une veille technologique nous avons choisi un nouveau modèle *state-of-the-art* récent 
              pour **améliorer la performance du modèle de segmentation sémantique** : le modèle **HRNetV2 + OCR**.
              """)
    st.markdown("""
                Rappelons que la **segmentation sémantique** est le **classement de chaque pixel selon la classe de l'objet 
                auquel il appartient** (humain, véhicule, construction, ciel, etc.) et les différents objets
                d'une même classe ne sont pas distingués. Ce travail est utilisé par les véhicules autonomes
                pour **comprendre leur environnement**.
                """)
