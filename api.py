import pandas as pd
from flask import Flask, request
import joblib

with open('model.pkl', 'rb') as model_file:
    model = joblib.load(model_file)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    application_year = request.form['application_year']
    showup = request.form['showup']
    finished = request.form['finished']
    venture_region = request.form['venture_region']
    website = request.form['website']
    founding_year = request.form['founding_year']
    age = request.form['age']

    prediction = model.predict(pd.DataFrame([[application_year, showup, finished, venture_region, website, founding_year, age]]))
    return str(prediction)

if __name__=='__main__':
    app.run(port=3000, debug=True)