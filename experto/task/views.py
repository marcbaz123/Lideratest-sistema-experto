from django.template import loader
from django.http import HttpResponse
from task.engine.inferencia import MotorLiderazgo

def calcular_estilo_liderazgo():
    # Crear una instancia del motor de inferencia
    engine = MotorLiderazgo()
    engine.reset()
    engine.run()

    # Obtener el resultado del motor de inferencia
    resultado = engine.resultado

    return resultado

def mostrar_resultados(request):
    estilo_liderazgo = calcular_estilo_liderazgo()
    
    # Cargar la plantilla HTML
    template = loader.get_template('home.html')

    # Renderizar la plantilla con el resultado
    context = {
        'resultado': estilo_liderazgo,  # Usar 'resultado' como la clave en el contexto
    }
    rendered_template = template.render(context)

    # Devolver la página HTML como respuesta
    return HttpResponse(rendered_template)