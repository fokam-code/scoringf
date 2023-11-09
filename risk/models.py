from django.db import models





class Client(models.Model):
    nom=models.CharField( max_length=50)
    prenom=models.CharField( max_length=50)
    created_at=models.DateField( auto_now=True, auto_now_add=False)
    

    def __str__(self):
        return self.nom
    
class pret(models.Model):
    nom=models.CharField( max_length=50)
    prenom=models.CharField( max_length=50)
    created_at=models.DateField( auto_now=True, auto_now_add=False)
    

    def __str__(self):
        return self.nom

#DataFlair Models
class Testdata(models.Model):
    name= models.CharField(max_length = 50)
    # picture = models.ImageField()
    author = models.CharField(max_length = 30, default="anonyme")
    email = models.EmailField(blank = True)
    describe = models.TextField(default = "test")

    def __str__(self):
        return self.name
    
class Donnee(models.Model):
    name=models.CharField(max_length = 30, default="anonyme")
    Id=models.AutoField(primary_key=True)
    # YOB=models.IntegerField( )
    # NKID=models.IntegerField( )
    # AES=models.CharField(max_length = 30, default="anonyme")
    # DAINC=models.IntegerField( )
    # RES=models.CharField(max_length = 30, default="anonyme")
    # RES=models.CharField(max_length = 30, default="anonyme")
    person_age=models.IntegerField( )
    person_income=models.DecimalField(decimal_places=2,max_digits=30)
    person_home_ownership=models.CharField(max_length = 30, default="anonyme")
    person_emp_length=models.IntegerField()
    loan_intent=models.CharField(max_length=50,default="anonyme")
    loan_grade=models.CharField(max_length=50,default="anonyme")
    loan_amnt=models.IntegerField( )
    loan_int_rate=models.DecimalField(decimal_places=2,max_digits=30,default=0)
    loan_status=models.IntegerField(default=0)
    loan_percent_income=models.DecimalField(decimal_places=2,max_digits=30,default=0)
    cb_person_default_on_file=models.CharField(max_length=50,default="anonyme")
    cb_person_cred_hist_length=models.IntegerField()
    # score = models.FloatField(null=True, blank=True)

    


    def __str__(self):
        return self.name					
  
