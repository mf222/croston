from django import forms
from .widgets import *
from .validators import validar_input


class UploadField(forms.FileField):

    def __init__(self, attrs):
        super(UploadField, self).__init__()
        self.widget = UploadFileWidget(attrs=attrs)

    def clean(self, data, initial=None):
        super(UploadField, self).clean(data)
        data.seek(0)
        result = validar_input(data.read())
        if result[0]:
            return (data.name, result[1])
        else:
            raise forms.ValidationError(result[1])


class UploadForm(forms.Form):

    data = UploadField(attrs={'placeholder': 'Arrastrar archivos aquí',
                              'button_text': 'Abrir'})


class DownloadForm(forms.Form):

    # numero_vectores = forms.IntegerField(label='Número de vectores')

    def save(self):
        cleaned_data = super(DownloadForm, self)
        return cleaned_data
