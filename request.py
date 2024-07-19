import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'':10, 
	'Gender':1,
	'Married':1,
	'Education':1,
	'Self_Employed	':1,
	'ApplicantIncome':3273,
	'CoapplicantIncome':1820.0,
	'LoanAmount':81.0,
	'Loan_Amount_Term':360,
	'Credit_History':1.0,
	'Property_Area':1})

print(r.json())