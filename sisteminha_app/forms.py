from django import forms


class ClienteForm(forms.Form):
    error_css_class = 'alert alert-danger'
    
    nome = forms.CharField(widget= forms.widgets.Input(attrs ={'class':'form-control', 'placeholder':'Nome'}))
    cpf = forms.CharField(widget= forms.widgets.Input(attrs ={'class':'form-control', 'placeholder':'CPF'}))
    cidade = forms.CharField(widget= forms.widgets.Input(attrs ={'class':'form-control', 'placeholder':'Cidade'}))