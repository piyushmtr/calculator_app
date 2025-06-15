import streamlit as st

# App Title
st.title("🧮 Simple Calculator App")

# Input numbers
num1 = st.number_input("Enter first number", step=1.0, format="%.2f")
num2 = st.number_input("Enter second number", step=1.0, format="%.2f")

# Operation Selection
operation = st.selectbox("Select Operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Calculate result
result = None
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("❌ Cannot divide by zero!")

# Display result
if result is not None:
    st.success(f"Result: {result:.2f}")

