import random


def chatbot_responder(pregunta):
    respuestas = ["Sí", "No", "Tal vez", "por supuesto",
                  "claro que no", "No estás listo para saberlo"]
    respuesta = random.choice(respuestas)
    return respuesta


def main():
    print("")
    print("----------------------------------")
    print("")
    print("¡Hola soy tabaco y leere tu futuro!")
    print("")
    print("----------------------------------")
    print("")
    print("Hazme una pregunta que pueda responder con sí o no.")
    print("")
    print("Escribe 'fin' para terminar la conversación.")
    print("")
    print("")

    while True:
        pregunta = input("\nTú: ")

        if pregunta.lower() == 'fin':
            print("Tabaco: ¡Hasta luego! Que tengas un buen día.")
            break

        respuesta = chatbot_responder(pregunta)
        print("")
        print("----------------------------------")
        print("Tabaco: ", respuesta)
        print("")


if __name__ == "__main__":
    main()
