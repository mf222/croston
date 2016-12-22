from django import forms
from multiupload.fields import MultiFileField
from ..operations.spreadsheets import run_operation, parse_files

ERR_MESSAGE = "Ha ocurrido un error, archivo corrupto o mal formado"
ERR_NULLFILE = "Debe ingresar los archivos primero"

class UploadForm(forms.Form):
    attachments = MultiFileField(min_num=2, max_num=2)

    def clean(self):
        cleaned_data = super(UploadForm, self).clean()

        file1, file2 = None, None
        try:
            for form_file in cleaned_data.get('attachments'):
                path = form_file.file.name
                # form_file.file.seek(0)
                # content = form_file.file.read()

                if form_file._name == "INPUT1.xlsx":
                    file1 = path
                elif form_file._name == "INPUT2.xlsx":
                    file2 = path
                else:
                    if file1 is None:
                        file1 = path
                    elif file2 is None:
                        file2 = path
                # elif file1 is None:
                #     file2 = path
                # elif file2 is None:
                #     file1 = path
        except Exception as e:
            raise forms.ValidationError(ERR_NULLFILE)
        try:
            xlsx = run_operation(*parse_files(file1, file2))
            cleaned_data["xlsx"] = xlsx
            return cleaned_data
            # xlsx.save("producto_punto/static/analisis.xlsx")
        except Exception as e:
            # raise e
            raise forms.ValidationError(ERR_MESSAGE)
