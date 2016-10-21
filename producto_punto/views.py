from django.shortcuts import render
from .data_processing import generar_output
from django.http import HttpResponse
from django.template.loader import render_to_string
from .file_generation import generar_archivo
import json
from producto_punto.forms import *
import time
from django.views.decorators.http import require_http_methods


def home(request):
    data = {'upload_form': UploadForm(), 'download_form': DownloadForm()}
    return render(request, 'pr_home.html', data)


def process_data(request):
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
        name, elements = form.cleaned_data['data']
        html_result = generar_output(elements)
        operation_id = int(time.time())
        menu_data = {'id': operation_id, 'name': name}
        tab_data = {'content': html_result, 'id': operation_id}
        data = {'menu_html': render_to_string('pr_menu.html', menu_data),
                'tab_html': render_to_string('pr_tab.html', tab_data)}
        print(data['tab_html'])
    else:
        data = {'error': form.errors}
    return HttpResponse(json.dumps(data), content_type="application/json")


@require_http_methods(["POST"])
def download_file(request):
    form = DownloadForm(request.POST)
    parameter = 0
    if form.is_valid():
        parameter = form.save()
    filename, content = generar_archivo(parameter)
    response = HttpResponse(content, content_type='text/csv')
    response['Content-Length'] = len(content)
    response['Content-Disposition'] = 'attachment; filename=' + filename
    return response
