from django import forms 
from .models import Lesson, Teacher
from bootstrap_datepicker_plus import DateTimePickerInput

class LessonForm(forms.ModelForm):
    # time = forms.DateField(widget = DateTimePickerInput())
    class Meta:
        model = Lesson
        fields = ['name', 'description', 'price', 'time', 'level']
        widgets = {
            'time': DateTimePickerInput(
                options={
                    'format': 'MM/DD/YY hh:mm',
                    }), 
            
        }



class TeacherForm(forms.ModelForm):
    class Meta: 
        model = Teacher
        fields = ['full_name', 'language', 'bio']