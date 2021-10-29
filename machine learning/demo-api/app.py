#Importing the libraries
import pickle
from flask import Flask, render_template, request

#Global Variables
loadedModel = pickle.load(open('diabetes.sav', 'rb'))
app = Flask(__name__)

#User-defined routes
@app.route("/")
def home():
    return render_template('diabetes.html')


@app.route("/prediction", methods=['POST'])
def prediction():
    bmi = request.form['bmi']
    age = request.form['age']
    glucose = request.form['glucose']

    prediction = loadedModel.predict([[glucose, bmi, age]])

    if prediction[0] == 0:
        prediction = "Not Diabetic"
    else:
        prediction = "Diabetic"

    return render_template('diabetes.html', output=prediction)


#Main function
if __name__ == '__main__':
    app.run(debug=True)