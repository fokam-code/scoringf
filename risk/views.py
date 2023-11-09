from django.shortcuts import render
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect, request
import csv
from .forms import BookCreate
from .models import Testdata,Donnee
from django.contrib.auth import authenticate
from django.contrib import messages
import pickle
# import sklearn
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Donnee
from pathlib import Path

#DataFlair
BASE_DIR = Path(__file__).resolve().parent.parent
model_dir=BASE_DIR/'models/'
def predict(request):
    with open(model_dir,'rb') as f:
        model=pickle.load(f)
    
        if request.method=="POST":
            name=request.POST['ID']
            Id=request.POST['ID']
            person_age=request.POST['person_age']
            person_income=request.POST['person_income']
            person_home_ownership=request.POST['person_home_ownership']
            person_emp_length=request.POST['person_emp_length']
            loan_intent=request.POST['loan_intent']
            loan_grade=request.POST['loan_grade']
            loan_amnt=request.POST['loan_amnt']
            loan_int_rate=request.POST['loan_int_rate']
            loan_status=request.POST['loan_status']
            loan_percent_income=request.POST['loan_percent_income']
            cb_person_default_on_file=request.POST['cb_person_default_on_file']
            cb_person_cred_hist_length=request.POST['cb_person_cred_hist_length']
            input_data=request.POST['input_data']
            client=Donnee(ID=request.POST['ID'],
            person_age=request.POST['person_age'],
            person_income=request.POST['person_income'],
            person_home_ownership=request.POST['person_home_ownership'],
            person_emp_length=request.POST['person_emp_length'],
            loan_intent=request.POST['loan_intent'],
            loan_grade=request.POST['loan_grade'],
            loan_amnt=request.POST['loan_amnt'],
            loan_int_rate=request.POST['loan_int_rate'],
            loan_status=request.POST['loan_status'],
            loan_percent_income=request.POST['loan_percent_income'],
            cb_person_default_on_file=request.POST['cb_person_default_on_file'],
            cb_person_cred_hist_length=request.POST['cb_person_cred_hist_length'])
            client.save()
            print("client")
            #traiter les donnees 
            #utiliser le model pour effectuer 
            if person_income < 20000 :
                prediction=0
            else:
                prediction=1
            prediction=model.predict(input_data)
            return render(request,'data.html',{'prediction':prediction,'data':client})
        return render(request,'data.html')
    
#operation de crud

class ArticleListView(ListView):
    model = Donnee
    template_name = 'article_list.html'

class ArticleCreateView(CreateView):
    model = Donnee
    template_name = 'article_create.html'
    fields = ['name','person_age', 'person_income','person_age','person_income','person_home_ownership','person_emp_length','loan_intent','loan_grade','loan_amnt','loan_int_rate','loan_percent_income','cb_person_default_on_file','cb_person_cred_hist_length']

    success_url = reverse_lazy('article_list')
    def predict(request):
        with open(model_dir,'rb') as f:
            model=pickle.load(f)
        
            if request.method=="POST":
                name=request.POST['ID']
                Id=request.POST['ID']
                person_age=request.POST['person_age']
                person_income=request.POST['person_income']
                person_home_ownership=request.POST['person_home_ownership']
                person_emp_length=request.POST['person_emp_length']
                loan_intent=request.POST['loan_intent']
                loan_grade=request.POST['loan_grade']
                loan_amnt=request.POST['loan_amnt']
                loan_int_rate=request.POST['loan_int_rate']
                loan_status=request.POST['loan_status']
                loan_percent_income=request.POST['loan_percent_income']
                cb_person_default_on_file=request.POST['cb_person_default_on_file']
                cb_person_cred_hist_length=request.POST['cb_person_cred_hist_length']
                input_data=request.POST['input_data']
                client=Donnee(ID=request.POST['ID'],
                person_age=request.POST['person_age'],
                person_income=request.POST['person_income'],
                person_home_ownership=request.POST['person_home_ownership'],
                person_emp_length=request.POST['person_emp_length'],
                loan_intent=request.POST['loan_intent'],
                loan_grade=request.POST['loan_grade'],
                loan_amnt=request.POST['loan_amnt'],
                loan_int_rate=request.POST['loan_int_rate'],
                loan_status=request.POST['loan_status'],
                loan_percent_income=request.POST['loan_percent_income'],
                cb_person_default_on_file=request.POST['cb_person_default_on_file'],
                cb_person_cred_hist_length=request.POST['cb_person_cred_hist_length'])
                client.save()
                print("client")
                #traiter les donnees 
                #utiliser le model pour effectuer 
                if person_income < 20000 :
                    prediction=0
                else:
                    prediction=1
                prediction=model.predict(input_data)
                return render(request,'data.html',{'prediction':prediction,'client':client})
            return render(request,'data.html')
class Predict:
    """Provide the ability to delete objects."""
    success_url = None

    def predict(self, request, *args, **kwargs):
       
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.save()
        return HttpResponseRedirect(success_url)
class Articlepredict(Predict):
    model = Donnee
    template_name = 'article_list.html'

class ArticleUpdateView(UpdateView):
    model = Donnee
    template_name = 'article_update.html'
    fields= '__all__'
    success_url = reverse_lazy('article_list')

class Listescoring(ListView):
    model = Donnee
    template_name = 'scoring.html'
    fields = '__all__'
    success_url = reverse_lazy('resultat')

class ArticleDeleteView(DeleteView):
    model = Donnee
    template_name = 'article_delete.html'
    success_url = reverse_lazy('mise')



def listecredit(request):
    liste=Donnee.objects.all()
    return render(request,"resultat.html",{'liste': liste})
# def index(request):
#     shelf = Credit.objects.all()
#     return render(request, 'crud.html', {'shelf': shelf})

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
            return render(request, 'book/upload_form.html', {'upload_form':upload})

def update_data(request, Testdata_id):
    Testdata_id = int(Testdata_id)
    try:
        book_sel =Testdata.objects.get(id = Testdata_id)
    except Testdata.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('index')
    return render(request, 'book/upload_form.html', {'upload_form':book_form})

def delete_data(request, Donnee_id):
    Test_id = int(Donnee_id)
    try:
        book_sel = Donnee.objects.get(id = Donnee_id)
    except Testdata.DoesNotExist:
        return redirect('update')
    
    book_sel.delete()
    return redirect('update')

#avant

def charger_csv(request):   
    if request.method == 'POST' and 'fichier' in request.FILES:
        fichier_csv = request.FILES['fichier']
        print(fichier_csv)
        decoded_file = fichier_csv.read().decode('utf-8')
        csv_data = csv.reader(decoded_file.splitlines(),delimiter="\n")
        next(csv_data,None)
        for ligne in csv_data:
            data=ligne[0].split(",")
            print(data[0])
            test=Donnee( name=data[0],  person_age=data[0],  person_income=data[1],person_home_ownership=data[2],person_emp_length=data[3], loan_intent=data[4], loan_grade=data[5],loan_amnt=data[6],loan_int_rate=float(data[7]),loan_status=data[8],loan_percent_income=data[9], cb_person_default_on_file=data[10],cb_person_cred_hist_length=data[11] )
            test.save()
            print(test)
            
        return render(request,'load.html')
    return render(request,"load.html")
def home(response):
    return render(response,"index.html")

def crud(request):
    model = Donnee
    return render(request,"crud.html")
    
def data(request):
    return render(request,"data.html")

def delete(request):
    return render(request,"delete.html")

    
def indexc(response):
    return render(response,"indexc.html")

def login(response):
    return render(response,"log-in.html")

def selectfeature(request):
    return render(request,"selectfeature.html")

def itemset(render):
    return render(request,"itemset.html")
    
def scoring(request):
    return render(request,"scoring.html")

def update(request):
    return render(request,"update.html")
def create(request):
    return render(request,"create.html")
def load(request):
    return render(request,"load.html")
def resultat(request):
    return render(request,"data.html")
# def mise(request):
#     return render (request,"update.html")




def login_blog(request):
    if request.method == "POST":
        username=request.POST['username']
        pwd=request.POST["pwd"]
        user=authenticate(username=username,password=pwd)
        
        if user is not None:
           
            return redirect("indexc")
        else:
            messages.error(request,"Erreur d'authentification")
            return render(request,"login.html")
    return render(request,"login.html")
  
def mise(request):
    liste=Donnee.objects.all()
    return render(request,"update.html",{'liste': liste})        

from django.shortcuts import render
from sklearn.metrics import confusion_matrix
import numpy as np

class Predicttest(CreateView):
    model = Donnee
    template_name = 'test.html'
    fields = ['person_age', 'person_income','person_age','person_income','person_home_ownership','person_emp_length','loan_intent','loan_grade','loan_amnt','loan_int_rate','loan_status','loan_percent_income','cb_person_default_on_file','cb_person_cred_hist_length']
    success_url = reverse_lazy('resultat')


from django.shortcuts import render, redirect
from .models import Donnee
from .forms import BookCreate
from django.http import HttpResponse

#DataFlair
def index(request):
    shelf = Donnee.objects.all()
    return render(request, 'book/library.html', {'shelf': shelf})

def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('articles_list')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
            return render(request, 'book/upload_form.html', {'upload_form':upload})

def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Donnee.objects.get(id = book_id)
    except Donnee.DoesNotExist:
        return redirect('articles_list')
    book_form = BookCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('articles_list')
    return render(request, 'book/upload_form.html', {'upload_form':book_form})

def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Donnee.objects.get(id = book_id)
    except Donnee.DoesNotExist:
        return redirect('articles_list')
    book_sel.delete()
    return redirect('articles_list')


from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

def train_model(request):
    # Collecte des données
    BASE_DIR = Path(__file__).resolve().parent.parent
    model_dir=BASE_DIR/'models/'
    df= pd.read_csv(model_dir/'testdata.csv')
    
    df1= df.drop(cible, axis=1)
    df1
#selection des variables categorielles 
    categorial_data=df1.select_dtypes('object')
#selection des variables numeriques 
    numerical_data=df1.select_dtypes(['float','int'])
    
    #remplacement des valeurs manquantes 
    df.interpolate(method ='linear', limit_direction ='backward', inplace=True)
    #encodage des donnees
    from sklearn.preprocessing import LabelEncoder ,OneHotEncoder
    le=LabelEncoder()
    for colum in categorial_data.columns:
        df[colum]=le.fit_transform(df[colum])
    
    for col in numerical_data.columns:
        means=np.mean(df[col],axis=0)
        stds=np.std(df[col],axis=0)
        df[col]=(df[col]-means)/stds
    print(df)
    #importation des bibliotheque 
    from sklearn.model_selection import train_test_split
#ici
    train, test = train_test_split(df, test_size = 0.2, random_state=42)
    x_train = train.drop(cible, axis=1)
    x_test =  test.drop(cible, axis=1)
    y_train = train[cible]
    y_test =  test[cible]
#precisons  la variable cibl
    cible='loan_status'
    # Prétraitement des données


    # Entraînement du modèle
    model = LogisticRegression()
    model.fit(x_train, y_train)
# Évaluation du modèle sur les données de test
    y_pred = model.predict(x_test)

    # Calcul des métriques
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # Renvoyer les métriques au template
    return render(request, 'resultat.html', {'accuracy': accuracy, 'precision': precision, 'recall': recall, 'f1': f1})


 
