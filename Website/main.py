from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn import preprocessing

import pickle
app = Flask(__name__)

pipe = pickle.load(open("finalized_model.sav",'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    district = request.form.get('district')
    housing = request.form.get('housing')
    paper = request.form.get('paper')
    size = float(request.form.get('size'))
    floor = float(request.form.get('floor'))
    room = float(request.form.get('room'))
    if request.form.get('width')!='':
        width = float(request.form.get('width'))
    else:
        width = float(0)
    if request.form.get('length')!='':
        length = float(request.form.get('length'))
    else:
         length = float(0)
    input = pd.DataFrame([[district,housing,paper,floor,room,size,length,width]],columns=['district','type_of_housing','legal_paper','num_floors','num_bed_rooms','squared_meter_area','length_meter','width_meter'])
    RF_prediction = pipe.predict(input)[0]
    print(RF_prediction)

    return str(RF_prediction)+' triệu đồng '
if __name__ == "__main__":
    app.run(debug=True,port=5001)