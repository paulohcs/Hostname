from django import forms

class HostnameForm(forms.Form):
    mac = forms.CharField(label='mac', max_length=17)
    ip = forms.CharField(label='ip', max_length=15)

class CreateForm(forms.Form):
    hostname = forms.CharField(label='hostname')
    mac = forms.CharField(label='mac', max_length=17)
    ip = forms.CharField(label='ip', max_length=15)

class RetrieveForm(forms.Form):
    hostname = forms.CharField(label='hostname')
    mac = forms.CharField(label='mac', max_length=17)
    ip = forms.CharField(label='ip', max_length=15)

class EditForm(forms.Form):
    id = forms.CharField(label='id')
    hostname = forms.CharField(label='hostname')
    mac = forms.CharField(label='mac', max_length=17)
    ip = forms.CharField(label='ip', max_length=15)

class DeleteForm(forms.Form):
    hostname = forms.CharField(label='hostname')
    mac = forms.CharField(label='mac', max_length=17)
    ip = forms.CharField(label='ip', max_length=15)

class DeleteForm2(forms.Form):
    id = forms.CharField(label='id')
