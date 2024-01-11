import streamlit as st
import pandas as pd


## App Header

st.image("https://i.postimg.cc/d3h2135n/HMD-Header-3.png")
st.write("")
st.write("")


## Customer Value: Calculation

st.image("https://i.postimg.cc/DwCd9dFt/HMD-H3-Kunden-1.png")

toggle_clvcalc = st.toggle('Individuell berechnen')
st.write("")
st.write("")


if toggle_clvcalc is False:

    kunden_nc_col1_icon, kunden_nc_cal2_value = st.columns([0.1, 0.9])
    
    with kunden_nc_col1_icon:
        st.image("https://i.postimg.cc/pX3jYX6g/ICON-New-Car.png", width=50)
    
    with kunden_nc_cal2_value:
        st.write("**Bruttoertrag pro Neuwagen:**")
        st.write("2.080 EUR")
        st.caption("(26.000 € x 8%)")

    st.divider()


    kunden_as_col1_icon, kunden_as_cal2_value = st.columns([0.1, 0.9])
    with kunden_as_col1_icon:
        st.image("https://i.postimg.cc/DmVJ7SrL/ICON-Test.png", width=50)
    with kunden_as_cal2_value:
        st.write("**Bruttoertrag im Service p. a.:**")
        st.write("462 €")
        st.caption("(ca. 1.100 € Umsatz Lohn + Teile x 42%)")


    sales_clv = 2080
    service_clv = 462
    total_clv = 5776
    
else:

    kunden_nc_col1_icon, kunden_nc_cal2_value = st.columns([0.1, 0.9])
    
    with kunden_nc_col1_icon:
        st.image("https://i.postimg.cc/pX3jYX6g/ICON-New-Car.png", width=50)

    with kunden_nc_cal2_value:   
        st.write("**Bruttoertrag pro Neuwagen berechnen:**")
        sales_avg_ncprice = st.slider("Durschnittlicher NW-Preis (in EUR) festlegen", min_value=10000, max_value=30000, value=26000, step=500)
        sales_avg_margin = st.slider("Durchschnittliche Marge (%) festlegen", min_value=1, max_value=10, value=8, step=1)
        sales_clv = sales_avg_ncprice / 100 * sales_avg_margin
    

    st.divider()
    

    kunden_as_col1_icon, kunden_as_cal2_value = st.columns([0.1, 0.9])

    with kunden_as_col1_icon:
        st.image("https://i.postimg.cc/DmVJ7SrL/ICON-Test.png", width=50)
    
    with kunden_as_cal2_value:
        st.write("**Bruttoertrag im Service p.a. berechnen:**")
        service_avg_revenue = st.slider("Durschnittlicher Umsatz L&T (p.A.; in EUR) festlegen", min_value=0, max_value=5000, value=1100, step=50)
        service_avg_margin = st.slider("Durchschnittliche Marge (%) festlegen", min_value=1, max_value=100, value=42, step=1)
        service_clv = service_avg_revenue / 100 * service_avg_margin

    ## st.write(sales_clv)
    ## st.write(service_clv)

    lifetime = 8
    total_clv = sales_clv + (lifetime * service_clv)
 


## Customer Value: Result

st.write("")
st.write("")

kunden_wert_col1_icon, kunden_wert_col2_value = st.columns([0.1, 0.9])

with kunden_wert_col1_icon:
    st. image("https://i.postimg.cc/RVbwFTFq/ICON-Kundenwert-5.png", width=50)

with kunden_wert_col2_value:
    st. image("https://i.postimg.cc/4NKm8RfN/image-42.png", width=50)
    clv_str = str(total_clv) + " Euro p. Kunde"
    st.info(clv_str)
    st.caption("Durchschnittlicher Ertrag pro Kunde und 8 Jahren Bindung")

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

dealer_jvz = st.slider("JVZ eingeben:", min_value=1, max_value=1000, value=100, step=50)
dealer_loyalty_improvement = st.slider("Kundenbindung erhöhen auf ... Jahre:", min_value=6, max_value=10, value=8, step=1)
st.write("")
st.divider()

## st.write(sales_clv)
## st.write(service_clv)



## Defining the lifetime

lifetime_churn = 5
lifetime_loyal = dealer_loyalty_improvement


## Calculating clv per churn and loyal custonmer 

total_clv_churn = sales_clv + (service_clv * lifetime_churn)
total_clv_loyal = sales_clv + (service_clv * lifetime_loyal)
total_clv_delta = total_clv_loyal - total_clv_churn

## st.write(total_clv_churn)
## st.write(total_clv_loyal)
## st.write(total_clv_delta)



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
total_clv_delta_y2 = sales_clv + (service_clv * 2) - total_clv_churn_y2
total_clv_delta_y3 = sales_clv + (service_clv * 3) - total_clv_churn_y3
total_clv_delta_y4 = sales_clv + (service_clv * 4) - total_clv_churn_y4
total_clv_delta_y5 = sales_clv + (service_clv * 5) - total_clv_churn_y5
total_clv_delta_y6 = sales_clv + (service_clv * 6) - total_clv_churn_y6
total_clv_delta_y7 = sales_clv + (service_clv * 7) - total_clv_churn_y7
total_clv_delta_y8 = sales_clv + (service_clv * 8) - total_clv_churn_y8
total_clv_delta_y9 = sales_clv + (service_clv * 9) - total_clv_churn_y9
total_clv_delta_y10 = sales_clv + (service_clv * 10) - total_clv_churn_y10



## Calculating equity for total customer base - churn and loyal custonmer 

bestand_equity_churn = dealer_jvz * total_clv_churn
bestand_equity_loyal = dealer_jvz * total_clv_loyal
bestand_equity_delta = bestand_equity_loyal - bestand_equity_churn

## st.write(bestand_equity_churn)
## st.write(bestand_equity_loyal)
## st.write(bestand_equity_delta)


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


## Creating the data frames for bar chart

data_peryear = {
    ## "Jahr": ["1.Jahr", "2.Jahr", "3.Jahr","4.Jahr", "5.Jahr", "6.Jahr","7.Jahr", "8.Jahr", "9.Jahr","10.Jahr"],
    "Bruttoertrag V&S - Abwanderung": [bestand_equity_churn_y1, bestand_equity_churn_y2, bestand_equity_churn_y3, bestand_equity_churn_y4, bestand_equity_churn_y5, bestand_equity_churn_y6, bestand_equity_churn_y7, bestand_equity_churn_y8, bestand_equity_churn_y9, bestand_equity_churn_y10],
    "Zusätzlicher Bruttoertrag": [bestand_equity_delta_y1, bestand_equity_delta_y2, bestand_equity_delta_y3, bestand_equity_delta_y4, bestand_equity_delta_y5, bestand_equity_delta_y6, bestand_equity_delta_y7, bestand_equity_delta_y8, bestand_equity_delta_y9, bestand_equity_delta_y10],
    ## "Bruttoertrag V&S - Gebunden": [bestand_equity_loyal_y1, bestand_equity_loyal_y2, bestand_equity_loyal_y3, bestand_equity_loyal_y4, bestand_equity_loyal_y5, bestand_equity_loyal_y6, bestand_equity_loyal_y7, bestand_equity_loyal_y8, bestand_equity_loyal_y9, bestand_equity_loyal_y10]
}

print("**Ihr zusätzlicher ERTRAG durch längere Kundenbindung**" )

## Creating the bar chart 
st.bar_chart(data=data_peryear, color=["#002B5E", "#00AAD2"])






## Customer Equity: Result

st.write("")
st.write("")

equity_upside = str(dealer_jvz) + " Kunden länger binden ergibt einen Zusatzertrag von: " + str(bestand_equity_delta_y10) + "Euro"
st.info(equity_upside)
st.caption("Errechnet auf Basis der o.g. Werten und dem Jahresverkaufsziel (JVZ). Erwirtschaftet bei einer Bindung über 5 zusätzlichen Jahren")





st.write("")
st.write("")

kundenbestand_wert_col1_icon, kundenbestand_wert_col2_value = st.columns([0.1, 0.9])

with kundenbestand_wert_col1_icon:
    st. image("https://i.postimg.cc/P5rFGy7x/ICON-Kundenwert-4.png", width=50)

with kundenbestand_wert_col2_value:
    clv_str = str(total_clv) + " Euro p. Kunde"
    st.info(clv_str)
    st.caption("Durchschnittlicher Ertrag pro Kunde und 8 Jahren Bindung")

st.divider()
st.write("")
st.write("")





## Footer


st.divider()
st.write("")
st.write("")

st.image("https://i.postimg.cc/63MYXqSQ/HMD-Impressum.png")