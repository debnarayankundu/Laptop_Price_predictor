# Laptop_Price_predictor
Welcome to the Laptop Price Predictor! This Streamlit application allows users to input various specifications of a laptop and get a predicted price based on a pre-trained machine learning model.

## Features
Interactive UI: User-friendly interface with select boxes for various laptop specifications.
Real-time Predictions: Get instant price predictions based on your input.
Responsive Design: Layout adapts to different screen sizes for a smooth user experience.
Animations: Enhanced visual appeal with animated headers and buttons.
## Specifications
The app accepts the following input parameters to predict the laptop price:

Brand: HP, DELL, APPLE, ASUS, Lenovo, acer, Avita, MSI
Processor Brand: Intel, AMD, M1
Processor Name: Core i3, Core i5, Core i7, Core i9, Ryzen 3, Ryzen 5, Ryzen 7, Ryzen 9, Celeron Dual, M1, Pentium Quad
Processor Generation: Not Available, 7th, 8th, 9th, 10th, 11th, 12th, 4th
RAM (GB): 4 GB, 8 GB, 32 GB, 16 GB
RAM Type: DDR3, DDR4, DDR5, LPDDR4X, LPDDR4, LPDDR3
SSD (GB): 0 GB, 1024 GB, 512 GB, 256 GB, 128 GB, 2048 GB
HDD (GB): 0 GB, 1024 GB, 512 GB, 2048 GB
Operating System: Windows, Mac, DOS
OS Bit: 32-bit, 64-bit
Graphic Card (GB): 0 GB, 4 GB, 2 GB, 6 GB, 8 GB
Weight: Casual, ThinNlight, Gaming
Warranty: No warranty, 1 year, 2 years, 3 years
Touchscreen: Yes, No
MS Office Included: Yes, No
Rating: 5 stars, 4 stars, 3 stars, 2 stars, 1 star

## Installation
Clone the repository:
git clone https://github.com/yourusername/laptop-price-predictor.git
cd laptop-price-predictor


Install the required dependencies:


pip install -r requirements.txt
Run the application:

sh
Copy code
streamlit run app.py
## Usage
Open your browser and go to http://localhost:8501 to interact with the application.
Fill in the specifications of the laptop you want to price.
Click on the Predict Price button to get the estimated price.
