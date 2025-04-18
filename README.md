# webapp-ML_project-Property_price_prediction
Developed a Property Price Prediction model using regression techniques to estimate rental prices based on features like size, location, and amenities. Integrated the model into a user-friendly web application for real-time predictions and easy user interaction

🏡 Property Price Prediction Web App
This project is a Property Price Prediction Web App that estimates rental property prices based on various input features. The app is built using machine learning for the predictive model and Flask for the web application interface.

🚀 Features
Predicts property rental prices based on:

Size (sq. ft)

Property Type (Flat/House)

Number of Bedrooms

Distance to key landmarks (AP, AIIMS, NDRLW)

Suburb

Interactive and user-friendly web interface

Real-time predictions

🧠 Machine Learning Model
Regression-based model trained on a dataset containing historical rental data.

Data preprocessing and feature engineering performed to improve prediction accuracy.

🛠️ Tech Stack
Frontend: HTML, CSS, Bootstrap (via Flask templates)

Backend: Python, Flask

ML: Scikit-learn, Pandas, NumPy

📦 How to Run the Project
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/property-price-prediction.git
cd property-price-prediction
Create a virtual environment and activate it

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install the dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask app

bash
Copy
Edit
python app.py
Open your browser and go to http://127.0.0.1:5000

📷 UI Preview

📌 Project Structure
csharp
Copy
Edit
property-price-prediction/
│
├── app.py                 # Flask app
├── model.pkl              # Trained ML model
├── templates/
│   └── index.html         # Frontend HTML form
├── static/
│   └── style.css          # CSS (if any)
├── requirements.txt       # Python dependencies
└── README.md              # Project README
✅ Future Enhancements
Add login/signup functionality

Connect to a live database for storage












