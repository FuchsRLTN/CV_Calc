import streamlit as st


## App Header

## st.titel("Hello World 2")


## Config Dealer Data

dealer_jvz = st.slider("JVZ eingeben:", min_value=1, max_value=1000, value=300, step=50)
st.write(dealer_jvz)



