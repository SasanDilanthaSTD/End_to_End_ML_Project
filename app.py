import os
from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from RedWineQualityPrediction.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

# define the train endpoint
@app.route("/train", methods=['GET'])
def training():
    os.system('python main.py')
    return "<h1>Training Sucessfull!</h1>"


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])
            
            data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]
            data = np.array(data).reshape(1, 11)
            
            predict_obj = PredictionPipeline()
            predict_quality = predict_obj.predict(data)
            
            return render_template('results.html', prediction=str(predict_quality))
        except Exception as error:
            print("The exeption message is : ", error)
            return "Something went wrong. Please try again."
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))