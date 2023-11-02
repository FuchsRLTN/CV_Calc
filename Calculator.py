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
    st.write("**Bruttoertrag pro Neuwagen:**")
    st.write("2.080 EUR (26.000 € x 8%)")
    st.write("")
    st.write("")
    st.write("**Bruttoertrag im Service p. a.:**")
    st.write("462 € (ca. 1.100 € Umsatz Lohn + Teile x 42%)")

    sales_clv = 2080
    service_clv = 462
    total_clv = 5776
    
else:
    st.write("**Bruttoertrag pro Neuwagen berechnen:**")
    sales_avg_ncprice = st.slider("Durschnittlicher NW-Preis (in EUR) festlegen", min_value=10000, max_value=30000, value=26000, step=500)
    sales_avg_margin = st.slider("Durchschnittliche Marge (%) festlegen", min_value=1, max_value=10, value=8, step=1)
    sales_clv = sales_avg_ncprice / 100 * sales_avg_margin
    st.write("")
    st.write("")
    st.write("**Bruttoertrag im Service p.a. berechnen:**")
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
dealer_loyalty_improvement = st.slider("Kundenbindung erhöhen auf ... Jahre:", min_value=6, max_value=10, value=8, step=1)
st.write("")
st.divider()

st.write(sales_clv)
st.write(service_clv)



## Defining the lifetime

lifetime_churn = 5
lifetime_loyal = dealer_loyalty_improvement


## Calculating clv per churn and loyal custonmer 

total_clv_churn = sales_clv + (service_clv * lifetime_churn)
total_clv_loyal = sales_clv + (service_clv * lifetime_loyal)
total_clv_delta = total_clv_loyal - total_clv_churn

st.write(total_clv_churn)
st.write(total_clv_loyal)
st.write(total_clv_delta)



## Calculating clv per churn and loyal custonmer - per Year of lifetime


total_clv_churn_y1 = sales_clv + (service_clv * 1)
total_clv_churn_y2 = sales_clv + (service_clv * 2)
total_clv_churn_y3 = sales_clv + (service_clv * 3)
total_clv_churn_y4 = sales_clv + (service_clv * 4)
total_clv_churn_y5 = sales_clv + (service_clv * 5)
total_clv_churn_y6 = sales_clv + (service_clv * 5)
total_clv_churn_y7 = sales_clv + (service_clv * 5)
total_clv_churn_y8 = sales_clv + (service_clv * 5)
total_clv_churn_y9 = sales_clv + (service_clv * 5)
total_clv_churn_y10 = sales_clv + (service_clv * 5)

total_clv_loyal_y1 = sales_clv + (service_clv * 1)
total_clv_loyal_y2 = sales_clv + (service_clv * 2)
total_clv_loyal_y3 = sales_clv + (service_clv * 3)
total_clv_loyal_y4 = sales_clv + (service_clv * 4)
total_clv_loyal_y5 = sales_clv + (service_clv * 5)
total_clv_loyal_y6 = sales_clv + (service_clv * 6)
total_clv_loyal_y7 = sales_clv + (service_clv * 7)
total_clv_loyal_y8 = sales_clv + (service_clv * 8)
total_clv_loyal_y9 = sales_clv + (service_clv * 9)
total_clv_loyal_y10 = sales_clv + (service_clv * 10)

total_clv_delta_y1 = sales_clv + (service_clv * 1) - total_clv_churn_y1
total_clv_delta_y2 = sales_clv + (service_clv * 2) - total_clv_churn_y1
total_clv_delta_y3 = sales_clv + (service_clv * 3) - total_clv_churn_y1
total_clv_delta_y4 = sales_clv + (service_clv * 4) - total_clv_churn_y1
total_clv_delta_y5 = sales_clv + (service_clv * 5) - total_clv_churn_y1
total_clv_delta_y6 = sales_clv + (service_clv * 6) - total_clv_churn_y1
total_clv_delta_y7 = sales_clv + (service_clv * 7) - total_clv_churn_y1
total_clv_delta_y8 = sales_clv + (service_clv * 8) - total_clv_churn_y1
total_clv_delta_y9 = sales_clv + (service_clv * 9) - total_clv_churn_y1
total_clv_delta_y10 = sales_clv + (service_clv * 10) - total_clv_churn_y1



## Calculating equity for total customer base - churn and loyal custonmer 

bestand_equity_churn = dealer_jvz * total_clv_churn
bestand_equity_loyal = dealer_jvz * total_clv_loyal
bestand_equity_delta = bestand_equity_loyal - bestand_equity_churn

st.write(bestand_equity_churn)
st.write(bestand_equity_loyal)
st.write(bestand_equity_delta)


bestand_equity_churn_y1 = dealer_jvz * total_clv_churn_y1
bestand_equity_churn_y2 = dealer_jvz * total_clv_churn_y2
bestand_equity_churn_y3 = dealer_jvz * total_clv_churn_y3
bestand_equity_churn_y4 = dealer_jvz * total_clv_churn_y4
bestand_equity_churn_y5 = dealer_jvz * total_clv_churn_y5
bestand_equity_churn_y6 = dealer_jvz * total_clv_churn_y6
bestand_equity_churn_y7 = dealer_jvz * total_clv_churn_y7
bestand_equity_churn_y8 = dealer_jvz * total_clv_churn_y8
bestand_equity_churn_y9 = dealer_jvz * total_clv_churn_y9
bestand_equity_churn_y10 = dealer_jvz * total_clv_churn_y10


bestand_equity_loyal_y1 = dealer_jvz * total_clv_loyal_y1
bestand_equity_loyal_y2 = dealer_jvz * total_clv_loyal_y2
bestand_equity_loyal_y3 = dealer_jvz * total_clv_loyal_y3
bestand_equity_loyal_y4 = dealer_jvz * total_clv_loyal_y4
bestand_equity_loyal_y5 = dealer_jvz * total_clv_loyal_y5
bestand_equity_loyal_y6 = dealer_jvz * total_clv_loyal_y6
bestand_equity_loyal_y7 = dealer_jvz * total_clv_loyal_y7
bestand_equity_loyal_y8 = dealer_jvz * total_clv_loyal_y8
bestand_equity_loyal_y9 = dealer_jvz * total_clv_loyal_y9
bestand_equity_loyal_y10 = dealer_jvz * total_clv_loyal_y10


bestand_equity_delta_y1 = dealer_jvz * total_clv_delta_y1
bestand_equity_delta_y2 = dealer_jvz * total_clv_delta_y2
bestand_equity_delta_y3 = dealer_jvz * total_clv_delta_y3
bestand_equity_delta_y4 = dealer_jvz * total_clv_delta_y4
bestand_equity_delta_y5 = dealer_jvz * total_clv_delta_y5
bestand_equity_delta_y6 = dealer_jvz * total_clv_delta_y6
bestand_equity_delta_y7 = dealer_jvz * total_clv_delta_y7
bestand_equity_delta_y8 = dealer_jvz * total_clv_delta_y8
bestand_equity_delta_y9 = dealer_jvz * total_clv_delta_y9
bestand_equity_delta_y10 = dealer_jvz * total_clv_delta_y10


## Calculating equity for total customer base - churn and loyal custonmer - per Year of lifetime





data = [bestand_equity_churn, bestand_equity_loyal] 
chart_data = pd.DataFrame(data)

st.dataframe(data)

st.bar_chart(data=chart_data)

st.divider()

st.write("line for new push")

