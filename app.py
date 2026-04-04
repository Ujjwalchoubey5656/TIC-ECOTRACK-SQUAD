








































































































# ---------- HOME AFTER LOGIN ----------
if "user" in st.session_state and menu == "Login":
    st.write(f"👤 Logged in as: {st.session_state['user']}")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://cdn-icons-png.flaticon.com/512/4140/4140048.png", width=200)
    with col2:
        st_lottie(lottie_hand, height=150)
        distance = st.number_input("Distance (km)", min_value=0.0)
        transport = st.selectbox("Transport", ["Car", "Bus", "Bike"])
        electricity = st.number_input("Electricity units", min_value=0.0)
        food = st.selectbox("Food", ["Veg", "Non-Veg"])

co2 = 0
    if transport == "Car":
        co2 += distance * 0.21
    elif transport == "Bus":
        co2 += distance * 0.1
    else:
        co2 += distance * 0.05
    co2 += electricity * 0.5
    co2 += 2 if food == "Non-Veg" else 1
    st.subheader(f"🌍 CO₂ Emission: {co2:.2f} kg/day")

if st.button("Save Data"):
        user = st.session_state["user"]
        new_data = pd.DataFrame([{"user": user, "co2": co2}])
        if os.path.exists("data.csv"):
            old = pd.read_csv("data.csv")
            df = pd.concat([old, new_data])
        else:
            df = new_data
        df.to_csv("data.csv", index=False)
        st.success("Saved!")

    st.subheader("📊 Dashboard")
    if os.path.exists("data.csv"):
        df = pd.read_csv("data.csv")
        user_data = df[df["user"] == st.session_state["user"]]
        st.line_chart(user_data["co2"]) 
    
