from django import forms

class NameForm(forms.Form):
    first_name = forms.CharField(label='first_name',max_length=30)
    last_name = forms.CharField(label = 'last_name',max_length=30)
    email = forms.CharField(label='email',max_length=50)
    phone = forms.CharField(label='phone',max_length=30)
    desc_data = forms.CharField(label='desc_data',max_length=300)
