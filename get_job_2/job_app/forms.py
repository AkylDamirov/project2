from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import JobsModel
from django.core.validators import MaxValueValidator

class NewUserFrom(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserFrom, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class AddVacancy(forms.ModelForm):
    class Meta:
        model = JobsModel
        fields = ('image', 'company_name','work_position', 'country','description', 'salary', 'phone_number', 'email')

    def valid_salary(self):
        salary_field = self.cleaned_data.get('salary')
        if salary_field is not None and salary_field >999999:
            raise forms.ValidationError('Value entered exceeds maximum length')
        return salary_field












