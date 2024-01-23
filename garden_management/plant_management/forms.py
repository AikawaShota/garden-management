from django import forms
from . import models


class PlantForm(forms.ModelForm):
    class Meta:
        model = models.Plant
        fields = (
            'name',
            'image',
            'watering_frequency',
            'last_watering_date',
            'description',
            'priority'
        )

    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                'class': 'input',
                'placeholder': 'バラ'
            }
        )
    )

    image = forms.ModelChoiceField(
        queryset=models.Image.objects.order_by('pk'),
        empty_label='デフォルト画像'
    )

    watering_frequency = forms.DurationField(
        widget=forms.TimeInput(
            attrs={
                'class': 'input',
                'placeholder': '1 00:00:00'
            }
        )
    )

    last_watering_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'class': 'input',
                'type': 'datetime-local'
            }
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'textarea',
                'placeholder': 'バラ（薔薇）は、バラ科バラ属の総称である[1][要ページ番号][2][要ページ番号][3][要ページ番号]。あるいは、そのうち特に園芸種（園芸バラ・栽培バラ）を総称する[1]（花が鑑賞用や食用とされる[4] ）。本項では、後者の園芸バラ・栽培バラを扱うこととする。\nwikipedia「バラ」より引用。'
            }
        )
    )

    priority = forms.IntegerField(
        min_value=0,
        max_value=32767,
        widget=forms.NumberInput(
            attrs={
                'class': 'input',
                'placeholder': '0 ~ 32767'
            }
        )
    )


class RelatedUrlForm(forms.ModelForm):
    class Meta:
        model = models.RelatedURL
        fields = (
            'name',
            'url'
        )
