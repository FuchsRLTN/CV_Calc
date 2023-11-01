import streamlit as st


## App Header

st.image("https://i.postimg.cc/qMBkK4nX/HMD-Header-2.png")
st.write("")
st.write("")


## Customer Value Calculation


st.subheader("KUNDENWERT")



toggle_clvcalc = st.toggle('Individuell berechnen')
st.write("")


if toggle_clvcalc is False:
    st.write("Bruttoertrag pro Neuwagen:")
    st.write("2.080 EUR (26.000 € x 8%)")
    st.write("")
    st.write("Bruttoertrag im Service p. a.:")
    st.write("462 € (ca. 1.100 € Umsatz Lohn + Teile x 42%)")

    total_clv = 5776
    
else:
    sales_avg_margin = st.slider("Durchschnittliche Marge (%) festlegen", min_value=1, max_value=10, step=1)
    sales_avg_ncprice = st.slider("Durschnittlicher NW-Preis (in EUR) festlegen", min_value=10000, max_value=30000, step=500)
    sales_clv = sales_avg_ncprice / 100 * sales_avg_margin

    service_avg_revenue = st.slider("Durschnittlicher Umsatz L&T (p.A.; in EUR) festlegen", min_value=0, max_value=5000, step=50)
    service_avg_margin = st.slider("Durchschnittliche Marge (%) festlegen", min_value=1, max_value=100, step=1)
    service_clv = service_avg_revenue / 100 * service_avg_margin

    st.write(sales_clv)
    st.write(service_clv)

    lifetime = 8
    total_clv = sales_clv + (lifetime * service_clv)
 


## Customer Value Displaying

st.write("")
clv_str = str(total_clv) + " Euro pro Kunde"
st.info(clv_str)
st.caption("Durchschnittlicher Ertrag erwirtschaftet pro Kunde nach 8 Jahren")







## Config Dealer Data
st.write("")
st.write("")

dealer_jvz = st.slider("JVZ eingeben:", min_value=1, max_value=1000, value=300, step=50)
## dealer_bevshare = st.slider("Anteil EV eingeben:", min_value=1, max_value=100, value=30, step=1)
st.write("")
st.divider()


