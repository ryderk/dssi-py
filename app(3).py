import streamlit as st
from src.inference2 import get_prediction

#Initialise session state variable
if 'input_features' not in st.session_state:
    st.session_state['input_features'] = {}
def app_sidebar():
    st.sidebar.header('Car Details')
    age_in = st.sidebar.text_input('Age of Car')
    mileage_in = st.sidebar.text_input("Mileage of Car", placeholder="in Kilometers")
    fueltype_in = st.sidebar.text_input('FuelType of Car', placeholder="Diesel,Petrol,CNG")
    hp_in = st.sidebar.text_input('HorsePower')
    transmission_in = st.sidebar.text_input('Automatic?',placeholder="put 1 if Automatic, 0 if Manual")
    cc_in = st.sidebar.text_input('Tank CC')
    doors_in = st.sidebar.text_input('No. of Doors')
    weight_in = st.sidebar.text_input("Weight of Car")
    def get_input_features():
        input_features = {'Age': age_in,
                          'KM': mileage_in,
                          'FuelType': fueltype_in,
                          'HP': hp_in,
                          'Automatic': transmission_in,
                          'CC':cc_in,
                          'Doors':doors_in,
                          'Weight':weight_in
                         }
        return input_features
    sdb_col1, sdb_col2 = st.sidebar.columns(2)
    with sdb_col1:
        predict_button = st.sidebar.button("Assess", key="predict")
    with sdb_col2:
        reset_button = st.sidebar.button("Reset", key="clear")
    if predict_button:
        st.session_state['input_features'] = get_input_features()
    if reset_button:
        st.session_state['input_features'] = {}
    return None

def app_body():
    title = '<p style="font-family:arial, sans-serif; color:Black; font-size: 40px;"><b> Welcome to Second Hand Car Evaluator</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    default_msg = '**The estimated price of your car is: SGD$ ** {}'
    if st.session_state['input_features']:
        assessment = get_prediction({'Age': st.session_state['input_features']['Age'],
                          'KM': st.session_state['input_features']['KM'],
                          'FuelType': st.session_state['input_features']['FuelType'],
                          'HP': st.session_state['input_features']['HP'],
                          'Automatic': st.session_state['input_features']['Automatic'],
                          'CC':st.session_state['input_features']['CC'],
                          'Doors':st.session_state['input_features']['Doors'],
                          'Weight':st.session_state['input_features']['Weight'],
                         })
        st.success(default_msg.format(assessment))
    return None

def main():
    app_sidebar()
    app_body()
    return None

if __name__ == "__main__":
    main()