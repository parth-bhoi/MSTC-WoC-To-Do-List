from .models import Task_date,Task_list
from django import forms
class home_form(forms.ModelForm):
    date_added = forms.DateField(widget = forms.SelectDateWidget(attrs = {'class':'custom-select'}))
    class Meta:
       
        model = Task_date
        fields = [
            'date_added'
        ]

class view_task_form(forms.ModelForm): 
    due_date = forms.DateField(widget = forms.SelectDateWidget(attrs = {'class':'custom-select'})) 
    class Meta:
        model = Task_list
        fields = [
            'task',
            'due_date',
            'task_date'

        ]