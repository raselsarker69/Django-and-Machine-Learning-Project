from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')


def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # # Create the path for the CSV file relative to the base directory
    # csv_file_path = os.path.join(BASE_DIR, 'data', 'diabetes.csv')
    
    # df = pd.read_csv(r'C:\Windows\System32\cmd.exe\diabetes.csv')
    # Get the base directory path
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # # Create the path for the CSV file relative to the base directory
    # csv_file_path = os.path.join(BASE_DIR, 'data', 'diabetes.csv')
    
    # Read the CSV file using the correct path
    #df = pd.read_csv(r'F:\\Django & ML Projects\\DiabeticsPrediction\\data\\diabetes.csv')
    df = pd.read_csv(r'../static/image/diabetes.csv')
    
    
    x = df.drop('Outcome', axis=1) 
    y = df['Outcome'] 
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    
    model = LogisticRegression()
    model.fit(x_train, y_train)
    
    
    val1 = float(request.GET['pregnancies'])
    val2 = float(request.GET['glucose'])
    val3 = float(request.GET['bloodpressure'])
    val4 = float(request.GET['skinthickness'])
    val5 = float(request.GET['insulin'])
    val6 = float(request.GET['bmi'])
    val7 = float(request.GET['diabatic'])
    val8 = float(request.GET['age'])

    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
    
    result1=""
    if pred==[1]:
        result1 = "Positive"
    else: 
        result1 = "Negative"
        
    return render(request, 'result.html', {"result2: result1"})