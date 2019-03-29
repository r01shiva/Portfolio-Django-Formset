from django import forms
from . models import  Data, Skills




class DataF(forms.ModelForm):

    class Meta:
        model = Data
        fields =['topic','point1','point2','point3']

class SkillsF(forms.ModelForm):

    class Meta:
        model = Skills
        fields =['area','percentage']


