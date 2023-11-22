import streamlit as st

def get_predict_profit(r_d_expenses, administration_expenses, marketing_expenses, state):
    # Your existing function remains unchanged

def main():
    st.set_page_config(
        page_title="Startup Profit Prediction",
        page_icon=":rocket:",
        layout="centered",
    )

    st.title("Startup Profit Prediction")

    # Streamlit UI components
    st.image("/static/img/Model Deployment-logos_black.png", width=350, caption="MDL LAB FH")

    st.header("Startup Expenses Details")

    r_d_expenses = st.text_input("R&D Expenses")
    administration_expenses = st.text_input("Administration Expenses")
    marketing_expenses = st.text_input("Marketing Expenses")
    state = st.selectbox("State", ["", "New York", "California", "Florida"])

    if st.button("Predict"):
        if r_d_expenses and administration_expenses and marketing_expenses and state:
            output = get_predict_profit(float(r_d_expenses), float(administration_expenses), float(marketing_expenses), state)
            st.success(f"Startup Profit must be $ {output}")
        else:
            st.error("Please provide all input values.")

    # Footer
    st.markdown("---")
    st.text("CSC-4154")
    st.text("MODEL DEPLOYMENT LABORATORY")
    st.text("FAAIZ FAROOK MOHAMED")
    st.text("HABIB MOHAMED")

