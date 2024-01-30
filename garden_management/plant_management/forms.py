from django import forms
from .models import Plant, Image, RelatedURL


# 植物追加フォーム。
class AddPlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = (
            "name",
            "image",
            "watering_frequency",
            "last_watering_date",
            "description",
            "priority"
        )

    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "input",
                "placeholder": "バラ"
            }
        )
    )

    image = forms.ModelChoiceField(
        queryset=Image.objects.order_by("pk"),
        empty_label="選択してください。"
    )

    watering_frequency = forms.DurationField(
        widget=forms.TimeInput(
            attrs={
                "class": "input",
                "placeholder": "1 00:00:00"
            }
        )
    )

    last_watering_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "class": "input",
                "type": "datetime-local"
            }
        )
    )

    description = forms.CharField(
        required=False,
        max_length=4095,
        widget=forms.Textarea(
            attrs={
                "class": "textarea",
                "placeholder": (
                    "バラ（薔薇）は、バラ科バラ属の総称である[1][要ページ番号][2][要ページ番号][3][要ページ番号]。"
                    "あるいは、そのうち特に園芸種（園芸バラ・栽培バラ）を総称する[1]（花が鑑賞用や食用とされる[4] ）。"
                    "本項では、後者の園芸バラ・栽培バラを扱うこととする。\n"
                    "wikipedia「バラ」より引用。"
                )
            }
        )
    )

    priority = forms.IntegerField(
        min_value=0,
        max_value=32767,
        widget=forms.NumberInput(
            attrs={
                "class": "input",
                "placeholder": "0 ~ 32767"
            }
        )
    )


# 植物編集フォーム。
class EditPlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = (
            "name",
            "image",
            "watering_frequency",
            "last_watering_date",
            "description",
            "priority"
        )

    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "class": "input",
                "placeholder": "バラ"
            }
        )
    )

    image = forms.ModelChoiceField(
        queryset=Image.objects.order_by("pk"),
        empty_label="選択してください。"
    )

    watering_frequency = forms.DurationField(
        widget=forms.TimeInput(
            attrs={
                "class": "input",
                "placeholder": "1 00:00:00"
            }
        )
    )

    last_watering_date = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                "class": "input",
                "type": "datetime-local"
            }
        )
    )

    description = forms.CharField(
        required=False,
        max_length=4095,
        widget=forms.Textarea(
            attrs={
                "class": "textarea",
                "placeholder": (
                    "バラ（薔薇）は、バラ科バラ属の総称である[1][要ページ番号][2][要ページ番号][3][要ページ番号]。"
                    "あるいは、そのうち特に園芸種（園芸バラ・栽培バラ）を総称する[1]（花が鑑賞用や食用とされる[4] ）。"
                    "本項では、後者の園芸バラ・栽培バラを扱うこととする。\n"
                    "wikipedia「バラ」より引用。"
                )
            }
        )
    )

    priority = forms.IntegerField(
        min_value=0,
        max_value=32767,
        widget=forms.NumberInput(
            attrs={
                "class": "input",
                "placeholder": "0 ~ 32767"
            }
        )
    )


# 関連URL追加フォーム。
class AddRelatedUrlForm(forms.ModelForm):
    class Meta:
        model = RelatedURL
        fields = (
            "name",
            "url"
        )

    name = forms.CharField(
        max_length=2047,
        widget=forms.TextInput(
            attrs={
                "class": "input",
                "placeholder": "サイト名など"
            }
        )
    )

    url = forms.URLField(
        max_length=2047,
        widget=forms.URLInput(
            attrs={
                "class": "input",
                "placeholder": "niwakan.mesekit.com"
            }
        )
    )
