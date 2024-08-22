import os
import time
import datetime
import keyboard
import tkinter as tk
from time import sleep

os.system("cls")

def toggle_console():
    if root.state() == 'withdrawn':
        root.deiconify()
    else:
        root.withdraw()

def start_timer():
    print("Iniciando temporizador...")
    # Aquí puedes agregar la lógica del temporizador
    pass

def show_ghost_info():
    while True:
        os.system('cls')  # Limpia la pantalla al inicio de la función
        print("Escribe el nombre del tipo de fantasma del que quieres saber o elige una opción:")
        print("(A) Ver atajos de fantasma.")
        print("(B) Salir.")
        user_input = input("Escribe el nombre del fantasma o selecciona una opción --->> ").strip()

        if user_input.lower() == 'a':
            print("Mostrando atajos de fantasma... ")
            print("=" * 40)
            print("Atajos de fantasmas:")
            # Lista de fantasmas con sus códigos numéricos
            # Lista de fantasmas con sus códigos numéricos
            fantasmas = [
                "1. Espíritu", "2. Espectro", "3. Ente", "4. Poltergeist",
                "5. Banshee", "6. Jinn", "7. Pesadilla", "8. Revenant",
                "9. Sombra", "10. Demonio", "11. Yurei", "12. Oni",
                "13. Yokai", "14. Hantu", "15. Goryo", "16. Myling",
                "17. Onryo", "18. Gemelos", "19. Raiju", "20. Obake",
                "21. Mímico", "22. Morio", "23. Deogen", "24. Thaye"
            ]

            # Determina el ancho de columna, ajusta según sea necesario
            ancho_columna = 20

            # Imprime las filas de fantasmas, con cada columna alineada
            for i in range(0, len(fantasmas), 4):
                print("".join(fantasmas[j].ljust(ancho_columna) for j in range(i, min(i + 4, len(fantasmas)))))


            print("=" * 40)
            print("Ingresa (B) para regresar al menú principal.")
            user_input = input("--->> ").strip().lower()
            if user_input == 'b':
                continue #vuelve al menu info

        elif user_input.lower() == 'b':
            print("Saliendo de la sección de información sobre fantasmas...")
            break  # Sale del bucle y regresa al menú principal

        elif user_input.isdigit():
            # Aquí podrías manejar la búsqueda de información sobre el fantasma basado en el código numérico
            fantasma_id = int(user_input)
            if 1 <= fantasma_id <= 24:
                print(f"Mostrando información para el fantasma con código {fantasma_id}.")
                #1
                if fantasma_id == 1:
                    os.system('cls')
                    print("=== ESPÍRITU ===")
                    print("→ Cordura: 50%")
                    print("→ Velocidad: Normal (1.7m/s)")
                    print("→ Al utilizar un incienso (cerca o durante ataque) evitarás que ataque durante 180 segundos (3 minutos). El tiempo se cuenta desde el momento que el fantasma tiene contacto con el incienso.")
                #2
                if fantasma_id == 2:
                    os.system('cls')
                    print("=== ESPECTRO ===")
                    print("→ Cordura: 50%")
                    print("→ Velocidad: Normal (1.7m/s)")
                    print("→ Este fantasma nunca pisará la sal y se mantendrá lejos de ella.")
                    print("→ Se puede teletransportar a tu ubicación en cualquier ubicación del mapa y deja como rastro EMF 2 o 5.")
                #3
                if fantasma_id == 3:
                    os.system('cls')
                    print("=== ENTE ===")
                    print("→ Cordura: 50%")
                    print("→ Velocidad: Normal (1.7m/s)")
                    print("→ Este fantasma puede seguirte a cualquier parte del mapa incluso entre plantas. Puede comenzar el ataque desde tu posición.")
                    print("→ Es el único fantasma que puede darnos una imagen limpia, sin interferencias y, sin fantasma. Pero que sí cuenta como 'Fantasma 3 estrellas'. Al momento de tomarle una foto desaparecerá. ")
                    print("→ Tiene un parpadeo que casi no te permite verlo durante las cacerías, es casi invisible. Muy dificil de ver.")
                #4
                if fantasma_id == 4:
                    os.system('cls')
                    print("=== POLTERGEIST ===")
                    print("→ Cordura: 50%")
                    print("→ Velocidad: Normal (1.7m/s)")
                    print("→ Tiene mayor probabilidad de lanzar objetos. Además puede lanzarlos mucho más lejos que otros fantasmas.")
                    print("→ En la cacería lanza objetos cada 0,5 segundos.")
                    print("→ Su habilidad especial es que puede lanzar varios objetos a la vez, (prueba de la montaña de objetos) y por cada objeto lanzado reduce un 2 porciento de cordura.")
                #5
                if fantasma_id == 5:
                    os.system('cls')
                    print("=== BANSHEE ===")
                    print("→ Cordura 50% (de su objetivo) 87% promedio si su target tiene 50%")
                    print("→ Velocidad: Normal (1.7m/s)")
                    print("→ Desde el comienzo de la partida fija a 1 objetivo o target. Al cual perseguirá y atacará. A no ser que esté fuera de la casa, en ese caso atacará a cualquiera.")
                    print("→ Su habilidad especial es un grito a través del micrófono parabólico. (Baja probabilidad de hacerlo.)")
                    print("→ Prefiere los eventos o manifestaciones de canto.")
                    print("→ Si muere su obsesión escogerá a otro target.")
                #6
                if fantasma_id == 6:
                    os.system('cls')
                    print("=== JINN ===")
                    print("→ Cordura 50%")
                    print("→ Velocidad: Normal (1.7m/s) sin habiliidad especial.")
                    print("→ Su habilidad especial es que acelera hasta 2.5m/s cuando estás lejos de él, pero solo si el cuadro eléctrico está encendido. No puede utilizar su habilidad con el cuadro eléctrico apagado.")
                    print("→ Nunca apagará el cuadro eléctrico.")
                #7
                if fantasma_id == 7:
                    os.system('cls')
                    print("=== PESADILLA ===")
                    print("→ Cordura 60%")
                    print("→ Velocidad: Normal (1.7m/s)")
                    print("→ Nunca encenderá una luz.")
                    print("→ Puede encender la TV y el PC.")
                    print("→ Si la luz en su habitación está encendida no podrá atacar hasta el 40%% de cordura. Pero si la luz está apagada atacará al 60%%.")
                    print("→ Su habilidad especial es apagar inmediatamente un interruptor que tu enciendas. Puede realizar esta habilidad cada 10 segundos.")
                #8
                if fantasma_id == 8:
                    os.system('cls')
                    print("=== REVENANT ===")
                    print("→ Cordura 50%")
                    print("→ Velocidad:\nSin detectar al jugador: Lento (1m/s)\nDetectando al jugador: Muy Rápido (3m/s)")
                    print("→ La velocidad del revenant no bajara al dejar de ver al jugador, ira rápido hasta el punto donde lo vio por ultima vez y luego disminuirá su velocidad.")
                #9
                if fantasma_id == 9:
                    os.system('cls')
                    print("=== SOMBRA ===")
                    print("→ Cordura: 30%")
                    print("→ Velocidad: Normal (1.7m/s)")
                    print("→ Una de sus pruebas es EMF 5, sin embargo nunca dará EMF 2, 3 o 5 en una interacción si hay alguien en su habitación. Excepto al escribir en el libro o apagar velas.")
                    print("→ Es el único fantasma que aparece en modo sombra al utilizar las posesiones malditas de: Caja de Música, Círculo de Invocación o Mano de Mono.")
                    print("→ Nunca atacara desde la habitación donde este si hay mas de una persona y rara vez dará las pruebas si no hay solo una persona.")
                #10
                if fantasma_id == 10:
                    print("=== DEMONIO ===")
            else:
                print("Código de fantasma no válido. Debe estar entre 1 y 24.")

        else:
            print("Opción no válida. Por favor, elige una opción válida.")
            os.system('cls')


def show_tips():
    print("Mostrando consejos de juego...")
    # Aquí puedes agregar la lógica para mostrar consejos
    pass

root = tk.Tk()
root.title("Phasmophobia Helper Console")

# Crear un campo de texto para las consultas
query_entry = tk.Entry(root)
query_entry.pack()

# Crear un botón para iniciar el temporizador
timer_button = tk.Button(root, text="Iniciar Temporizador", command=start_timer)
timer_button.pack()

root.withdraw()  # Para que la consola esté oculta al inicio

# Detecta la tecla F1 para mostrar/ocultar la consola
keyboard.add_hotkey('F1', toggle_console)

# Menú principal
def menu():
    while True:
        print("Phasmophobia Helper Console")
        print("[1] Consultar información sobre fantasmas.")
        print("[2] Configurar un temporizador.")
        print("[3] Consultar consejos de juego.")
        print("[4] Salir del programa.")

        opc = input("Ingrese una opción --->> ")

        if opc == '1':
            show_ghost_info()
        elif opc == '2':
            start_timer()
        elif opc == '3':
            show_tips()
        elif opc == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción ingresada no es válida.")

# Mantén la aplicación en ejecución
while True:
    sleep(0.1)
    root.update()
    menu()  # Llama al menú para que el usuario pueda interactuar
