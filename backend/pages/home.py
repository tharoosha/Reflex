import yaml
import streamlit as st
import datetime
import uuid

# Set white background color
st.markdown(
    """
    <style>
    body {
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Home Page Design
def home_page():
    st.title("Welcome to the Machine Customer Platform!")
    st.write("Easily manage and register your smart devices.")

    # Buttons for device registration
    col1, col2 = st.columns([1, 1], gap="small")

    with col1:
        st.image("assets/devices/coffee_machine.png", use_container_width=True)
        if st.button("Register Coffee Machine"):
            st.session_state["selected_device"] = "coffee_machine"
            st.rerun()

    with col2:
        st.image("assets/devices/smart_fridge.png", use_container_width=True)
        if st.button("Register Smart Fridge"):
            st.session_state["selected_device"] = "smart_fridge"
            st.rerun()

def coffee_machine():
    st.title("Coffee Machine")
    st.write("There are the refill items given by your manufacturer. Do you have any preferences while re-ordering these items?")

    # Buttons for item customization
    col1, col2 = st.columns([1, 1], gap="small")

    with col1:
        st.image("assets/devices/coffee.png", use_container_width=True)
        if st.button("Customize your coffee"):
            st.session_state["selected_device"] = "customize_coffee"
            st.rerun()

    with col2:
        st.image("assets/devices/milk.png", use_container_width=True)
        if st.button("Customize your milk"):
            st.session_state["selected_device"] = "customize_milk"
            st.rerun()

    if st.button("Go Back"):
        st.session_state["selected_device"] = "home"
        st.rerun()

def customize_coffee():
    st.title("Customize Your Coffee Preferences")
    preferences = st.text_area("Enter your coffee preferences:", placeholder="E.g., I like medium roast with low acidity and caramel flavor.")

    if st.button("Submit Coffee Preferences"):
        if preferences.strip():
            st.success(f"Your coffee preferences have been saved: {preferences}")
        else:
            st.error("Please enter your coffee preferences before submitting.")

    if st.button("Go Back"):
        st.session_state["selected_device"] = "coffee_machine"
        st.rerun()

def customize_milk():
    st.title("Customize Your Milk Preferences")
    preferences = st.text_area("Enter your milk preferences:", placeholder="E.g., I prefer oat milk with vanilla flavor.")

    if st.button("Submit Milk Preferences"):
        if preferences.strip():
            st.success(f"Your milk preferences have been saved: {preferences}")
        else:
            st.error("Please enter your milk preferences before submitting.")

    if st.button("Go Back"):
        st.session_state["selected_device"] = "coffee_machine"
        st.rerun()

# Register Device Pages
def register_device_page(device_type):
    st.header(f"Register Your {device_type.replace('_', ' ').title()}")

    # Form for device registration
    device_name = st.text_input("Device Name", placeholder=f"E.g., {device_type.replace('_', ' ').title()}")
    device_model = st.text_input("Model", placeholder="E.g., CM-1234")
    serial_number = st.text_input("Serial Number", placeholder="E.g., SN12345678")
    purchase_date = st.date_input("Purchase Date", value=datetime.datetime.now())

    if st.button("Register Device"):
        st.session_state["selected_device"] = "coffee_registered"
        if device_name and device_model and serial_number:
            # Generate unique device ID
            device_id = str(uuid.uuid4())
            st.success(f"Device Registered Successfully! Your Device ID: {device_id}")
            st.rerun()
        else:
            st.error("All fields are required. Please fill out the form completely.")

    if st.button("Go Back"):
        st.session_state["selected_device"] = "home"
        st.rerun()

# Page Routing
if "selected_device" not in st.session_state:
    home_page()
elif st.session_state['selected_device'] == "home":
    home_page()
elif st.session_state['selected_device'] == 'coffee_machine':
    coffee_machine()
elif st.session_state['selected_device'] == 'customize_coffee':
    customize_coffee()
elif st.session_state['selected_device'] == 'customize_milk':
    customize_milk()
else:
    register_device_page(st.session_state["selected_device"])
