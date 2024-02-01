from django import forms
from .models import InquiryCategory


class InquiryForm(forms.Form):
    category = forms.ModelChoiceField(
        queryset=InquiryCategory.objects.order_by("-priority"),
        empty_label="選択してください。",
    )

    subject = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "input",
                "placeholder": "件名",
            }
        ),
    )

    message = forms.CharField(
        max_length=8192,
        widget=forms.Textarea(
            attrs={
                "class": "textarea",
                "placeholder": "お問い合わせ内容。",
            }
        ),
    )

    is_send_user = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                "class": "checkbox",
            }
        )
    )
