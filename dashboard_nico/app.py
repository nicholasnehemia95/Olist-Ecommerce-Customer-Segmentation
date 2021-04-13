from flask import Flask, render_template, request
import pickle
import pandas as pd
import csv
import os 
import json
import chart_studio
import chart_studio.plotly as py
import chart_studio.tools as tls

def rfm_price(x):
    lower_quartil=42.90
    median=79.99
    upper_quartil=149.81
    if x<=lower_quartil:
        val=1
    elif lower_quartil<x<=median:
        val=2
    elif median<x<=upper_quartil:
        val=3
    else:
        val=4
    return val

def rfm_freq(x):
    lower_quartil=2
    median=3
    upper_quartil=4
    if x<=lower_quartil:
        val=1
    elif lower_quartil<x<=median:
        val=2
    elif median<x<=upper_quartil:
        val=3
    else:
        val=4
    return val
def rfm_recency(x):
    lower_quartil=-336.0
    median=-209.0
    upper_quartil=-112.0
    if x<=lower_quartil:
        val=1
    elif lower_quartil<x<=median:
        val=2
    elif median<x<=upper_quartil:
        val=3
    else:
        val=4
    return val

user = "nicholasnehemia95"
api= "NDL6mOh1t12ZjGfnj5ZZ"
chart_studio.tools.set_credentials_file(username=user, api_key=api)

import chart_studio.plotly as py
import chart_studio.tools as tls

app = Flask(__name__)
olist_data=pd.read_csv('./csv/big_df_clean.csv')

@app.route("/",methods=['POST','GET'])
def home():
    return render_template('index.html')

@app.route("/dataset",methods=['POST','GET'])
def dataset():
    ## Our combined data, only first 1000
    table=olist_data.head(1000)

    return render_template('dataset.html',data=table)

@app.route("/EDA",methods=['GET','POST'])
def eda():    
    return render_template('EDA.html')


@app.route("/cluster_results",methods=['GET','POST'])
def show_clusters():    
    return render_template('show_clusters.html')

@app.route("/predict",methods=['POST','GET'])
def predict():
    return render_template('predict.html')

        

@app.route("/result",methods=['POST','GET'])
def result():
    user = request.form
    if request.method=='POST':
        df_to_predict = pd.DataFrame({
            'Recency': pd.Series([user['Recency']]).apply(lambda x : rfm_recency(float(x)))[0],
            'Frequency': pd.Series([user['Frequency']]).apply(lambda x : rfm_freq(float(x)))[0],
            'Monetary': pd.Series([user['Monetary']]).apply(lambda x : rfm_price(float(x)))[0],
        },
        index=[0])

        prediction=model.predict(df_to_predict)
        
        if prediction==0:
            category="Low Value, Churned"
            description="Memiliki nilai monetery rendah , Frequency yang rendah , dan Recency yang rendah"
            item_recc='top_10_clust_0.png'
        elif prediction==1:
            category="High Value, Churned"
            description='Memiliki nilai montary tinggi , nilai frequensi yang relatif tinggi, dan recency yang sudah lama'
            item_recc='top_10_clust_1.png'
        elif prediction==2:
            category="High Value Active"
            description='Memiliki nilai monetary ,frequensi yang paling tinggi, dan Recency yang kedua tertinggi'
            item_recc='top_10_clust_2.png'
        else:
            category="Potential Customer"
            description='Memiliki nilai monetary dan frequensi yang rendah, tetapi memiliki recency yang tertinggi'
            item_recc='top_10_clust_3.png'

        return render_template('predict_result.html',data=user,pred=category,clusterdesc=description,show_reccom_item=item_recc)



if __name__ =="__main__":
    filename = 'KMeans_K4_final.sav'
    model = pickle.load(open(filename, 'rb'))
    app.run(debug=True)
