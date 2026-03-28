from question_model import Pregunta
from quiz_brain import QuizBrain
from data import compilaciones

banco_preguntas =[]
for compilacion in compilaciones:
    texto_pregunta=compilacion["text"]
    respuesta_pregunta=compilacion["answer"]
    nueva_pregunta=Pregunta(text=texto_pregunta,answer=respuesta_pregunta)
    banco_preguntas.append(nueva_pregunta)

quiz=QuizBrain(banco_preguntas)

while quiz.aun_hay_preguntas():
    quiz.nueva_pregunta()

print("Has completado el cuestionario")
print(f"Tu puntaje final es de: {quiz.puntuacion}/{len(banco_preguntas)}")

