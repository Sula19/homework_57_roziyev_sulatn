from django import forms
from webapp.models import Tasks
from django.core.exceptions import ValidationError


class TasksForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('summary', 'description', 'status', 'type')
        labels = {
            'summary': 'Кратоке описание',
            'description': 'Описание',
            'status': 'Статус',
            'type': 'Тип',
        }

    def clean_summary(self):
        summary = self.cleaned_data.get('summary')
        if len(summary) < 3:
            raise ValidationError('Поле summary должно быть не менее 3 символов')
        return summary

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 3:
            raise ValidationError('Поле description должно быть не менее 3 символов')
        return description
