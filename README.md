<h1 align="center">⚡Income Predictor⚡</h1>

---

<h2 align="left">➡️ Visit the Application</h2>

[![Click Me](https://img.shields.io/badge/Click-Me-blue?style=for-the-badge)](https://income-predictor-w52t.onrender.com)

---

<h2 align="left">➡️ Description</h2>

This project uses a **`Random Forest ML Model`** to predict an individual's income based on various features such as age, education, occupation, and work experience. The Random Forest model combines the outputs of multiple decision trees to improve prediction accuracy and reduce overfitting. The trained model is deployed using a web application built with Flask.

---

<h2 align="left">➡️ Features</h2>

- **`Input Data`**: Age, education, occupation, experience, hours worked per week, and more.
- **`Output`**: Predicted income (`<=50K` or `>50K`).
- **`Model`**: Random Forest, an ensemble machine learning algorithm.
- **`Web Application`**: A user-friendly interface to input data and view predictions.
- **`Technologies Used`**: Python, Scikit-learn, Pandas, Matplotlib/Seaborn for visualization

---

<h2 align="left">➡️ Installation</h2>

### Prerequisites

- **`Python 3.8+`** (Ensure you have Python installed. You can download it from [python.org](python.org).)
- **`pip`** (Python package manager)

### Required Libraries

- Install the required Python libraries using:
  ```bash
  pip install -r requirements.txt
  ```
  - `numpy 1.26.4`, `pandas 2.2.2`, `matplotlib 3.9.2`, `seaborn 0.13.2`, `scikit-learn 1.5.2`, `Flask`

---

<h2 align="left">➡️ File Structure</h2>

![income_predictor_file_structure.png](https://github.com/MrGenius18/Income_Predictor/blob/e79ace96a21f215c0c83f1b3c788e68d3b53b724/income_predictor_file_structure.png)

### Key Files

1. **`app.py`**:
   - Contains the Flask application code.
   - Loads the trained model (`Income_Predictor.pkl`), scaler (`scaler.pkl`), and label encoder (`label_encoder.pkl`).
   - Handles form inputs and makes predictions.

2. **`Income_Predictor.pkl`**:
   - The trained Random Forest model saved using `joblib`.

3. **`label_encoder.pkl`**:
   - Encodes categorical variables for consistent input formatting.

4. **`scaler.pkl`**:
   - Scales numerical inputs to the range expected by the model.

5. **`templates/index.html`**:
   - The HTML file for the web interface.
     
---

<h2 align="left">➡️ Dataset</h2>

The model expects a dataset with the following features:

  - **`Numerical Variables`**:- Age, Hours Worked Per Week
  - **`Categorical Variables`**:- Education Level, Occupation,
    
- For more details about this dataset, you can refer to the following link: [dataset](https://archive.ics.uci.edu/ml/datasets/census+income)
  
---

<h2 align="left">➡️ Usage</h2>

- **`Step 1`:** Clone the Repository to your local machine:
  ```bash
  git clone https://github.com/yourusername/income-predictor.git
  cd income-predictor
  ```

- **`Step 2`:** Run the Flask application using the following command:
  ```bash
  python app.py
  ```
  - The application will start, and you can access it in your browser at `http://127.0.0.1:5000`.

- **`Step 3`:** Use the Web Application:
  - Open the web app in your browser.
  - Enter the required details (age, education, occupation, etc.).
  - Click the **Predict** button to get the income prediction.

---

<h2 align="left">➡️ Model Performance</h2>

- **`Best Parameters for Random Forest`**: {'max_depth': None, 'min_samples_leaf': 4, 'min_samples_split': 10, 'n_estimators': 100}
- **`Best Score for Random Forest`**: 0.8433494610067394

### Model Wise Metrics:

![income_predictor_metrics_df.png](https://github.com/MrGenius18/Income_Predictor/blob/e79ace96a21f215c0c83f1b3c788e68d3b53b724/income_predictor_metrics_df.png)

---

## Contribution

Contributions are welcome! If you have suggestions for improvements, submit an issue or a pull request.

---

## Acknowledgments

- Thanks to **`Intellipaat`** for the inspiration and datasets used in this project.
- Scikit-learn for providing the machine learning libraries.
- Flask for the web framework.

---
