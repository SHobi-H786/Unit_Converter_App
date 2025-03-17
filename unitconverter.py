import streamlit as st 

st.title("🌍Unit Converter App")
st.write("👩‍💻 **Developed by M.Shoaib Panwar**")
st.markdown("### Converts Length, Weigth and Time Instantly")
st.write("👋Welcome! select a category, enter a value and get the converted result in real-time")
category = st.selectbox("choose a category", ["Length", "Weigth", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
    elif category == "weigth":
        if unit == "kilogram to pounds":
            return value /2.20462
    elif category == "Time":
        if unit == "Seconds to minutes":
            return value /60
        elif unit == "Minutes to seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to minutes":
            return value * 60
        elif unit == " Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
    return 0
if category == "Length":
    unit = st.selectbox("📏Select conversation", ["Kilometers to Miles","Miles to Kilometers"]) 
elif category == "Weigth":
    unit = st.selectbox("⚖ Select Conversation", ["Kilograms to pounds", "Pound to Kilograms"])
    
elif category == "Time":
    unit = st.selectbox("⌚ Select conversation", ["Seconds to minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])
    
value = st.number_input("Enter the Value to convert")

if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The Result is {result:.2f}")
    
