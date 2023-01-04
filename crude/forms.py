from django import forms
from django.core import validators
from datetime import date
from .models import Todo


# def notinteger(value):
#     if value[0]==int:
#         raise forms.ValidationError('first letter integer not allowed')



# class Todoforms(forms.Form):
#     today_date = forms.DateField(initial=date.today())
#     topic = forms.CharField(required=True,error_messages={"required":"please enter topic"},validators=[validators.MaxLengthValidator(100)])
#     describe = forms.CharField(widget=forms.TextInput,required=True,error_messages={'required':"this field is required",'max_length':"enter less than 1000 words"})
#     time_remaning = forms.CharField(max_length=2,widget=(forms.NumberInput),required=True,error_messages={'required':"this field is required"})

#     def clean_time_remaning(self):
#         value = self.cleaned_data['time_remaning']
#         if value[0] ==str:
#             raise forms.ValidationError('first letter should be integer ')
#         return value

    
#     def clean_topic(self):
#         data = self.cleaned_data['topic']
#         if Todo.objects.filter(topic=data).exists():
#             raise forms.ValidationError("This data is already in the database")
#         return data





class Todoforms(forms.ModelForm):
    class Meta:
        model= Todo
        fields = ['topic','describe','time_remaning']
        # OR
        
        # fields = '__all__'
        # exclude = ('topic','time_remaning')

       
    def clean_topic(self):
        data = self.cleaned_data['topic']
        if Todo.objects.filter(topic=data).exists():
            raise forms.ValidationError("This data is already in the database")
        return data
