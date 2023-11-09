from django import forms
from .models import Donnee
#DataFlair
class BookCreate(forms.ModelForm):
    class Meta:
        model =Donnee
        fields = '__all__'