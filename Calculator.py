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
        st.write("2.864 EUR")
        st.caption("(35.800 € x 8%)")

    st.write("")
    st.write("")
    st.write("")
    st.write("")


    kunden_as_col1_icon, kunden_as_cal2_value = st.columns([0.1, 0.9])
    with kunden_as_col1_icon:
        st.image("https://i.postimg.cc/DmVJ7SrL/ICON-Test.png", width=50)
    with kunden_as_cal2_value:
        st.write("**Bruttoertrag im Service p. a.:**")
        st.write("462 €")
        st.caption("(ca. 1.100 € Umsatz Lohn + Teile x 42%)")


    sales_clv = 2864
    service_clv = 462
    total_clv = 6560
    
else:

    kunden_nc_col1_icon, kunden_nc_cal2_value = st.columns([0.1, 0.9])
    
    with kunden_nc_col1_icon:
        st.image("https://i.postimg.cc/pX3jYX6g/ICON-New-Car.png", width=50)

    with kunden_nc_cal2_value:   
        st.write("**Bruttoertrag pro Neuwagen berechnen:**")
        sales_avg_ncprice = st.slider("Durschnittlicher NW-Preis (in EUR) festlegen", min_value=10000, max_value=40000, value=35800, step=100)
        sales_avg_margin = st.slider("Durchschnittliche Marge (%) festlegen", min_value=1, max_value=10, value=8, step=1)
        sales_clv = sales_avg_ncprice / 100 * sales_avg_margin
    
    st.write("")
    st.write("")
    st.write("")
    st.write("")

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
st.write("")
st.write("")
st.write("")
st.write("")


kunden_wert_col1_icon, kunden_wert_col2_value = st.columns([0.1, 0.9])

with kunden_wert_col1_icon:
    st. image("https://i.postimg.cc/RVbwFTFq/ICON-Kundenwert-5.png", width=50)

with kunden_wert_col2_value:
    st. image("https://i.postimg.cc/4NKm8RfN/image-42.png", width=150)
    clv_str = str(total_clv) + " Euro p. Kunde"
    st.info(clv_str)
    st.caption("Durchschnittlicher Ertrag pro Kunde und 8 Jahren Bindung")

st.divider()
st.write("")
st.write("")
st.write("")
st.write("")




## Customer Equity: Calculation

st.image("https://i.postimg.cc/26g0Pddz/HMD-H3-Bestand-1.png")
st.write("")
st.write("")

## Config Dealer Data

dealer_jvz = st.slider("JVZ eingeben:", min_value=1, max_value=1000, value=100, step=50)
dealer_loyalty_improvement = st.slider("Kundenbindung erhöhen auf ... Jahre:", min_value=6, max_value=10, value=8, step=1)
st.write("")
st.write("")
st.write("")
st.write("")

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
if lifetime_loyal > 5:
    total_clv_churn_y6 = sales_clv + (service_clv * 5)
else:
    total_clv_churn_y6 = 0

if lifetime_loyal > 6:
    total_clv_churn_y7 = sales_clv + (service_clv * 5)
else:
    total_clv_churn_y7 = 0 

if lifetime_loyal > 7:
    total_clv_churn_y8 = sales_clv + (service_clv * 5)
else:
    total_clv_churn_y8 = 0 

if lifetime_loyal > 8:
    total_clv_churn_y9 = sales_clv + (service_clv * 5)
else:
    total_clv_churn_y9 = 0

if lifetime_loyal > 9:
    total_clv_churn_y10 = sales_clv + (service_clv * 5)
else:
    total_clv_churn_y10 = 0



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
if lifetime_loyal > 5:
    total_clv_delta_y6 = sales_clv + (service_clv * 6) - total_clv_churn_y6
else:
    total_clv_delta_y6 = 0
if lifetime_loyal > 6:
    total_clv_delta_y7 = sales_clv + (service_clv * 7) - total_clv_churn_y7
else:
    total_clv_delta_y7 = 0
if lifetime_loyal > 7:
    total_clv_delta_y8 = sales_clv + (service_clv * 8) - total_clv_churn_y8
else:
    total_clv_delta_y8 = 0
if lifetime_loyal > 8:
    total_clv_delta_y9 = sales_clv + (service_clv * 9) - total_clv_churn_y9
else:
    total_clv_delta_y9 = 0
if lifetime_loyal > 9:
    total_clv_delta_y10 = sales_clv + (service_clv * 10) - total_clv_churn_y10
else:
    total_clv_delta_y10 = 0


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






if lifetime_loyal > 5:
    total_clv_delta_y6 = sales_clv + (service_clv * 6) - total_clv_churn_y6
else:
    total_clv_delta_y6 = 0
if lifetime_loyal > 6:
    total_clv_delta_y7 = sales_clv + (service_clv * 7) - total_clv_churn_y7
else:
    total_clv_delta_y7 = 0
if lifetime_loyal > 7:
    total_clv_delta_y8 = sales_clv + (service_clv * 8) - total_clv_churn_y8
else:
    total_clv_delta_y8 = 0
if lifetime_loyal > 8:
    total_clv_delta_y9 = sales_clv + (service_clv * 9) - total_clv_churn_y9
else:
    total_clv_delta_y9 = 0
if lifetime_loyal > 9:
    total_clv_delta_y10 = sales_clv + (service_clv * 10) - total_clv_churn_y10
else:
    total_clv_delta_y10 = 0





## Customer Equity: Result depending on loyality improvement

if bestand_equity_delta_y10 > 0:
    bestand_equity_delta_dynamic = bestand_equity_delta_y10
else:
    if bestand_equity_delta_y9 > 0:
        bestand_equity_delta_dynamic = bestand_equity_delta_y9
    else:
        if bestand_equity_delta_y8 > 0:
            bestand_equity_delta_dynamic = bestand_equity_delta_y8
        else:
            if bestand_equity_delta_y7 > 0:
                bestand_equity_delta_dynamic = bestand_equity_delta_y7
            else:
                if bestand_equity_delta_y6 > 0:
                    bestand_equity_delta_dynamic = bestand_equity_delta_y6
                else:
                    bestand_equity_delta_dynamic = bestand_equity_delta_y5


st.write(bestand_equity_delta_dynamic)
st.write(total_clv_delta_y7)

## Customer Equity: Result

st.write("")
st.write("")

kundenbestand_wert_col1_icon, kundenbestand_wert_col2_value = st.columns([0.1, 0.9])

with kundenbestand_wert_col1_icon:
    st. image("https://i.postimg.cc/P5rFGy7x/ICON-Kundenwert-4.png", width=50)

with kundenbestand_wert_col2_value:
    st. image("https://i.postimg.cc/mrQsk8bs/image-43.png", width=130)
    equity_upside = str(dealer_jvz) + " Kunden eines Verkaufsjahres länger binden ergibt einen Zusatzertrag von: " + str(bestand_equity_delta_dynamic) + " Euro"
    st.info(equity_upside)
    st.caption("Errechnet auf Basis der o.g. Werten und dem Jahresverkaufsziel (JVZ). Erwirtschaftet bei einer Bindung über 5 zusätzlichen Jahren")






## Creating the data frames for bar chart

data_peryear = {
    ## "Jahr": ["1.Jahr", "2.Jahr", "3.Jahr","4.Jahr", "5.Jahr", "6.Jahr","7.Jahr", "8.Jahr", "9.Jahr","10.Jahr"],
    "Bruttoertrag Vertrieb & Service": [bestand_equity_churn_y1, bestand_equity_churn_y2, bestand_equity_churn_y3, bestand_equity_churn_y4, bestand_equity_churn_y5, bestand_equity_churn_y6, bestand_equity_churn_y7, bestand_equity_churn_y8, bestand_equity_churn_y9, bestand_equity_churn_y10],
    "Zusätzlicher Bruttoertrag": [bestand_equity_delta_y1, bestand_equity_delta_y2, bestand_equity_delta_y3, bestand_equity_delta_y4, bestand_equity_delta_y5, bestand_equity_delta_y6, bestand_equity_delta_y7, bestand_equity_delta_y8, bestand_equity_delta_y9, bestand_equity_delta_y10],
    ## "Bruttoertrag V&S - Gebunden": [bestand_equity_loyal_y1, bestand_equity_loyal_y2, bestand_equity_loyal_y3, bestand_equity_loyal_y4, bestand_equity_loyal_y5, bestand_equity_loyal_y6, bestand_equity_loyal_y7, bestand_equity_loyal_y8, bestand_equity_loyal_y9, bestand_equity_loyal_y10]
}

## data_year = {["1.Jahr", "2.Jahr", "3.Jahr","4.Jahr", "5.Jahr", "6.Jahr","7.Jahr", "8.Jahr", "9.Jahr","10.Jahr"]}


st.write("**Ihr Zusatzertrag nach Jahren**" )



## Creating the bar chart 
st.bar_chart(data=data_peryear, x="data_year" ,  color=["#002B5E", "#00AAD2"])








## Footer


st.write("")
st.write("")

st.image("https://i.postimg.cc/63MYXqSQ/HMD-Impressum.png")