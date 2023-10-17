from django.template import loader
from django.http import HttpResponse
from .inferencia import MotorInferencia, Liderazgo
from .base_hechos import base_de_hechos  # Asegúrate de importar tus datos de base de hechos

def mostrar_resultados(request):
    # Crea una instancia del motor de inferencia
    motor = MotorInferencia(base_de_hechos)

    # Ejecutar el motor de inferencia
    motor.reset()
    motor.introducir_datos()
    motor.run()

    # Obtener el resultado de la inferencia
    resultado = ""
    for fact in motor.facts:
        if isinstance(fact, Liderazgo):
            resultado = fact.resultado
            break

    # Cargar la plantilla HTML
    template = loader.get_template('home.html')

    # Renderizar la plantilla con el resultado
    context = {
        'resultado': resultado,
    }
    rendered_template = template.render(context)

    # Devolver la página HTML como respuesta
    return HttpResponse(rendered_template)
