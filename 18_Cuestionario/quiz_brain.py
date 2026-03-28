class QuizBrain:
    def __init__(self,lista_pregunta):
        self.numero_pregunta=0
        self.lista_pregunta = lista_pregunta
        self.puntuacion=0

    def aun_hay_preguntas(self):
        return self.numero_pregunta<len(self.lista_pregunta)
    
    def nueva_pregunta(self):
        pregunta_actual=self.lista_pregunta[self.numero_pregunta]
        self.numero_pregunta+=1
        respuesta_usuario=input(f"P.{self.numero_pregunta} {pregunta_actual.text} (Cierto/Falso): ")
        self.revision(respuesta_usuario,pregunta_actual.answer)

    def revision(self,respuesta_usuario, respuesta_pregunta):
        if respuesta_usuario.lower()==respuesta_pregunta.lower():
           print("Correcto")
           self.puntuacion+=1
        else:
            print("Incorrecto")
        
        print(f"Tu puntuación es: {self.puntuacion}/{self.numero_pregunta}\n\n")

        