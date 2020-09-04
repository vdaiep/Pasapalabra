# coding=utf-8

import pygame
import numpy as np

# Letras del abecedario
abc = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
    "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Colores a usar
black = (0, 0, 0)
white = (255, 255, 255)
gray = (156, 156, 156)
orange_team = (255, 128, 0)
blue_team = (0, 0, 153)
team_colors = [blue_team, orange_team]

# Constantes del juego
N = 9           # Número de palabras por equipo
tiempo = 90     # Tiempo en segundos por equipo (máximo 99)

# Se indican palabras a usar al comenzar la aplicación
words1 = []
words2 = []
for k in range(N):
    word = input("Palabra azul {}: ".format(k+1))
    while len(word) < 2 or len(word) > 16:
        print("Las palabras deben tener entre 2 y 16 caracteres")
        word = input("Palabra azul {}: ".format(k+1))
    words1.append(word.upper())
for k in range(N):
    word = input("Palabra naranja {}: ".format(k+1))
    while len(word) < 2 or len(word) > 16:
        print("Las palabras deben tener entre 2 y 16 caracteres")
        word = input("Palabra naranja {}: ".format(k+1))
    words2.append(word.upper())

# Funcion main
def main():

    # Variables a usar
    puntajes = np.zeros((2,2))   # Puntuaciones
    words = words1               # Palabras a usar por el primer equipo
    current_team = 0             # Comienza el equipo naranja
    current_word = 0             # Se comienza desde la primera palabra
    current_time = tiempo        # Tiempo del equipo naranja
    letras_dichas = []           # Letras que ya se han dicho
    incorrectas = []             # Letras incorrectas que ya se han dicho
    next_word = False            # ¿Se pasa a la siguiente palabra?

    # Se inicia pygame
    pygame.init()

    # Fuentes a usar
    font2 = pygame.font.SysFont("comicsansms", 32)
    font3 = pygame.font.SysFont("comicsansms", 50)
    font4 = pygame.font.SysFont("comicsansms", 160)
    font5 = pygame.font.SysFont("comicsansms", 120)

    # Tamaño de la ventana
    screen_size = (1000, 1000)

    # Establece el título de la ventana
    pygame.display.set_caption(u'PASAPALABRA: El Ahorcado')

    # Crea y establece el tamaño de la ventana, y habilita algunas opciones
    DISPLAY = pygame.display.set_mode(screen_size, 0, 32)

    # ¿La aplicación está ejecutándose?
    is_running = True

    # Color de fondo según equipo que está jugando
    background_color = team_colors[current_team]

    # Se inicializa el reloj y los tiempos
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 1000)

    # Condiciones actuales
    timing = False      # ¿Se está tomando el tiempo?
    correct = False     # ¿La palabra actual se identificó correctamente?
    incorrect = False   # ¿La palabra actual se identificó incorrectamente?
    done = False        # ¿Terminaron ambos equipos?

    # Si la aplicación está ejecutándose
    while is_running:

        # Se alterna entre equipos
        # Termina el equipo naranja y se reinician las variables
        if current_team == 0 and (current_word == 9 or current_time == 0):
            current_team = 1
            words = words2
            current_time = tiempo
            current_word = 0
            letras_dichas = []
            incorrectas = []
            background_color = team_colors[1]
            timing = False
        # Termina el equipo azul y se pasa a la pantalla final
        if current_team == 1 and (current_word == 9 or current_time == 0):
            done = True

        # Pantalla final cuando ambos equipos han terminado
        if done:
            if puntajes[0, 0] > puntajes[1, 0]:
                background_color = team_colors[0]
                DISPLAY.fill(background_color)
                DISPLAY.blit(font5.render("GANADOR", True, white), (280, 330))
                DISPLAY.blit(font5.render("Equipo Azul", True, white), (250, 530))
            elif puntajes[0, 0] < puntajes[1, 0]:
                background_color = team_colors[1]
                DISPLAY.fill(background_color)
                DISPLAY.blit(font5.render("GANADOR", True, white), (280, 330))
                DISPLAY.blit(font5.render("Equipo Naranja", True, white), (200, 530))
            else:
                background_color = gray
                DISPLAY.fill(background_color)
                DISPLAY.blit(font5.render("EMPATE", True, white), (330, 430))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    is_running = False

            # Se dibuja círculo que indica la puntuación final del equipo azul
            pygame.draw.circle(DISPLAY, white, (120, 790), 100)
            pygame.draw.circle(DISPLAY, team_colors[0], (120, 790), 98)
            DISPLAY.blit(font4.render(str(int(puntajes[0, 0])), True, (0,100,0)), (90, 740))

            # Se dibuja círculo que indica la puntuación final del equipo naranja
            pygame.draw.circle(DISPLAY, white, (880, 790), 100)
            pygame.draw.circle(DISPLAY, team_colors[1], (880, 790), 98)
            DISPLAY.blit(font4.render(str(int(puntajes[1, 0])), True, (0,100,0)), (850, 740))

            # Se itera indefinidamente hasta que se cierre el programa
            pygame.display.flip()
            continue

        # Se colorea el fondo según equipo que está jugando
        DISPLAY.fill(background_color)
    
        # Obtiene los eventos de la cola de eventos
        for event in pygame.event.get():

            # Si se presiona el botón 'cerrar' de la ventana, se detiene la aplicación
            if event.type == pygame.QUIT:
                is_running = False

            # Si se aprieta alguna tecla
            if event.type == pygame.KEYDOWN:
                
                # Tecla ESC: se detiene la aplicación
                if event.key == pygame.K_ESCAPE:
                    is_running = False

                # Tecla SPACE: se activa o desactiva el tiempo
                if event.key == pygame.K_SPACE:
                    timing = not timing

                # Tecla 1: la palabra actual se identificó correctamente
                if event.key == pygame.K_1:
                    correct = True
                
                # Tecla 2: la palabra actual se identificó incorrectamente
                if event.key == pygame.K_2:
                    incorrect = True

                # Teclas de letra: se aplica la letra en cuestión
                if event.unicode.upper() in abc:
                    letras_dichas.append(event.unicode.upper())
                    if (not (letras_dichas[-1] in words[current_word])):
                        if not (letras_dichas[-1] in incorrectas):
                            incorrectas.append(letras_dichas[-1])

            # Paso del tiempo de cada equipo
            if event.type == pygame.USEREVENT:
                if timing:
                    current_time = current_time - 1

        # Se dibuja cuadro de puntuación del equipo azul, y se proporcionan los datos
        pygame.draw.rect(DISPLAY, (0,0,0), (10,10, 200,115))
        pygame.draw.rect(DISPLAY, team_colors[0], (12,12, 196,111))
        DISPLAY.blit(font2.render("Equipo Azul", True, white), (45, 18))
        DISPLAY.blit(font2.render("Buenas:", True, white), (22, 58))
        DISPLAY.blit(font3.render(str(int(puntajes[0, 0])), True, (0, 160, 0)),  (150, 54))
        DISPLAY.blit(font2.render("Malas:", True, white), (22, 93))
        DISPLAY.blit(font3.render(str(int(puntajes[0, 1])), True, (160, 0, 0)),  (150, 89))

        # Se dibuja cuadro de puntuación del equipo naranja, y se proporcionan los datos
        pygame.draw.rect(DISPLAY, (0,0,0), (790,10, 200,115))
        pygame.draw.rect(DISPLAY, team_colors[1], (792,12, 196,111))
        DISPLAY.blit(font2.render("Equipo Naranja", True, white), (805, 18))
        DISPLAY.blit(font2.render("Buenas:", True, white), (802, 58))
        DISPLAY.blit(font3.render(str(int(puntajes[1, 0])), True, (0, 160, 0)),  (920, 54))
        DISPLAY.blit(font2.render("Malas:", True, white), (802, 93))
        DISPLAY.blit(font3.render(str(int(puntajes[1, 1])), True, (160, 0, 0)),  (920, 89))

        # Se dibuja círculo que indica las correctas del equipo actual, y se proporciona la información
        pygame.draw.circle(DISPLAY, white, (880, 790), 100)
        pygame.draw.circle(DISPLAY, gray, (880, 790), 98)
        DISPLAY.blit(font4.render(str(int(puntajes[current_team, 0])), True, (0,100,0)), (850, 740))

        # Se dibuja círculo que indica el tiempo restante del equipo actual, y se proporciona la información
        pygame.draw.circle(DISPLAY, white, (650, 790), 100)
        pygame.draw.circle(DISPLAY, gray, (650, 790), 98)
        if current_time > 9:
            DISPLAY.blit(font4.render(str(current_time), True, white), (585, 740))
        else:
            DISPLAY.blit(font4.render(str(current_time), True, white), (620, 740))

        # Se indican las letras incorrectas
        for i in range(len(incorrectas)):
            DISPLAY.blit(font3.render(incorrectas[i] , True, white), (100, 600+i*50))

        # Se verifica si se han adivinado todas las letras
        next_word = True
        for letra in words[current_word]:
            if not (letra in letras_dichas):
                next_word = False
                break
            else:
                pass
        
        # Se verifica si se han cometido 5 errores
        if len(incorrectas) == 5:
            next_word = True

        # Se verifica si la palabra ha sido identificada correcta o incorrectamente
        if correct or incorrect:
            next_word = True

        # Se dibujan las letras identificadas y no identificadas de cada palabra
        palabra = words[current_word]
        n = len(palabra)
        l = 25 - n
        L = 900/n
        # Si la palabra se ha identificado, se dibujan todas las letras y se pasa a la siguiente
        if next_word:
            for i in range(n):
                q = 0
                letra = palabra[i]
                if letra == "I":
                    q = 20
                if n < 8:
                    DISPLAY.blit(font5.render(letra, True, white), (int(120+i*L+q), 430))
                elif n < 12:
                    DISPLAY.blit(font5.render(letra, True, white), (int(60+i*L+q), 430))
                else:
                    DISPLAY.blit(font5.render(letra, True, white), (int(40+i*L+q), 430))
            if len(incorrectas) == 5 or incorrect:
                puntajes[current_team, 1] = puntajes[current_team, 1] + 1
            else:
                puntajes[current_team, 0] = puntajes[current_team, 0] + 1
            current_word = current_word + 1
            letras_dichas = []
            incorrectas = []
            correct = False
            incorrect = False
        # Si la palabra no se ha identificado, se dibujan las letras que sí, y líneas en aquellas letras que no
        else:
            for i in range(n):
                q = 0
                if palabra[i] in letras_dichas:
                    if palabra[i] == "I":
                        q = 20
                    if n < 8:
                        DISPLAY.blit(font5.render(palabra[i], True, white), (int(120+i*L+q), 430))
                    elif n < 12:
                        DISPLAY.blit(font5.render(palabra[i], True, white), (int(60+i*L+q), 430))
                    else:
                        DISPLAY.blit(font5.render(palabra[i], True, white), (int(40+i*L+q), 430))
                else:
                    pygame.draw.rect(DISPLAY, white, (int(50 + i*L), 500, int(L-l), 5))


        # Se actualizan el cuadro
        pygame.display.flip()
        if next_word:
            pygame.time.delay(750)

        # Se limita el programa a 60 FPS
        clock.tick(60)

    # Se finaliza Pygame
    pygame.quit()

# Se ejecuta función main
if __name__ == '__main__':
    main()
