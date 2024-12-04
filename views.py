from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.http import HttpResponseRedirect
from django.contrib import messages
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def blog(request):
    return render(request,"blog.html")
def blogdetails(request):
    return render(request,"blog-details.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
def doctors(request):
    return render(request,"doctors.html")



# Create your views here.
def register(request):
    if request.method=="POST":
        fn=request.POST['FName']
        ln=request.POST['LName']
        un=request.POST['UName']
        em=request.POST['Email']
        p1=request.POST['psw']
        p2=request.POST['psw1']
        if p1==p2:
            if User.objects.filter(username=un).exists():
                messages.info(request,"Username Exists")
                return render(request,"register.html")
            elif User.objects.filter(email=em).exists():
                messages.info(request,"Email Exists")
                return render(request,"register.html")
            else:
                user=User.objects.create_user(first_name=fn,last_name=ln,
                email=em,username=un,password=p2)
                user.save()
                return HttpResponseRedirect('login')
        else:
            messages.info(request,"Password Not Matching")
            return render(request,"register.html")
    else:
        return render(request,"register.html")
    return render(request,"register.html")
       


def login(request):
    if request.method=="POST":
        un=request.POST['UName']
        p1=request.POST['psw']
        user=auth.authenticate(username=un,password=p1)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,"login.html")
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def predict(request):
    if request.method=="POST":
        Year=int(request.POST['year'])
        Schizophrenia_disorders=float(request.POST['schizophrenia_disorders'])
        Depressive_disorders=float(request.POST['depressive_disorders'])
        Anxiety_disorders=float(request.POST['anxiety_disorders'])
        Bipolar_disorders=float(request.POST['bipolar_disorders'])
        Eating_disorders=float(request.POST['eating_disorders'])
        import numpy as np 
        import pandas as pd 
        mh=pd.read_csv(r"static/datasets/mental.csv")
        print(mh.shape)
        print(mh.info())
        print(mh.describe().transpose())
        mh.columns = ['Year' , 'Schizophrenia disorders' , 'Depressive disorders' , 'Anxiety disorders' , 'Bipolar disorders' , 'Eating disorders']
        print(mh.head(1))
        print(mh.isnull().sum())
        Schizo_mean = mh['Schizophrenia disorders'].mean()
        Depression_mean = mh['Depressive disorders'].mean()
        Anxiety_mean = mh['Anxiety disorders'].mean()
        Bipolar_mean = mh['Bipolar disorders'].mean()
        Eating_mean = mh['Eating disorders'].mean()
        mean_list = [Schizo_mean, Depression_mean, Anxiety_mean, Bipolar_mean, Eating_mean]
        mean_list
        from sklearn.model_selection import train_test_split
        X = mh.drop(['Country', 'Year'], axis=1)
        y = mh['Schizophrenia disorders']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        print("X_train shape:", X_train.shape)
        print("X_test shape:", X_test.shape)
        print("y_train shape:", y_train.shape)
        print("y_test shape:", y_test.shape)
        
        from sklearn.ensemble import RandomForestRegressor
        from sklearn.metrics import mean_squared_error, r2_score
        rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

        rf_model.fit(X_train, y_train)
        y_pred = rf_model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        print(f"Mean Squared Error: {mse}")
        print(f"R-squared: {r2}")

        import numpy as np 
        prediction_data=np.array([[Year,Schizophrenia_disorders,Depressive_disorders,Anxiety_disorders,Bipolar_disorders,Eating_disorders]],dtype=object)
        prediction_mental=rf_model.predict(prediction_data)
        return render(request,"prediction.html",{"year":Year,"schizophrenia_disorders":Schizophrenia_disorders,"depressive_disorders":Depressive_disorders,
        "anxiety_disorders":Anxiety_disorders,"bipolar_disorders":Bipolar_disorders,"eating_disorders":Eating_disorders,"prediction":prediction_mental})
    else:
        return render(request,"predict.html")
    return render(request,"predict.html")
    return render(request,"predict.html")

def prediction(request):
    return render(request,"prediction.html")