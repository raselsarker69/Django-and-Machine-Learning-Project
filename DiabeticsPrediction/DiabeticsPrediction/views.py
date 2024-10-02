from django.shortcuts import render
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings('ignore')
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):
    # Read the CSV from the provided URL
    df = pd.read_csv('https://raw.githubusercontent.com/raselsarker69/Django-and-Machine-Learning-Project/refs/heads/main/Diabetes%20Prediction%20System/diabetes.csv')
    
    
    # Prepare the data for training
    x = df.drop('Outcome', axis=1) 
    y = df['Outcome'] 
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = LogisticRegression()
    model.fit(x_train, y_train)
    
    # Get values from the request and convert them to floats
    val1 = float(request.GET['pregnancies'])
    val2 = float(request.GET['glucose'])
    val3 = float(request.GET['bloodpressure'])
    val4 = float(request.GET['skinthickness'])
    val5 = float(request.GET['insulin'])
    val6 = float(request.GET['bmi'])
    val7 = float(request.GET['diabatic'])
    val8 = float(request.GET['age'])

    # Make prediction using the trained model
    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
    
    # Determine the result based on prediction
    result1 = "Positive" if pred == [1] else "Negative"
    
    messages.success(request,"Positive" if pred == [1] else "Negative") 
    # Return the result to the template
    return render(request, 'predict.html', {"result2": result1})

    
    # result1=""
    # if pred==[1]:
    #     result1 = "Positive"
    # else: 
    #     result1 = "Negative"