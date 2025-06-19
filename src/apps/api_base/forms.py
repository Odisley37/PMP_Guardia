from django import forms

from .models import Policial


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
