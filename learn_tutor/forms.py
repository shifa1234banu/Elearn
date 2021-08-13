from django import forms
from .models import Course



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('video1','video2','video3','video4','video5','video6','video7','video8','preview_video','course_name','course_des','short_des','category','price','course_image','tutor_name')
    
    
    def __init__(self, *args ,**kwargs):
        super(CourseForm,self).__init__(*args ,**kwargs)
        



        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'  