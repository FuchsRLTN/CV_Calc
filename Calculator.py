import streamlit as st


## App Header

st.image("https://i.postimg.cc/qMBkK4nX/HMD-Header-2.png")
st.write("")
st.write("")


## Customer Value


st.header("Was ist ein Kunde wert?")
toggle_clvcalc = st.toggle('Individuell berechnen')

if toggle_clvcalc:
    sales_avg_ncprice = st.slider("Durschnittlicher NW-Preis (in EUR) festlegen", min_value=10000, max_value=30000, step=500)
    sales_avg_margin = st.slider("Durchschnittliche Marge (%) festlegen", min_value=1, max_value=10, step=1)
    sales_clv = sales_avg_ncprice / 100 * sales_avg_margin

    service_avg_revenue = st.slider("Durschnittlicher Umsatz L&T (p.A.; in EUR) festlegen", min_value=0, max_value=5000, step=50)
    service_avg_margin = st.slider("Durchschnittliche Marge (%) festlegen", min_value=1, max_value=100, step=1)
    service_clv = service_avg_revenue / 100 * service_avg_margin

    st.write(sales_clv)
    st.write(service_clv)

    lifetime = 8
    total_clv = sales_clv + (lifetime * service_clv)
 
else:
    st.write("Bruttoertrag pro Neuwagen: 2.080 EUR (26.000 € x 8%)")
    st.write("Bruttoertrag im Service p. a.: 462 € (ca. 1.100 € Umsatz Lohn + Teile x 42%)")
    total_clv = 5776

st.write("Nach 8 Jahren hat das Autohaus pro Kunde einen durchschnittlichen Ertrag von" )
st.metric("", total_clv)







## Config Dealer Data
st.write("")
st.write("")

dealer_jvz = st.slider("JVZ eingeben:", min_value=1, max_value=1000, value=300, step=50)
## dealer_bevshare = st.slider("Anteil EV eingeben:", min_value=1, max_value=100, value=30, step=1)
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
    sales_grprofit_customer = sales_avg_ncprice / 100 * sales_avg_margin
    st.write(sales_grprofit_customer)
