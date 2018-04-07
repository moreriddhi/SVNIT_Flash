from django import forms

class RegForm(forms.Form):
    firstName = forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=100)
    rollno = forms.CharField(max_length=100)
    todate = forms.DateField()
    fromdate = forms.DateField()
    noofmembers = forms.NumberInput()
    personfirstname = forms.CharField(max_length=100)
    personlastname = forms.CharField(max_length=100)
