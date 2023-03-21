from django import forms

from grafico.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'text': forms.TextInput(
                attrs={
                    'class': 'form-control my-4'
                }
            )
        }
