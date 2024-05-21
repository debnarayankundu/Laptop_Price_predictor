import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the model
model = pickle.load(open('C:/Users/Debnarayan Kundu/projects/laptop_price/laptop_price2.sav', 'rb'))

def main():
    # Set page title and background color
    st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻", layout="wide")

    # Decorative header with custom font and animation
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">
        <style>
            @keyframes fadeIn {
                0% { opacity: 0; }
                100% { opacity: 1; }
            }
            .header-text {
                font-family: 'Pacifico', cursive;
                font-size: 36px;
                color: #ffffff;
                text-align: center;
                animation: fadeIn 3s;
            }
            .form-container {
                animation: fadeIn 2s;
            }
            .stButton button {
                background-color: white;
                color: red;
                padding: 5px 8px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                transition-duration: 0.4s;
                cursor: pointer;
            }
            .stButton button:hover {
                background-color: white;
                color: green;
                border: 4px solid #4CAF50;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('<p class="header-text">Laptop Price Predictor</p>', unsafe_allow_html=True)

    # User inputs for each independent variable
    with st.form(key='input_form'):  
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            brand = st.selectbox('Brand', ['HP', 'DELL', 'APPLE', 'ASUS', 'Lenovo', 'acer', 'Avita', 'MSI'], key='brand')
            processor_brand = st.selectbox('Processor Brand', ['Intel', 'AMD', 'M1'], key='processor_brand')
            processor_name = st.selectbox('Processor Name', ['Core i3', 'Core i5', 'Core i7', 'Core i9', 'Ryzen 3', 'Ryzen 5', 'Ryzen 7', 'Ryzen 9', 'Celeron Dual', 'M1', 'Pentium Quad'], key='processor_name')
            processor_gnrtn = st.selectbox('Processor Generation', ['Not Available', '7th', '8th', '9th', '10th', '11th', '12th', '4th'], key='processor_gnrtn')

        with col2:
            ram_gb = st.selectbox('RAM (GB)', ['4 GB', '8 GB', '32 GB', '16 GB'], key='ram_gb')
            ram_type = st.selectbox('RAM Type', ['DDR3', 'DDR4', 'DDR5', 'LPDDR4X', 'LPDDR4', 'LPDDR3'], key='ram_type')
            ssd = st.selectbox('SSD (GB)', ['0 GB', '1024 GB', '512 GB', '256 GB', '128 GB', '2048 GB'], key='ssd')
            hdd = st.selectbox('HDD (GB)', ['0 GB', '1024 GB', '512 GB', '2048 GB'], key='hdd')

        with col3:
            os = st.selectbox('Operating System', ['Windows', 'Mac', 'DOS'], key='os')
            os_bit = st.selectbox('OS Bit', ['32-bit', '64-bit'], key='os_bit')
            graphic_card_gb = st.selectbox('Graphic Card (GB)', ['0 GB', '4 GB', '2 GB', '6 GB', '8 GB'], key='graphic_card_gb')
            weight = st.selectbox('Weight', ['Casual', 'ThinNlight', 'Gaming'], key='weight')

        with col4:
            warranty = st.selectbox('Warranty', ['No warranty', '1 year', '2 years', '3 years'], key='warranty')
            touchscreen = st.selectbox('Touchscreen', ['Yes', 'No'], key='touchscreen')
            msoffice = st.selectbox('MS Office Included', ['Yes', 'No'], key='msoffice')
            rating = st.selectbox('Rating', ['5 stars', '4 stars', '3 stars', '2 stars', '1 star'], key='rating')

        submit_button = st.form_submit_button(label='Predict Price')

    # When the "Predict Price" button is clicked
    if submit_button:
        # Preprocess inputs
        features = {
            'brand': brand,
            'processor_brand': processor_brand,
            'processor_name': processor_name,
            'processor_gnrtn': processor_gnrtn,
            'ram_gb': ram_gb,
            'ram_type': ram_type,
            'ssd': ssd,
            'hdd': hdd,
            'os': os,
            'os_bit': os_bit,
            'graphic_card_gb': graphic_card_gb,
            'weight': weight,
            'warranty': warranty,
            'Touchscreen': touchscreen,
            'msoffice': msoffice,
            'rating': rating
        }

        # Convert categorical features to numerical (example code, adjust as necessary)
        feature_df = pd.DataFrame([features])

        prediction = model.predict(feature_df)[0]

        # Display the prediction
        st.success(f'The predicted price of the laptop is: ₹{prediction:.2f}')

if __name__ == '__main__':
    main()
