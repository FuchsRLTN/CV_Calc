import streamlit as st


## App Header



## Config Dealer Data

dealer_jvz = st.slider("JVZ eingeben:", min_value=1, max_value=1000, value=300, step=50)
dealer_bevshare = st.slider("Anteil EV eingeben:", min_value=1, max_value=100, value=30, step=1)
st.write("")
st.divider()




## Customer Value

clv_ev = 2500
clv_ice = 5776


st.header("Kundenwert:")

col1, col2 = st.columns(2)

with col1:
    st.metric(label="EV-Kunde", value=clv_ev)

with col2:
    st.metric(label="ICE-Kunde", value=clv_ice)




## Details CLV Calculation as an expander

with st.expander("Kundenwert neu berechnen:"):
    sales_avg_ncprice = st.number_input("Durschnittlicher NW-Preis festlegen")
    sales_avg_margin = st.number_input("Durchschnittliche Marge festlegen")
    sales_grprofit_customer = sales_avg_margin / 100 * sales_avg_margin
    st.write(sales_grprofit_customer)
