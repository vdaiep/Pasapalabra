# coding=utf-8

import pygame
import numpy as np
import random
import time

# Colores a usar
black = (0, 0, 0)
white = (255, 255, 255)
gray = (156, 156, 156)
green = (0, 120, 0)
orange_team = (255, 128, 0)
blue_team = (0, 0, 153)
team_colors = [blue_team, orange_team]

# Constantes del juego
N = 8           # Número de palabras por equipo
tiempo = 60     # Tiempo en segundos por equipo (máximo 99)
keys = [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8]
random.seed(time.time)

# Se indican palabras a usar al comenzar la aplicación
words1 = []
words2 = []
for k in range(N):
    word = input("Palabra azul {}: ".format(k+1))
    true_word = word.upper().split(" ")
    while (len(word) < 2 or len(word) > 16) or (len(true_word) != 2):
        print("Las palabras deben tener entre 2 y 16 caracteres, y estar separadas por un espacio.")
        word = input("Palabra azul {}: ".format(k+1))
        true_word = word.upper().split(" ")
    words1.append(true_word)
for k in range(N):
    word = input("Palabra naranja {}: ".format(k+1))
    true_word = word.upper().split(" ")
    while (len(word) < 2 or len(word) > 16) or (len(true_word) != 2):
        print("Las palabras deben tener entre 2 y 16 caracteres, y estar separadas por un espacio.")
        word = input("Palabra naranja {}: ".format(k+1))
        true_word = word.upper().split(" ")
    words2.append(true_word)
words = [words1, words2]

def main():

    # Variables a usar
    numbers1 = np.arange(8)
    numbers2 = np.arange(8)
    puntajes = np.zeros(2)              # Marcador de puntajes
    current_team = 0                    # Comienza el equipo naranja
    random.shuffle(numbers1)            # Se mezclan las palabras de manera aleatoria
    random.shuffle(numbers2)            # Se mezclan las palabras de manera aleatoria
    mark = np.zeros(N)                  # Indicador de cada palabra (¿correcta o no?)
    current_time = tiempo               # Tiempo del equipo inicial

    # Se inicia pygame
    pygame.init()

    # Fuentes a usar
    font1 = pygame.font.SysFont("comicsansms", 32)
    font2 = pygame.font.SysFont("comicsansms", 60)
    font3 = pygame.font.SysFont("comicsansms", 160)
    font4 = pygame.font.SysFont("comicsansms", 120)

    # Tamaño de la ventana
    screen_size = (1000, 1000)

    # Establece el título de la ventana
    pygame.display.set_caption(u'PASAPALABRA: Palabras Cruzadas')

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
    timing = False          # ¿Se está tomando el tiempo?
    next_team = False       # ¿Cambio de equipo?
    done = False            # ¿Terminaron ambos equipos?

    while is_running:

        # Se alterna entre equipos
        if next_team:
            if current_team == 0:
                current_team = 1
                current_time = tiempo
                background_color = team_colors[current_team]
                random.shuffle(numbers1)
                random.shuffle(numbers2)
                mark = np.zeros(N)
                next_team = False
                timing = False
            else:
                done = True
                next_team = False

        if done:
            if puntajes[0] > puntajes[1]:
                background_color = team_colors[0]
            elif puntajes[0] < puntajes[1]:
                background_color = team_colors[1]
            else:
                background_color = gray

        # Se colorea el fondo según equipo que está jugando
        DISPLAY.fill(background_color)

        # Se dibuja cuadro de puntuación del equipo naranja, y se proporcionan los datos
        pygame.draw.rect(DISPLAY, black, (10,10, 200,85))
        pygame.draw.rect(DISPLAY, team_colors[0], (12,12, 196,81))
        DISPLAY.blit(font1.render("Equipo Azul", True, white), (45, 18))
        DISPLAY.blit(font1.render("Buenas:", True, white), (22, 58))
        DISPLAY.blit(font2.render(str(int(puntajes[0])), True, green),  (150, 54))

        # Se dibuja cuadro de puntuación del equipo azul, y se proporcionan los datos
        pygame.draw.rect(DISPLAY, black, (790,10, 200,85))
        pygame.draw.rect(DISPLAY, team_colors[1], (792,12, 196,81))
        DISPLAY.blit(font1.render("Equipo Naranja", True, white), (805, 18))
        DISPLAY.blit(font1.render("Buenas:", True, white), (802, 58))
        DISPLAY.blit(font2.render(str(int(puntajes[1])), True, green),  (920, 54))

        # Pantalla final (ambos equipos ya terminaron)
        if done:
            if puntajes[0] > puntajes[1]:
                DISPLAY.blit(font4.render("GANADOR", True, white), (280, 330))
                DISPLAY.blit(font4.render("Equipo Azul", True, white), (250, 530))
            elif puntajes[0] < puntajes[1]:
                DISPLAY.blit(font4.render("GANADOR", True, white), (280, 330))
                DISPLAY.blit(font4.render("Equipo Naranja", True, white), (200, 530))
            else:
                DISPLAY.blit(font4.render("EMPATE", True, white), (330, 430))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    is_running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    is_running = False

            # Se itera indefinidamente hasta que se cierre el programa
            pygame.display.flip()
            continue
    
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

                # Tecla C: cambio de equipo en caso de que el equipo actual haya terminado
                if event.key == pygame.K_c:
                    if current_time == 0 or puntajes[current_team] == 8:
                        next_team = True

                # Teclas 1-8: la palabra 1-8 se identificó correctamente
                if event.key in keys:
                    q = int(event.unicode)
                    if current_time > 0:
                        if mark[q-1] == 1:
                            mark[q-1] = 0
                            puntajes[current_team] = puntajes[current_team] - 1
                        else:
                            mark[q-1] = 1
                            puntajes[current_team] = puntajes[current_team] + 1
                

            # Paso del tiempo de cada equipo
            if event.type == pygame.USEREVENT:
                if timing:
                    if current_time > 0:
                        current_time = current_time - 1

        # Se dibujan (o no) los rectángulos con las palabras (lado izquierdo)
        pos_x = 30
        pos_y_0 = 180
        for j in range(N):
            i = numbers1[j]
            pos_y = pos_y_0 + i*90
            if mark[j] == 0:
                pygame.draw.rect(DISPLAY, white, (pos_x, pos_y, 280, 65))
                pygame.draw.rect(DISPLAY, gray, (pos_x+1, pos_y+1, 278, 63))
                word = words[current_team][j][0]
                L = len(word)
                DISPLAY.blit(font2.render(word, True, white), (pos_x+10+(9-L)*13, pos_y+15))
            else:
                pygame.draw.rect(DISPLAY, team_colors[current_team], (pos_x, pos_y, 280, 65))

        # Se dibujan (o no) los rectángulos con las palabras (lado derecho)
        for j in range(N):
            i = numbers2[j]
            pos_y = pos_y_0 + i*90
            if mark[j] == 0:
                pygame.draw.rect(DISPLAY, white, (pos_x+660, pos_y, 280, 65))
                pygame.draw.rect(DISPLAY, gray, (pos_x+660+1, pos_y+1, 278, 63))
                word = words[current_team][j][1]
                L = len(word)
                DISPLAY.blit(font2.render(word, True, white), (pos_x+660+10+(9-L)*13, pos_y+15))
            else:
                pygame.draw.rect(DISPLAY, team_colors[current_team], (pos_x+660, pos_y, 280, 65))

        # Se dibuja círculo que indica el tiempo restante del equipo actual, y se proporciona la información
        pygame.draw.circle(DISPLAY, white, (500, 120), 100)
        pygame.draw.circle(DISPLAY, gray, (500, 120), 98)
        if current_time > 9:
            DISPLAY.blit(font3.render(str(current_time), True, white), (440, 70))
        else:
            DISPLAY.blit(font3.render(str(current_time), True, white), (470, 70))

        # Se actualizan el cuadro
        pygame.display.flip()

        # Se limita el programa a 60 FPS
        clock.tick(60)

    # Se finaliza Pygame
    pygame.quit()

# Se ejecuta función main
if __name__ == '__main__':
    main()
