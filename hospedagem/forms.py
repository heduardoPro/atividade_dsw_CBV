from django import forms
from .models import Cliente, Quarto,  Hospedagem

class HospedagemForm(forms.ModelForm):
    class Meta:
        model=Hospedagem
        fields='__all__'
        widgets = {
            'data_entrada' : forms.DateInput(attrs={'class': 'form-control' }),
            'data_saida' : forms.DateInput(attrs={'class': 'form-control' }),
            'valor' : forms.NumberInput(attrs={'class': 'form-control' }),
            'cliente': forms.Select(attrs={'class': 'form-control' }),
            'quarto': forms.Select(attrs={'class': 'form-control' })
        }

class HospedagemFilterForm(forms.Form):
    data_entrada = forms.DateField(required=False)
    data_saida = forms.DateField(required=False)
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.all(), required=False)
    quarto = forms.ModelChoiceField(queryset=Quarto.objects.all(), required=False)
    
    # adicionar a classe form-control para todos os campos
    def __init__(self, *args, **kwargs):
        super(HospedagemFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'