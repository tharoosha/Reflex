import streamlit as st
import requests
from datetime import datetime

# Backend API URLs
IOT_API_URL = "http://localhost:8000/api/iot/data"  # Replace with your actual endpoint
USER_API_URL = "http://localhost:8000/api/user/nl-process"  # Replace with your actual endpoint
PREFERENCES_API_URL = "http://localhost:8000/api/user/preferences"  # Replace with your actual endpoint
NEGOTIATION_START_API_URL = "http://localhost:8000/api/negotiation/start"  
NEGOTIATION_CONTINUE_API_URL = "http://localhost:8000/api/negotiation/continue"  

# Initialize session state for storing conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []  # List to store {"user": message, "bot": message} pairs

def add_page_custom_styling():
    st.markdown(
        """
        <style>
            /* Overall page background */
            .stApp {
                background-color: #D3D3D3 !important; /* White background */
                color: #000000 !important; /* Black text for the whole page */
                font-family: 'Arial', sans-serif !important; /* Consistent modern font */
            }

            /* Title and headers */
            h1 {
                color: #000000 !important; /* Black header text */
                font-family: 'Arial', sans-serif !important; /* Consistent font */
            }
            h2, h3 {
                color: #000000 !important; /* Black subheader text */
                font-family: 'Arial', sans-serif !important; /* Consistent font for subheaders */
            }

            /* Labels above input fields */
            label {
                color: #000000 !important; /* Black text for labels */
                font-weight: bold !important; /* Bold for better visibility */
                display: block !important; /* Ensure labels appear above inputs */
                margin-bottom: 5px !important; /* Add spacing below labels */
            }

            /* Form input fields */
            input, textarea, select {
                background-color: #FFFFFF !important; /* White background for inputs */
                color: #000000 !important; /* Black text color */
                border: 1px solid #000000 !important; /* Black border */
                padding: 8px !important;
                border-radius: 5px !important;
                font-family: 'Arial', sans-serif !important; /* Consistent input font */
                box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1) !important; /* Subtle shadow */
            }
            input::placeholder, textarea::placeholder {
                color: #666666 !important; /* Dark gray placeholder text */
                opacity: 0.8 !important; /* Slightly faded for distinction */
            }
            input:focus, textarea:focus, select:focus {
                border: 1px solid #4CAF50 !important; /* Green border on focus */
                box-shadow: 2px 2px 8px rgba(0, 128, 0, 0.2) !important; /* Subtle green shadow */
                outline: none !important; /* Remove default outline */
            }

            /* Dropdown styling */
            select {
                background-color: #FFFFFF !important; /* White dropdown background */
                color: #000000 !important; /* Black text inside dropdown */
                border: 1px solid #000000 !important; /* Black border */
                padding: 8px !important;
                border-radius: 5px !important;
                font-family: 'Arial', sans-serif !important; /* Consistent dropdown font */
                box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1) !important; /* Subtle shadow */
            }
            select option {
                background-color: #FFFFFF !important; /* White option background */
                color: #000000 !important; /* Black text for options */
            }

            /* Buttons */
            button {
                background-color: #FFFFFF !important; /* White button background */
                color: #000000 !important; /* Black text for buttons */
                border: 1px solid #000000 !important; /* Black border for buttons */
                padding: 10px 20px !important;
                border-radius: 5px !important;
                font-size: 16px !important;
                font-family: 'Arial', sans-serif !important; /* Consistent button font */
                cursor: pointer !important; /* Add pointer cursor for buttons */
                box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.1) !important; /* Subtle shadow for buttons */
                transition: all 0.3s ease-in-out !important; /* Smooth transition for hover effect */
            }
            button:hover {
                background-color: #F0F0F0 !important; /* Light gray background on hover */
                box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.2) !important; /* Enhanced shadow on hover */
            }

            /* Form container (IoT form box) */
            .stForm {
                border: 2px solid #000000 !important; /* Black border around the form */
                padding: 20px !important; /* Add padding inside the form container */
                border-radius: 10px !important; /* Rounded corners */
                box-shadow: 4px 4px 10px rgba(0, 0, 0, 0.2) !important; /* Subtle shadow for depth */
                background-color: #F9F9F9 !important; /* Light gray background for form */
            }

            /* Success and error messages */
            .stAlert {
                border-radius: 5px !important; /* Rounded corners for alerts */
                font-family: 'Arial', sans-serif !important; /* Consistent font for alerts */
                padding: 10px !important; /* Add padding for better spacing */
                color: #000000 !important; /* Black text for messages */
            }
            /* Make *everything* inside stAlert black. */
.stAlert,
.stAlert * {
  color: #000000 !important;
}

/* Force the checkbox label text to be black */
.stCheckbox > label div {
    color: #000000 !important;
}

/* Force the label of your selectbox to be black */
.stSelectbox > label {
    color: #000000 !important;
    font-weight: bold !important;
}

/* Ensure the actual dropdown has white background and black text */
.stSelectbox select {
    background-color: #FFFFFF !important;
    color: #000000 !important;
    border: 1px solid #000000 !important; 
}


        </style>
        """,
        unsafe_allow_html=True,
    )




def main():
    # Add custom styling
    add_page_custom_styling()

    st.title("Welcome to REFLEX")

    # Start button to show chat interface
    if "show_chat" not in st.session_state:
        st.session_state.show_chat = False

    # Display User Preferences Form
    st.subheader("Set User Preferences")
    user_preferences_form()

    # Display IoT Form
    st.subheader("IoT Data Submission")
    iot_form()

    # Display NLP Processing Form
    st.subheader("User NLP Processing")
    user_nlp_form()

    

    # Add negotiation section
    st.subheader("Negotiation")
    if st.button("Start Chat"):
        st.session_state.show_chat = True        

    if st.session_state.show_chat:
        start_section()
        negotiation_section()


def iot_form():
    with st.form(key="iot_form"):
        # Input fields for IoT data
        device_id = st.text_input("Device ID", placeholder="Enter Device ID")
        sensor_type = st.text_input("Sensor Type", placeholder="Enter Sensor Type")
        product = st.text_input("Product", placeholder="Enter Product Name")
        remaining = st.number_input("Remaining", min_value=0, step=1)
        unit=st.text_input("Unit", placeholder="Enter Unit, eg='Liters, pods, etc.'")
        timestamp = st.date_input("Timestamp")

        # Submit button
        submit = st.form_submit_button("Submit IoT Data")

        if submit:
            payload = {
                "deviceId": device_id,
                "sensorType": sensor_type,
                "product_type": product,
                "remaining": remaining,
                "unit": unit,
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

def start_section():
    # for message in st.session_state.messages:
    #     print("/////////////////////////////// inside start////////////////", message)
    #     if "user" in message:
    #         st.markdown(f"<div style='text-align: right; color: blue;'><strong>You:</strong> {message['user']}</div>", unsafe_allow_html=True)
    #     if "bot" in message:
    #         st.markdown(f"<div style='text-align: left; color: green;'><strong>Bot:</strong> {message['bot']}</div>", unsafe_allow_html=True)


    # st.session_state.messages.append({"user": "Start"})

    payload = {"message": "Start"}  

    try:
        response = requests.post(NEGOTIATION_START_API_URL, json=payload)
        handle_negotiation_start_response(response)
    except Exception as e:
        st.error(f"Failed to send message: {e}")

def handle_negotiation_start_response(response):
    print("-------------------------------------------------------------")
    if response.status_code == 200:
        response_json = response.json()
        print("-----------------", response_json)
        if "bot_response" in response_json:
            # st.session_state.messages.append({"bot": response_json["bot_response"]})
            st.markdown(f"<div style='text-align: left; color: green;'><strong>Bot:</strong> {response_json["bot_response"]}</div>", unsafe_allow_html=True)

        else:
            st.warning("Unexpected response format!")
    else:
        try:
            response_json = response.json()
            if "error" in response_json:
                st.error(response_json["error"])
        except:
            st.error("Invalid JSON response from the server.")

def negotiation_section():
    for message in st.session_state.messages:
        print("=======================inside negotiation////////////////", message)
        if "user" in message:
            st.markdown(f"<div style='text-align: right; color: blue;'><strong>You:</strong> {message['user']}</div>", unsafe_allow_html=True)
        if "bot" in message:
            st.markdown(f"<div style='text-align: left; color: green;'><strong>Bot:</strong> {message['bot']}</div>", unsafe_allow_html=True)

    with st.form(key="negotiation_form"):
        user_message = st.text_area("Your Message", placeholder="Enter your message to the bot")
        submit = st.form_submit_button("Send Message")
        
        if submit and user_message.strip():
            st.session_state.messages.append({"user": user_message})

            payload = {"message": user_message}

            try:
                response = requests.post(NEGOTIATION_CONTINUE_API_URL, json=payload)
                handle_negotiation_response(response)
            except Exception as e:
                st.error(f"Failed to send message: {e}")

def handle_negotiation_response(response):
    if response.status_code == 200:
        response_json = response.json()
        print("-----------------", response_json)
        if "bot_response" in response_json:
            st.session_state.messages.append({"bot": response_json["bot_response"]})
            st.rerun()
        else:
            st.warning("Unexpected response format!")
    else:
        try:
            response_json = response.json()
            if "error" in response_json:
                st.error(response_json["error"])
        except:
            st.error("Invalid JSON response from the server.")

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
