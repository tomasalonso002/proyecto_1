from django import forms
from .models import Tarea

class TareaForms(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ["nombre","completada","fecha_completado", "responsable"]