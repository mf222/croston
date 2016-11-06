def generar_archivo(numero_vectores):
    '''Esta funcion genera el archivo. Ahora si recibe parámetros.
    Debe retornar un par (nombre, contenido) donde nombre es el
    nombre del archivo, y contenido es un string con su contenido'''

    # Generamos el contenido
    contenido = '#ingrese los componentes de vectores'
    for i in range(numero_vectores):
        vector = '0,' * 4
        contenido += '\n' + vector[:-1]

    # Retornamos un par con el nombre y el contenido
    return ('analisis.csv', contenido)
