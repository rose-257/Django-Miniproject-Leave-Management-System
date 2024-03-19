from django import forms
from .models import student,leaverequest,Teacher

class StudentForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=student.Genderchoices,widget=forms.RadioSelect)
    class Meta:
        model =student
        
        fields = ('name','age','email','phone','password','department','gender')
        
        widgets = {
            
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'})
        }

class LeaveForm(forms.ModelForm):
    class Meta:
        model =leaverequest
        
        fields = ('student','date','days','reason','leaveapprovalstatus')
        
        widgets = {
            'date':forms.DateInput(attrs={'class':'form-control','type': 'date'}),
            'days':forms.NumberInput(attrs={'class':'form-control'}),
            'reason':forms.TextInput(attrs={'class':'form-control'}),
        }


class TeacherRegForm(forms.ModelForm):
    class Meta:
        model = Teacher
        
        fields = ('name','age','email','phone','password','department','loginapproval')
        
        widgets = {
            
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.NumberInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'})
        }        