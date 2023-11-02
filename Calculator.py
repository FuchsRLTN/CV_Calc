import streamlit as st
import pandas as pd


## App Header

st.image("https://i.postimg.cc/qMBkK4nX/HMD-Header-2.png")
st.write("")
st.write("")


## Customer Value: Calculation

st.image("https://i.postimg.cc/DwCd9dFt/HMD-H3-Kunden-1.png")

toggle_clvcalc = st.toggle('Individuell berechnen')
st.write("")


if toggle_clvcalc is False:
    st.write("Bruttoertrag pro Neuwagen:")
    st.write("2.080 EUR (26.000 € x 8%)")
    st.write("")
    st.write("")
    st.write("Bruttoertrag im Service p. a.:")
    st.write("462 € (ca. 1.100 € Umsatz Lohn + Teile x 42%)")

    sales_clv = 2080
    service_clv = 462
    total_clv = 5776
    
else:
    st.write("Bruttoertrag pro Neuwagen berechnen:")
    sales_avg_ncprice = st.slider("Durschnittlicher NW-Preis (in EUR) festlegen", min_value=10000, max_value=30000, value=26000, step=500)
    sales_avg_margin = st.slider("Durchschnittliche Marge (%) festlegen", min_value=1, max_value=10, value=8, step=1)
    sales_clv = sales_avg_ncprice / 100 * sales_avg_margin
    st.write("")
    st.write("")
    st.write("Bruttoertrag im Service p.a. berechnen:")
    service_avg_revenue = st.slider("Durschnittlicher Umsatz L&T (p.A.; in EUR) festlegen", min_value=0, max_value=5000, value=1100, step=50)
    service_avg_margin = st.slider("Durchschnittliche Marge (%) festlegen", min_value=1, max_value=100, value=42, step=1)
    service_clv = service_avg_revenue / 100 * service_avg_margin

    st.write(sales_clv)
    st.write(service_clv)

    lifetime = 8
    total_clv = sales_clv + (lifetime * service_clv)
 


## Customer Value: Result

st.write("")
st.write("")

clv_str = str(total_clv) + " Euro pro Kunde"
st.info(clv_str)
st.caption("Durchschnittlicher Ertrag erwirtschaftet pro Kunde nach 8 Jahren")

st.write("")
st.write("")
st.divider()
st.write("")
st.write("")




## Customer Equity: Calculation

st.image("https://i.postimg.cc/26g0Pddz/HMD-H3-Bestand-1.png")
st.write("")
st.write("")

## Config Dealer Data
st.write("")
st.write("")

dealer_jvz = st.slider("JVZ eingeben:", min_value=1, max_value=1000, value=300, step=50)
dealer_loyalty_improvement = st.slider("Kundenbindung erhöhen auf:", min_value=6, max_value=10, value=8, step=1)
st.write("")
st.divider()

st.write(sales_clv)
st.write(service_clv)

lifetime_churn = 5
lifetime_loyal = 10

total_clv_churn = sales_clv + (service_clv * lifetime_churn)
total_clv_loyal = sales_clv + (service_clv * lifetime_loyal)
total_clv_delta = total_clv_loyal - total_clv_churn

st.write(total_clv_churn)
st.write(total_clv_loyal)
st.write(total_clv_delta)

bestand_equity_churn = dealer_jvz * total_clv_churn
bestand_equity_loyal = dealer_jvz * total_clv_loyal
bestand_equity_delta = bestand_equity_loyal - bestand_equity_churn

st.write(bestand_equity_churn)
st.write(bestand_equity_loyal)
st.write(bestand_equity_delta)

data = [bestand_equity_churn, bestand_equity_loyal] 
chart_data = pd.DataFrame(data)

st.dataframe(data)

st.bar_chart(data=chart_data)

st.divider()

st.write("line for new push")

