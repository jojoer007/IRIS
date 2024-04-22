from flask import Flask, render_template, request
from iris import predict_iris
from irisDB import iris_db

app = Flask(__name__)


@app.route('/')

def index():
    return render_template('index.html', prediction=None)


@app.route('/predict', methods=['POST'])

def predict():
    sepal_length = float(request.form['sepal_length'])
    sepal_width = float(request.form['sepal_width'])
    petal_length = float(request.form['petal_length'])
    petal_width = float(request.form['petal_width'])

    features = [sepal_length, sepal_width, petal_length, petal_width]
    prediction = predict_iris(features)
    features.append(prediction)

    iris_db(features)   # เขียนข้อมูลลง database

    return render_template('index.html', prediction=prediction)

@app.route('/All_result')

def all_result():

    results = iris_db()    # อ่านข้อมูลจาก database

    return render_template ('result.html', results=results);

if __name__ == '__main__':
    app.run(debug=True)