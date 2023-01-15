from django import forms
from .models import Qrcode


class QrcodeForm(forms.ModelForm):
    class Meta:
        model = Qrcode

        fields = [
            'nome',
            'link',
        ]