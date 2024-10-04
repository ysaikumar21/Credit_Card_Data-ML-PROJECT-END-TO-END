import numpy as np 
import pandas as pd 
import sklearn 
import pickle
import warnings
warnings.filterwarnings('ignore')
from sklearn.ensemble import RandomForestClassifier
reg = RandomForestClassifier()
g = pickle.load(open('C:\\Users\\Saiku\\Downloads\\Credit_Project\\Credit_card_project.pkl','rb'))
from flask import Flask , render_template , request

app = Flask(__name__)


@app.route("/")
def fun():
    return render_template("index.html")

@app.route("/sk", methods = ['POST'])
def predict():
    if request.method == 'POST':
        NCL = request.form['NumberOfOpenCreditLinesAndLoans_log_trimming']
        NRL = request.form['NumberRealEstateLoansOrLines_log_trimming']
        MI = request.form['MonthlyIncome_replaced_log_trimming']
        ND = request.form['NumberOfDependents_replaced_log_trimming']
        RC = request.form['Region_Central']
        RE = request.form['Region_East']
        RN = request.form['Region_North']
        RW = request.form['Region_West']
        Edu = request.form['Education']
        data = [[float(NCL) , float(NRL) , float(MI) , float(ND),float(RC) , float(RE) , float(RN) , float(RW),float(Edu)]]
        outcome = g.predict(data)[0]
        if outcome == 0:
          return render_template("index.html" , prediction='Bad Customer')
        else:
            return render_template("index.html" , prediction='Good Customer')


if __name__ == "__main__":
    app.run(debug=True)
