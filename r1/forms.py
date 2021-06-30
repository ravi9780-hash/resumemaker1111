from django import forms
from  .models import myimg
class imgform(forms.ModelForm):
    class  Meta:
         model = myimg
         fields = ['id', 'img']