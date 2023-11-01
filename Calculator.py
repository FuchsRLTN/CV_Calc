import streamlit as st


## App Header

## st.titel("Hello World 2")


## Config Dealer Data

dealer_jvz = st.slider("JVZ eingeben:", min_value=1, max_value=1000, value=300, step=50)
dealer_bevshare = st.slider("Anteil EV eingeben:", min_value=1, max_value=100, value=30, step=1)


## Details CLV Calculation as an expander

with st.expander("Details zur Kundenwertberechnung:"):
    st.header("Rechenweg")

    
