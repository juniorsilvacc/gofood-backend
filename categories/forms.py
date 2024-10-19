from django import forms
from categories.models import Category


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data.get('name')

        if not name:
            raise forms.ValidationError('O nome da categoria não pode estar vazio.')

        if Category.objects.filter(name=name).exists():
            raise forms.ValidationError('Já existe uma categoria com esse nome.')
        return name
