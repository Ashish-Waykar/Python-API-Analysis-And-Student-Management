from django import forms
from .models import *

class EditStudent(forms.ModelForm):
    class Meta:
        model = student
        fields = ['s_name','branch','year','mail','mobile']


class CreateStudent(forms.ModelForm):
    class Meta:
        model = student
        fields = ['s_roll','s_name','branch','year','mail','mobile']

    def __init__(self, *args, **kwargs):
        super(CreateStudent, self).__init__(*args, **kwargs)
        # self.fields['s_name'].widget.attrs['placeholder'] = 'Full Name'
        # self.fields['branch'].widget.attrs['placeholder'] = 'Branch Name'
        # self.fields['mobile'].widget.input_type = 'number'
        # self.fields['mail'].widget.input_type = 'mail'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class EditResult(forms.ModelForm):
    class Meta:
        model = result
        fields = ['name','branch','year','s_marksheet']

class CreateResult(forms.ModelForm):
    class Meta:
        model = result
        fields = ['reg_no','name','branch','year','s_marksheet']
    def __init__(self, *args, **kwargs):
        super(CreateResult, self).__init__(*args, **kwargs)
        # self.fields['s_name'].widget.attrs['placeholder'] = 'Full Name'
        # self.fields['branch'].widget.attrs['placeholder'] = 'Branch Name'
        # self.fields['mobile'].widget.input_type = 'number'
        # self.fields['mail'].widget.input_type = 'mail'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
