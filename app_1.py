from flask import Flask, render_template, request
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('model_Loan_eligibility_predictions.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index2.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
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

        prediction=model.predict([[Credit_History,Married,two_dependant,Education,Gender,one_dependant, ApplicantIncome,CoapplicantIncome,Urban,LoanAmount,Rural]])

        if prediction==0:
            return render_template('index2.html',prediction_text="Sorry you are not eligibile for loan")
        else:
            return render_template('index2.html',prediction_text="you are eligibile for loan")
    else:
        return render_template('index2.html')

if __name__=="__main__":
    app.run(debug=True)

