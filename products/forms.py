# products/forms.py
from django import forms
from .models import Review, Product, Category


class ReviewForm(forms.ModelForm):
    """Form for creating and editing product reviews"""

    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, f'{i} Star{"s" if i > 1 else ""}') for i in range(1, 6)]), #rates using star values
            'comment': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write your review here...' #placeholder text for the comment field
            }),
        }
        labels = {
            'rating': 'Rating',
            'comment': 'Your Review',
        }


class ProductForm(forms.ModelForm):
    """Form for superusers to add and edit products"""

    class Meta:
        model = Product
        fields = ['name', 'sku', 'description', 'price', 'image', 'categories']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'categories': forms.CheckboxSelectMultiple(),
        }
