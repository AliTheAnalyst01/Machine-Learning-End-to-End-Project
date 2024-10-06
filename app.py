from flask import Flask, render_template, request
import os
import pandas as pd
import numpy as np
from MLProject_WineQT.pipeline.prediction import PredictionPipeline

app = Flask(__name__) # initialize the flask


app.route('/',methods=["GET"])
def homePage():
    return render_template("index.html")


@app.route('/train',methods=['GET'])  # route to trian the pipeline
def training():
    os.system("python main.py")
    return "Training Successful" 


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)