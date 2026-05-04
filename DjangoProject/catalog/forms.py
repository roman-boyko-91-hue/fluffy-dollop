from django.core.exceptions import ValidationError
from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    """Список запрещенных слов"""
    FORBIDDEN_WORDS = [
        'казино', 'биржа', 'обман', 'криптовалюта',
        'дешево', 'полиция', 'крипта', 'бесплатно', 'радар'
    ]

    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price', 'category']

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        return self._validate_content(cleaned_data)

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        return self._validate_content(cleaned_data)

    def _validate_content(self, content):
        """Метод для проверки текста на запрещенные слова"""
        if content:
            lower_content = content.lower()
            for word in self.FORBIDDEN_WORDS:
                if word in lower_content:
                    raise ValidationError(f'Текст содержит запрещенное слово: "{word}"')
        return content

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

    def clean_price(self):
        price = self.cleaned_data.get('price')

        if price < 0:
            raise ValidationError('Цена не может быть отрицательной.')

        return price
