from django import forms

from .models import Agressor, Assistida, Guarnicao, GuarnicaoIntegrante, Policial


class PolicialForm(forms.ModelForm):
    class Meta:
        model = Policial
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update(
                {
                    "class": "form-control",  # classe Bootstrap padrão
                    "placeholder": field.label,
                }
            )


class AssistidaForm(forms.ModelForm):
    class Meta:
        model = Assistida
        fields = "__all__"
        widgets = {
            "numero_processo": forms.TextInput(attrs={"class": "form-control"}),
            "nome_completo": forms.TextInput(attrs={"class": "form-control"}),
            "nome_mae": forms.TextInput(attrs={"class": "form-control"}),
            "nome_pai": forms.TextInput(attrs={"class": "form-control"}),
            "cpf": forms.TextInput(attrs={"class": "form-control"}),
            "data_nascimento": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "identidade": forms.TextInput(attrs={"class": "form-control"}),
            "endereco": forms.Textarea(attrs={"class": "form-control"}),
            "longitude": forms.TextInput(attrs={"class": "form-control"}),
            "latitude": forms.TextInput(attrs={"class": "form-control"}),
            "data_visita": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "validade_processo": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "agressor_citado": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "ultima_visita": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "ocorrencia": forms.Textarea(attrs={"class": "form-control"}),
            "cancelar_atendimento": forms.CheckboxInput(
                attrs={"class": "form-check-input"}
            ),
        }


class AgressorForm(forms.ModelForm):
    class Meta:
        model = Agressor
        fields = "__all__"
        widgets = {
            "nome_completo": forms.TextInput(attrs={"class": "form-control"}),
            "identidade": forms.TextInput(attrs={"class": "form-control"}),
            "cpf": forms.TextInput(attrs={"class": "form-control"}),
            "data_nascimento": forms.DateInput(
                attrs={"class": "form-control", "type": "date"}
            ),
            "endereco": forms.Textarea(attrs={"class": "form-control"}),
            "longitude": forms.TextInput(attrs={"class": "form-control"}),
            "latitude": forms.TextInput(attrs={"class": "form-control"}),
            "foto": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }


class GuarnicaoForm(forms.ModelForm):
    class Meta:
        model = Guarnicao
        fields = "__all__"
        widgets = {
            "inicio_servico": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "fim_servico": forms.DateTimeInput(
                attrs={"class": "form-control", "type": "datetime-local"}
            ),
            "km_inicial": forms.NumberInput(attrs={"class": "form-control"}),
            "km_final": forms.NumberInput(attrs={"class": "form-control"}),
            "vtr_pmp": forms.Select(attrs={"class": "form-select"}),
        }


class GuarnicaoIntegranteForm(forms.ModelForm):
    class Meta:
        model = GuarnicaoIntegrante
        fields = "__all__"
        widgets = {
            "guarnicao": forms.Select(attrs={"class": "form-select"}),
            "policial": forms.Select(attrs={"class": "form-select"}),
            "funcao": forms.Select(attrs={"class": "form-select"}),
        }
