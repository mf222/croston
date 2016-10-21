from django.template.loader import render_to_string
from pygal.style import LightGreenStyle
import pygal
# from pygal.style import LightSolarizedStyle


def generar_output(data):
    '''Recibe el segundo elemento retornado por la funcion
    validar_input para procesarlo.
    Retorna el HTML que se va a mostrar como output.'''

    # En este caso, data es una lista que contiene
    # los dos vectores data[0] y data[1]

    # calculamos el producto punto
    dotprod = 0

    # for i in range(len(data[0])):
    #     dotprod += data[0][i] * data[1][i]

    # labels = ['C' + str(i) for i in range(1, len(data[0]) + 1)]

    # creamos el grafico
    line_chart = pygal.Line(width=400,
                            height=400,
                            style=LightGreenStyle,
                            interpolate='cubic',
                            fill=True)
    line_chart.title = 'Vectores v/s índices (Interpolado)'
    # line_chart.x_labels = map(str, labels)
    # line_chart.add('Vector 1', data[0])
    # line_chart.add('Vector 2', data[1])

    # generamos el diccionario con las variables que
    # seran entregadas al renderear el html
    html_data = {
        # 'vector1': data[0],
        # 'vector2': data[1],
        # 'dotprod': dotprod,
        # 'chart': line_chart.render(),
    }

    # retornamos el render del archivo output.html
    return render_to_string('pr_output.html', html_data)
