from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('churn_rf.pkl', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        
        Tenure = float(request.form['Tenure'])
        
        Balance = float(request.form['Balance'])
               
        EstimatedSalary = float(request.form['EstimatedSalary'])
        
        CreditScore = float(request.form['CreditScore'])
        
        Age = float(request.form['Age'])
        
        NumOfProducts = float(request.form['NumOfProducts'])


        HasCrCard = request.form['HasCrCard']
        if (HasCrCard == 'Yes'):
            HasCrCard = 1
            
        else :
            HasCrCard = 0


        IsActiveMember = request.form['IsActiveMember']
        if (IsActiveMember == 'Yes'):
            IsActiveMember = 1
            
        else :
            IsActiveMember = 0
        
        
        Gender = request.form['Gender']
        if (Gender == 'Male'):
            Male = 1
            
        else :
            Male = 0
            
            
        Geography = request.form['Geography']
        if (Geography == 'Germany'):
            Germany = 1
            Spain = 0
            
        elif (Geography == 'Spain'):
            Germany = 0
            Spain = 1
            
        else:
            Germany = 0
            Spain = 0
                    

        prediction=model.predict([[Tenure, Balance, EstimatedSalary, CreditScore, Age, NumOfProducts, HasCrCard, IsActiveMember,Germany, Spain, Male]])
        
        output = prediction

        if output == 0:
            return render_template('index.html',prediction_text="The customer Won't leave the Bank")
        elif output == 1:
            return render_template('index.html',prediction_text="The customer Will probably leave the Bank")
    else:
        return render_template('index.html')
            
        

if __name__=="__main__":
    app.run(debug=True)
