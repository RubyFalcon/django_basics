from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "body", "author","is_published"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Your title"}),
            "body": forms.Textarea(attrs={
                "placeholder": "Your description",
                "class": "new-class-name-two",
                "id": "my_id",
                "rows": 20,
                "cols": 120,
            }),
        }

