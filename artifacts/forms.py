from django import forms

from .models import Artefato


class ArtefatoCreateForm(forms.ModelForm):
    class Meta:
        model = Artefato
        fields = ['projeto', 'nome', 'descricao', 'situacao', 'data_entrega']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'data_entrega': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'projeto': forms.Select(attrs={'class': 'form-select'}),
            'situacao': forms.TextInput(attrs={'class': 'form-control'}),
        }
