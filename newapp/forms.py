from django import forms
from newapp.models import Form


class StudentForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['name','dob','age','gender','phn','email','address','department','course','Purpose','debit','note_book','pen','exam_papper']

