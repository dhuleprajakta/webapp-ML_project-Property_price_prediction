
from flask import Flask, request, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("property_price_model.joblib")

# List of suburbs to match your one-hot encoding
suburbs = [
    "Delhi Central", "Delhi East", "Delhi North", "Delhi South", "Delhi West",
    "Dwarka", "North Delhi", "North West Delhi", "Other", "Rohini",
    "South West Delhi", "West Delhi"
]

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        try:
            size = float(request.form["size_sq_ft"])
            property_type = int(request.form["propertyType"])
            bedrooms = int(request.form["bedrooms"])
            ap_dist = float(request.form["AP_dist_km"])
            aiims_dist = float(request.form["Aiims_dist_km"])
            ndrlw_dist = float(request.form["NDRLW_dist_km"])
            suburb_selected = request.form["suburb"]

            # One-hot encode suburbs
            suburb_encoded = [1 if suburb == suburb_selected else 0 for suburb in suburbs]

            # Combine all features
            input_data = np.array([[size, property_type, bedrooms, ap_dist, aiims_dist, ndrlw_dist] + suburb_encoded])
            prediction = model.predict(input_data)[0]
            return render_template("index.html", prediction=round(prediction, 2))
        except Exception as e:
            return render_template("index.html", prediction=f"Error: {e}")

    return render_template("index.html", prediction=None)
if __name__ == "__main__":
    app.run(debug=True)
