from experta import Rule, Fact, KnowledgeEngine, P, DefFacts

class EstiloLiderazgo(Fact):
    pass

class MotorLiderazgo(KnowledgeEngine):
    
    @DefFacts()
    def datos_iniciales(self):
        total_orientacion_personas = 0
        total_orientacion_produccion = 0

        for i in range(1, 19):
            while True:
                respuesta = int(input(f"Ingresa la calificación (0-5) para la pregunta {i}: "))
                if 0 <= respuesta <= 5:
                    break
                else:
                    print("La calificación debe estar en el rango de 0 a 5. Inténtalo de nuevo.")
            
            if i in [1, 4, 6, 9, 10, 12, 14, 16, 17]:
                total_orientacion_personas += respuesta
            else:
                total_orientacion_produccion += respuesta
        
        total_orientacion_personas *= 0.2
        total_orientacion_produccion *= 0.2
        print("La calificacion obtenida en Orientada a Gente es: ",total_orientacion_personas)
        print("La calificacion obtenida en Orientada a Tareas es: ",total_orientacion_produccion)
        yield EstiloLiderazgo(total_orientacion_personas=total_orientacion_personas, total_orientacion_produccion=total_orientacion_produccion)

    @Rule(
        EstiloLiderazgo(total_orientacion_personas=P(lambda x: x <= 5), total_orientacion_produccion=P(lambda x: x <= 5))
    )
    def rule_ajeno(self):
        print("Resultado: Estilo de liderazgo: Ajeno (Indiferente en lo social y en las tareas)")

    @Rule(
        EstiloLiderazgo(total_orientacion_personas=P(lambda x: x <= 6), total_orientacion_produccion=P(lambda x: x >= 6))
    )
    def rule_social(self):
        print("Resultado: Estilo de liderazgo: Social (Centrado en lo social)")

    @Rule(
        EstiloLiderazgo(total_orientacion_personas=P(lambda x: x >= 6), total_orientacion_produccion=P(lambda x: x <= 6))
    )
    def rule_autoritario(self):
        print("Resultado: Estilo de liderazgo: Autoritario (Centrado en las tareas)")

    @Rule(
        EstiloLiderazgo(total_orientacion_personas=P(lambda x: x >= 6), total_orientacion_produccion=P(lambda x: x >= 6))
    )
    def rule_equipo(self):
        print("Resultado: Estilo de liderazgo: Líder de equipo (Centrado en lo social y en las tareas)")

if __name__ == "__main__":
    engine = MotorLiderazgo()
    engine.reset()
    engine.run()