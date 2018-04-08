from django import forms

class RegForm(forms.Form):
    firstName = forms.CharField(label='FirstName',max_length=100)
    lastName = forms.CharField(max_length=100)
    rollno = forms.CharField(max_length=100)
    todate = forms.DateField()
    fromdate = forms.DateField()
    noofmembers = forms.IntegerField(min_value=0)
    personname = forms.CharField(max_length=100)
    personage = forms.IntegerField(min_value=0)
    id = forms.ImageField()
