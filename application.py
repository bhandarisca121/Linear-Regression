from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Initialize Flask app
application = Flask(__name__)
app=application
# Load the trained model
model = joblib.load(open(r'models\regression_model.joblib', 'rb'))

# Define a route for home page
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            # Get input values from the form
            val1 = float(request.form["val1"])
            val2 = float(request.form["val2"])
            val3 = float(request.form["val3"])
            
            # Make prediction
            input_data = np.array([[val1, val2, val3]])
            prediction = model.predict(input_data)[0]

            return render_template("index.html", prediction=prediction)
        except Exception as e:
            print("Prediction error:", str(e))
            return render_template("index.html", error=str(e))

    return render_template("index.html", prediction=None)


# Run the Flask app
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
