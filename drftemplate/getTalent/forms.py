from django import forms
from django.core.exceptions import ValidationError




class UserForm(forms.Form):
    email = forms.EmailField(max_length=120)
    password = forms.CharField(max_length=120)


    def clean_email(self):
        data = self.cleaned_data['email']
        if "irlandakelly@gmail.com" not in data:
            raise ValidationError("Te olvidaste de Irlanda")
        return data


'''
{
"email":"irlandakelly@gmail.com",
"password":"123456"
}
'''