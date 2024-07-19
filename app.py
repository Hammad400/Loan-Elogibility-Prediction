# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'model_Loan_eligibility_predictions.pkl'
classifier = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    Rural=0
    two_dependant=0
    if request.method == 'POST':
        Credit_History=request.form['Credit_History']
        if(Credit_History=='Yes'):
            Credit_History=1
        else:
            Credit_History=0    

        Married=request.form['Married']
        if(Married=='Married'):
            Married =1
        else:
            Married=0

        Education=request.form['Education']
        if(Education=='Graduate'):
            Education =1
        else:
            Education=0

        Gender=request.form['Gender']
        if(Gender=='Male'):
            Gender=1
        else:
            Gender=0

        one_dependant=request.form['one_dependant']
        one_dependant
        if(one_dependant=='Only one dependant'):
            one_dependant=1
            two_dependant=0
        else:
            one_dependant=0
            two_dependant=1

        ApplicantIncome = int(request.form['ApplicantIncome'])

        CoapplicantIncome=float(request.form['CoapplicantIncome'])

        LoanAmount=float(request.form['LoanAmount'])

        Urban=request.form['Urban']
        if(Urban=='Urban Area'):
            Urban=1
            Rural=0
        else:
            Urban=0
            Rural=1
        
        data = np.array([[Credit_History,Married,two_dependant,Education,Gender,one_dependant, ApplicantIncome,CoapplicantIncome,Urban,LoanAmount,Rural]])
        my_prediction = classifier.predict(data)
        
        return render_template('result.html', prediction=my_prediction)

if __name__ == '__main__':
	app.run(debug=True)