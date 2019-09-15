from django import forms


class ClienteForm(forms.Form):
    error_css_class = 'alert alert-danger'

    nome = forms.CharField(widget= forms.widgets.Input(attrs ={'class':'form-control', 'placeholder':'Nome'}))
    cpf = forms.CharField(widget= forms.widgets.Input(attrs ={'class':'form-control', 'placeholder':'CPF'}))
    cidade = forms.CharField(widget= forms.widgets.Input(attrs ={'class':'form-control', 'placeholder':'Cidade'}))

    def clean(self):

        super(ClienteForm, self).clean()
        nome = self.cleaned_data.get['nome']
        cpf = self.cleaned_data.get['cpf']
        cidade = self.cleaned_data.get['cidade']

        if nome == None and cpf == None and cidade == None:
            self._errors['nome'] = self.error_class(['Digite alguma coisa nos campos!'])

        if nome == None:
            self._errors['nome'] = self.error_class(['Caixa de nome vazia!'])

        if cpf == None:
            self._errors['cpf'] = self.error_class(['Caixa de cpf vazia!'])
        
        if nome == None:
            self._errors['cidade'] = self.error_class(['Caixa de cidade vazia!'])

        return self.cleaned_data
