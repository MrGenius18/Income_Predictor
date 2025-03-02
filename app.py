from flask import Flask, render_template, request
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model, scaler, and label encoder from pickle files
with open('pkl files/Income_Predictor.pkl', 'rb') as file:
    rf_grid_search = pickle.load(file)

with open('pkl files/scaler.pkl', 'rb') as file:
    SC = pickle.load(file)

with open('pkl files/label_encoder.pkl', 'rb') as file:
    LE = pickle.load(file)

# Route for displaying the form
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling the form submission and prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        input_data = {
            "age": int(request.form['age']),
            "workclass": request.form['workclass'],
            "education": request.form['education'],
            "education-num": int(request.form['education-num']),
            "occupation": request.form['occupation'],
            "race": request.form['race'],
            "sex": request.form['sex'],
            "capital-gain": int(request.form['capital-gain']),
            "capital-loss": int(request.form['capital-loss']),
            "hours-per-week": int(request.form['hours-per-week']),
            "native-country": request.form['native-country']
        }

        input_df = pd.DataFrame([input_data])

        for col in input_df.columns:
            if input_df[col].dtype == 'object':
                LE.fit(input_df[col].astype(str))
                input_df[col] = LE.transform(input_df[col].astype(str))

        fitted_columns = SC.feature_names_in_
        input_df_aligned = input_df.reindex(columns=fitted_columns, fill_value=0)
        input_df_aligned = SC.transform(input_df_aligned)
        input_df[fitted_columns] = input_df_aligned

        try:
            predicted_income = rf_grid_search.predict(input_df)
            result = ">50K" if predicted_income[0] == 1 else "<=50K"
        except Exception as e:
            result = f"Prediction failed: {e}"

        return render_template('index.html', prediction=result)

    except Exception as e:
        return f"Error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
