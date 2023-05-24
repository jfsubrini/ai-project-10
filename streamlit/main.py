import time
import streamlit as st
import numpy as np
from matplotlib import pyplot as plt


# Creating the title for all pages.
st.header(":blue[PROJET 10 - Développez une preuve de concept]")
st.subheader(":orange[Test d’un nouveau modèle de segmentation sémantique]")

# Creating the side bar with the logo and the pages to select.
st.sidebar.title(":blue[Tableau de bord]")
st.sidebar.markdown("<br>", unsafe_allow_html=True)
st.sidebar.image("img_notebook/logo_dataspace.png", width=250)
st.sidebar.markdown("<br>", unsafe_allow_html=True)
page_sel = st.sidebar.radio(
    "Pages", options=("Home", "Jeu de données", "Segmentation sémantique", "A propos du model SOTA"))


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
    st.markdown("<h2 style='text-align: center;'>Sélection d'une image pour la segmentation sémantique</h2>",
                unsafe_allow_html=True)
    form = st.form("Form 1")
    img_selected = form.selectbox("Select an image : ",
                                  options=("img1", "img2", "img3"))
    submit_state = form.form_submit_button("Submit")
    if submit_state:
        st.success(f"You have selected the {img_selected} image now let's make \
            a semantic segmentation on it with our model.")
        st.success("Just wait for 4 seconds to complete the process.")
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
    st.image("img_notebook/logo_cityscapes.png", width=300)
    st.markdown("""
                Nous utiliserons le même jeu de données de Cityscapes qui se concentre 
                sur la compréhension sémantique des scènes de rue urbaines, 
                avec ses 5 000 images et masques de haute qualité.
                """)
    opt = st.radio("Sélectionner un graphique", options=("Lignes", "Bar", "Camembert"))
    URL = "https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle"
    if opt == "Line":
        st.markdown("<h3 style='text-align: center;'>Line graph</h3>", unsafe_allow_html=True)
        fig = plt.figure()
        plt.style.use(URL)
        plt.plot(np.linspace(0,10,100), np.sin(np.linspace(0,10,100)))
        plt.plot(np.linspace(0,10,100), np.cos(np.linspace(0,10,100)), '--')
        st.write(fig)
    elif opt == "Bar":
        st.markdown("<h3 style='text-align: center;'>Bar graph</h3>", unsafe_allow_html=True)
        fig = plt.figure()
        plt.style.use(URL)
        plt.bar(np.array([1,2,3,4,5]), np.array([1,2,3,4,5]) * 10)
        st.write(fig)
    elif opt == "Pie":
        st.markdown("<h3 style='text-align: center;'>Camembert</h3>", unsafe_allow_html=True)
        fig = plt.figure()
        plt.style.use(URL)
        plt.barh(np.array([1,2,3,4,5]) * 10, np.array([1,2,3,4,5]))
        st.write(fig)

elif page_sel == "A propos du model HRNetV2 + OCR":
    st.image("img_notebook/tasm.png", caption="This is thddc", width=300)
    st.markdown("----")
    st.markdown("[HRNet](https://github.com/HRNet/HRNet-Semantic-Segmentation)")
    st.markdown("[My GitHub](https://github.com/jfsubrini/ai-project-10)")

else:
    st.markdown("""
              Pour cette **preuve de concept (POC)**, nous reprenons le **Projet 8** du parcours de formation 
              « Ingénieur IA » d’OpenClassrooms : **Participez à la conception d'une voiture autonome**.
              """)
    st.markdown("""
              Suite à une veille technologique afin de trouver une méthode récente pour **améliorer
              la performance du modèle de segmentation sémantique**, il s’agit ici d’expliquer et de 
              démontrer l’apport de ce nouveau modèle state-of-the-art, le **HRNetV2 + OCR**.
              """)
