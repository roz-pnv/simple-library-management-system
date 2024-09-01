from django import forms
from .models import *

class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        label='Author',
        required=False,
        empty_label='Select an author or add new'
    )
    new_author = forms.CharField(label='New Author', max_length=250, required=False)

    price = forms.ModelChoiceField(
        queryset=Price.objects.all(),
        label='Price',
        required=False,
        empty_label='Select a price or add new'
    )
    new_price = forms.IntegerField(label='New Price', max_value=None, required=False)


    class Meta:
        model = Book
        fields = ['name', 'author', 'new_author', 'price', 'new_price', 'category']

    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data.get("author")
        new_author = cleaned_data.get("new_author")
        price = cleaned_data.get("price")
        new_price = cleaned_data.get("new_price")

        if not author and not new_author:
            raise forms.ValidationError("Please select an existing author or enter a new author name.")

        if author and new_author:
            raise forms.ValidationError("Please either select an existing author or enter a new author, not both.")
        
        if not price and not new_price:
            raise forms.ValidationError("Please select an existing price or enter a new price.")
        
        if price and new_price:
            raise forms.ValidationError("Please either select an existing price or enter a new price, not both.")

        return cleaned_data