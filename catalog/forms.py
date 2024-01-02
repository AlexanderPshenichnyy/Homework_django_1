from django import forms

from catalog.models import Product, Version


class FormStyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.ChoiceField):
                field.widget.attrs['class'] = 'form-select'
            elif isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


def check_title_and_description(phrase):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                       'радар']
    for word in forbidden_words:
        if word in phrase.lower():
            raise forms.ValidationError(f'Запрещенное слово! {word}')


class ProductForm(FormStyleMixin, forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('owner',)

    def clean_title(self):
        cleaned_data = self.cleaned_data.get('title')
        check_title_and_description(cleaned_data)
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        check_title_and_description(cleaned_data)
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
