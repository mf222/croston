import json
import time

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic.edit import FormView
# from django.views.decorators.http import require_http_methods

from .data_processing import generar_output
from .forms import UploadForm
# from .file_generation import generar_archivo

# CONT = "application/vnd.ms-excel"
CONT = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"


class UploadView(FormView):
    template_name = "pr_home.html"
    form_class = UploadForm
    # success_url = "/producto_punto/"  # TODO: change

    def form_valid(self, form):
        xlsx = form.cleaned_data["xlsx"]
        response = HttpResponse(content_type=CONT)
        response["Content-Disposition"] = 'attachment; filename="output.xlsx"'
        xlsx.save(response)
        return response


# TODO: What to do with this?
def process_data(request):
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():  # calls UploadField.clean -> WriteToExcel
        name, elements = form.cleaned_data['data']
        html_result = generar_output(elements)
        operation_id = int(time.time())
        menu_data = {'id': operation_id, 'name': name}
        tab_data = {'content': html_result, 'id': operation_id}
        data = {'menu_html': render_to_string('pr_menu.html', menu_data),
                'tab_html': render_to_string('pr_tab.html', tab_data)}
    else:
        data = {'error': form.errors}
    return HttpResponse(json.dumps(data), content_type="application/json")
