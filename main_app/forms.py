from django import forms 
from .models import Lesson, Teacher
from bootstrap_datepicker_plus import DateTimePickerInput

class LessonForm(forms.ModelForm):
    # add bootstrap form-control class to all text inputs
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control', 'step': 0.01}))

    class Meta:
        model = Lesson
        fields = ['name', 'description', 'price', 'time', 'level']
        # add DateTimePickerInput widget to time field
        widgets = {
            'time': DateTimePickerInput(
                options={
                    'format': 'MM/DD/YY hh:mm',
                    }), 
        }


class TeacherForm(forms.ModelForm):
    # add bootstrap form-control class to all text inputs
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    image_url = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta: 
        model = Teacher
        fields = ['full_name', 'language', 'bio', 'image_url']