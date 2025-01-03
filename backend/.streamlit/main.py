import streamlit as st
import requests
from datetime import datetime

# Backend API URLs
IOT_API_URL = "http://localhost:8000/api/iot/data"  # Replace with your actual endpoint
USER_API_URL = "http://localhost:8000/api/user/nl-process"  # Replace with your actual endpoint
PREFERENCES_API_URL = "http://localhost:8000/api/user/preferences"  # Replace with your actual endpoint


def add_page_custom_styling():
    """
    Add custom styling to the Streamlit page using CSS for colors and fonts.
    """
    st.markdown(
        """
        <style>
            /* Overall page background */
            .stApp {
                background-color: #A69080; /* Primary background color */
            }

            /* Title and headers */
            h1 {
                color: #3E362E; /* Dark header text color */
            }
            h2, h3 {
                color: #3E362E; /* Subheader text color */
                background-color: #865D36; /* Subheader background color */
                padding: 10px;
                border-radius: 5px;
            }

            /* Form input fields */
            input, textarea, select {
                background-color: #AC8968; /* Input background */
                color: #3E362E; /* Input text color */
                border: 1px solid #3E362E; /* Input border */
                padding: 8px;
                border-radius: 5px;
            }

            /* Buttons */
            button {
                background-color: #93785B; /* Button background */
                color: white; /* Button text */
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 16px;
            }
            button:hover {
                background-color: #865D36; /* Button hover color */
            }

            /* Success and error messages */
            .stAlert {
                border-radius: 5px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def main():
    # Add custom styling
    add_page_custom_styling()

    st.title("API Input Application")

    # Display IoT Form
    st.subheader("IoT Data Submission")
    iot_form()

    # Display NLP Processing Form
    st.subheader("User NLP Processing")
    user_nlp_form()

    # Display User Preferences Form
    st.subheader("Set User Preferences")
    user_preferences_form()


def iot_form():
    with st.form(key="iot_form"):
        # Input fields for IoT data
        device_id = st.text_input("Device ID", placeholder="Enter Device ID")
        sensor_type = st.text_input("Sensor Type", placeholder="Enter Sensor Type")
        product = st.text_input("Product", placeholder="Enter Product Name")
        remaining = st.number_input("Remaining", min_value=0, step=1)
        timestamp = st.date_input("Timestamp")

        # Submit button
        submit = st.form_submit_button("Submit IoT Data")

        if submit:
            payload = {
                "deviceId": device_id,
                "sensorType": sensor_type,
                "product": product,
                "remaining": remaining,
                "timestamp": timestamp.isoformat(),
            }

            try:
                response = requests.post(IOT_API_URL, json=payload)
                handle_response(response)
            except Exception as e:
                st.error(f"Failed to submit IoT data: {e}")


def user_nlp_form():
    with st.form(key="user_nlp_form"):
        text_input = st.text_area("Text Input", placeholder="Enter text for NLP processing")
        submit = st.form_submit_button("Submit NLP Data")

        if submit:
            payload = {"query": text_input}

            try:
                response = requests.post(USER_API_URL, json=payload)
                handle_response(response)
            except Exception as e:
                st.error(f"Failed to process NLP data: {e}")


def user_preferences_form():
    with st.form(key="preferences_form"):
        # Input fields for User Preferences
        user_id = st.text_input("User ID", placeholder="Enter User ID")
        preferred_brands = st.text_area("Preferred Brands", placeholder="Enter brands, separated by commas")
        dietary_restrictions = st.text_area(
            "Dietary Restrictions", placeholder="Enter restrictions, separated by commas"
        )
        max_budget = st.number_input("Max Budget", min_value=0.0, step=1.0)
        delivery_priority = st.selectbox("Delivery Priority", ["Low", "Medium", "High"])
        autonomy = st.checkbox("Autonomy", value=False)

        # Submit button
        submit = st.form_submit_button("Submit Preferences")

        if submit:
            payload = {
                "preferred_brands": [brand.strip() for brand in preferred_brands.split(",") if brand.strip()],
                "dietary_restrictions": [
                    restriction.strip() for restriction in dietary_restrictions.split(",") if restriction.strip()
                ],
                "max_budget": max_budget,
                "delivery_priority": delivery_priority,
                "autonomy": autonomy,
            }

            try:
                response = requests.post(PREFERENCES_API_URL, params={"user_id": user_id}, json=payload)
                handle_response(response)
            except Exception as e:
                st.error(f"Failed to set user preferences: {e}")


def handle_response(response):
    if response.status_code == 200:
        response_json = response.json()
        if "message" in response_json:
            st.success(response_json["message"])
        elif "error" in response_json:
            st.error(response_json["error"])
        else:
            st.warning("Unexpected response format!")
    else:
        try:
            response_json = response.json()
            if "error" in response_json:
                st.error(response_json["error"])
        except:
            st.error("Invalid JSON response from the server.")


if __name__ == "__main__":
    main()
