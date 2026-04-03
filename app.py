## frontend









## Bckened













## Database

















##ai intergeration
transport_co2 = distance * factors[transport]
electricity_co2 = electricity * ELECTRICITY_CO2
food_co2 = 2 if food == "Veg" else 5

total = transport_co2 + electricity_co2 + food_co2
#looping
if total > 10:
    st.warning("Reduce emissions! Use public transport & save electricity.")
else:
    st.success("Great job! You're eco-friendly!")

if food == "Non-Veg":
    st.write("Try plant-based meals 2–3 times a week")

if electricity > 5:
    st.write("Turn off unused appliances")
