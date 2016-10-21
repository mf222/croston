from django import forms
from django.template.loader import render_to_string


class UploadFileWidget(forms.widgets.FileInput):
    def render(self, name, value, attrs=None):
        data = {'attrs': self.attrs, 'name': name}
        return render_to_string('_upload_file_widget.html', data)
