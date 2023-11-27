from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from store.models import Person, Course,Choices


# class UserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = [‘username’, ‘email’, ‘password1’, ‘password2’]
#         widgets = {
#             'name':forms.TextInput(attrs={'class': 'form-control'}),
#         }


class PersonCreationForm(forms.ModelForm):
    Metirials_provide = forms.ModelMultipleChoiceField(Choices.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        CHOICES = [("Male", "Male"), ("Female", "Female")]
        model = Person
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'dob':forms.DateInput(attrs={'class': 'form-control','type': 'date',},format='%d-%m-%Y'),
            'age':forms.NumberInput(attrs={'class': 'form-control'}),
            'gender':forms.RadioSelect( choices=CHOICES,),
            'phoneno':forms.NumberInput(attrs={'class': 'form-control'}),
            'email':forms.TextInput(attrs={'class': 'form-control'}),
            'address':forms.Textarea(attrs={'class': 'form-control'}),
            'department':forms.Select(attrs={'class': 'form-control'}),
            'course':forms.Select(attrs={'class': 'form-control'}),
            'purpose':forms.Select(attrs={'class': 'form-control'}),
            'Metirials_provide':forms.TextInput(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['course'].queryset = Course.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['course'].queryset = Course.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['course'].queryset = self.instance.department.course_set.order_by('name')


# NGO_CHOICES = (('one', 'ONE'), ('two', 'TWO'), ('three', 'THREE'),)

# # Create a form class with a MultipleChoiceField
# class UserForm(forms.ModelForm):
#     ngo = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=NGO_CHOICES)
#     class Meta():
#         model = Person
#         fields = ('ngo',)