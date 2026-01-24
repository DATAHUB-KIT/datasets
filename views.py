from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse

from sklearn import metrics

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

def index(request): 
	return render(request, "index.html") 

# Create your views here.
def predict(request): 
	return render(request, "predict.html") 


def result(request): 
    data = pd.read_csv('diabetes.csv')
    X = data[['Glucose','BloodPressure','Insulin','BMI','Age']]
    y = data.Outcome 
    #from sklearn.model_selection import train_test_split
    #X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)
    model = LogisticRegression() 
    model.fit(X, y) 
    val1 = float(request.GET['Glucose']) 
    val2 = float(request.GET['Bloodpressure']) 
    val3 = float(request.GET['Insulin']) 
    val4 = float(request.GET['BMI']) 
    val5 = float(request.GET['Age']) 
    pred = model.predict([[val1, val2, val3,val4, val5]]) 
    result = "" 
    if pred == [0]: 
        result = "<h1>You are not diabetic.</h1>"
    else: 
        
        result= "<h1>You are diabetic.</h1>"
    return HttpResponse(result)

#####################################################################################################

from django.contrib import admin
from django.urls import path
from diabeticapp import views
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index), 
    path("predict/", views.predict), 
    path("predict/result", views.result), 
]

##################################################################################################


index.html


<html>
<body> 
	<div> 
		<h1>Welcome to Diabetic prediction Project</h1> 
		<br> 
		<form action="predict"> 
			<button class="btn" type="submit">Click Here</button> 
		</form> 
	</div> 



</body> 

</html>


###########################################################################3


result.html

<Html>  
    <head>   
    <title>  
    Patient Input Form 
    </title>  
    </head>  
    <body bgcolor="Lightskyblue">  
    <br>  
    <br>  
    <form action="result">  
      
    <label> Glucose </label>         
    <input type="text" name="Glucose" size="15"/> <br> <br>  
    <label> BloodPressure </label>     
    <input type="text" name="Bloodpressure" size="15"/> <br> <br>  
    <label> Insulin </label>         
    <input type="text" name="Insulin" size="15"/> <br> <br>
    <label> BMI </label>         
    <input type="text" name="BMI" size="15"/> <br> <br>    
    <label> Age</label>         
    <input type="text" name="Age" size="15"/> <br> <br>  

    
    <input class="predict" type="submit" value="PREDICT"> 
    </form>  
    </body>  
    </html>  

