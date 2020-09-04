# coding=utf-8

import pygame
import numpy as np

# Inputs: tiempos de cada equipo
while True:
    try:
        tiempo1 = int(input("Tiempo equipo azul: "))
    except ValueError:
        print("Por favor ingrese un valor numérico.")
        continue
    break
while tiempo1 < 0 or tiempo1 > 999:
    print("Por favor ingrese un valor entre 1 y 999 segundos.")
    tiempo1 = int(input("Tiempo equipo azul: "))

while True:
    try:
        tiempo2 = int(input("Tiempo equipo naranja: "))
    except ValueError:
        print("Por favor ingrese un valor numérico.")
        continue
    break
while tiempo2 < 0 or tiempo2 > 999:
    print("Por favor ingrese un valor entre 1 y 999 segundos.")
    tiempo2 = int(input("Tiempo equipo naranja: "))

# Colores a usar
letras_nada = (0, 85, 255)
letras_pasapalabra = (255, 188, 0)
letras_buena = (0, 160, 0)
letras_mala = (160, 0, 0)
orange_team = (255, 128, 0)
blue_team = (0, 0, 153)
white = (255, 255, 255)
black = (0, 0, 0)
team_colors = [blue_team, orange_team]
colors = [letras_nada, letras_pasapalabra, letras_buena, letras_mala]

# Letras del abecedario
abc = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "M", "N",
    "ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y", "Z"]
N = len(abc)


# Objeto Rosco
# Estado de las letras:
# 0 -> vacio
# 1 -> pasapalabra
# 2 -> buena
# 3 -> mala
class Rosco():
    def __init__(self):
        self.letters = np.zeros(N)       # 0, 1, 2 ,3
        self.pasapalabra = np.zeros(N)   # 0, 1
        self.correct = np.zeros(N)       # 0, 1
        self.incorrect = np.zeros(N)     # 0, 1
        self.timing = False              # ¿Se está tomando el tiempo?
        self.no_time = False             # ¿Se acabó el tiempo?
        self.current = 0                 # Letra actual

# Se crean roscos naranja (0) y azul (1) y comienza el equipo naranja
rosco1 = Rosco()
rosco2 = Rosco()
roscos = [rosco1, rosco2]
rosco_actual = 0

# Funciones para operar con roscos
def pasapalabra(rosco):
    while(rosco.letters[rosco.current] >= 2):
        if sum(rosco.incorrect) + sum(rosco.correct) == N:
            break
        if rosco.current == (N-1):
            vuelta_rosco(rosco)
        else:
            rosco.current = rosco.current + 1
    if sum(rosco.incorrect) + sum(rosco.correct) == N:
        return
    if rosco.current == (N-1):
        vuelta_rosco(rosco)
    else:
        rosco.pasapalabra[rosco.current] = 1
        rosco.letters[rosco.current] = 1
        rosco.current = rosco.current + 1
    rosco.timing = False

def correcta(rosco):
    while(rosco.letters[rosco.current] >= 2):
        if sum(rosco.incorrect) + sum(rosco.correct) == N:
            break
        if rosco.current == (N-1):
            vuelta_rosco(rosco)
        else:
            rosco.current = rosco.current + 1
    if sum(rosco.incorrect) + sum(rosco.correct) == N:
        return
    rosco.letters[rosco.current] = 2
    rosco.correct[rosco.current] = 1
    if rosco.current == (N-1):
        vuelta_rosco(rosco)
    else:
        rosco.current = rosco.current + 1


def incorrecta(rosco):
    while(rosco.letters[rosco.current] >= 2):
        if sum(rosco.incorrect) + sum(rosco.correct) == N:
            break
        if rosco.current == (N-1):
            vuelta_rosco(rosco)
        else:
            rosco.current = rosco.current + 1
    if sum(rosco.incorrect) + sum(rosco.correct) == N:
        return
    rosco.letters[rosco.current] = 3
    rosco.incorrect[rosco.current] = 1
    if rosco.current == (N-1):
        vuelta_rosco(rosco)
    else:
        rosco.current = rosco.current + 1
    rosco.timing = False


def vuelta_rosco(rosco):
    rosco.current = 0
    for j in range(N):
        rosco.pasapalabra[j] = 0
        if rosco.correct[j] != 1 and rosco.incorrect[j] != 1:
            rosco.letters[j] = 0

def undo(rosco):
    if rosco.current == 0:
        rosco.current = N-1
        rosco.letters[rosco.current] = 0
        rosco.pasapalabra[rosco.current] = 0
        rosco.correct[rosco.current] = 0
        rosco.incorrect[rosco.current] = 0
    else:
        rosco.current = rosco.current - 1
        rosco.letters[rosco.current] = 0
        rosco.pasapalabra[rosco.current] = 0
        rosco.correct[rosco.current] = 0
        rosco.incorrect[rosco.current] = 0

# Funcion main
def main():

    # Variables globales a usar 
    global roscos
    global rosco_actual
    global tiempo1
    global tiempo2

    # Se inicia pygame
    pygame.init()

    # Fuentes a usar
    font1 = pygame.font.SysFont("comicsansms", 54)
    font2 = pygame.font.SysFont("comicsansms", 32)
    font3 = pygame.font.SysFont("comicsansms", 50)
    font4 = pygame.font.SysFont("comicsansms", 160)
    font5 = pygame.font.SysFont("comicsansms", 100)

    # Tamaño de la ventana
    screen_size = (1000, 1000)

    # Establece el título de la ventana
    pygame.display.set_caption(u'PASAPALABRA: El Rosco')

    # Crea y establece el tamaño de la ventana, y habilita algunas opciones
    DISPLAY = pygame.display.set_mode(screen_size, 0, 32)

    # ¿La aplicación está ejecutándose?
    is_running = True

    # Color de fondo según equipo que está jugando (comienza el equipo naranja)
    background_color = team_colors[rosco_actual]

    # Se inicializa el reloj y los tiempos
    clock = pygame.time.Clock()
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    theta = 0

    # Si la aplicación está ejecutándose
    while is_running:
        
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

                # Tecla C: alterna roscos
                elif event.key == pygame.K_c:
                    roscos[rosco_actual].timing = False
                    if rosco_actual == 0:
                        rosco_actual = 1
                    else:
                        rosco_actual = 0

                # Tecla CTRL izquierda: inicia o detiene el tiempo para el rosco actual
                elif event.key == pygame.K_LCTRL:
                    roscos[rosco_actual].timing = not roscos[rosco_actual].timing

                # Tecla Z: limpia la letra anterior
                elif event.key == pygame.K_z:
                    undo(roscos[rosco_actual])

                # Tecla 1: pasapalabra en la letra actual del rosco actual
                elif event.key == pygame.K_1 and roscos[rosco_actual].no_time == False:
                    pasapalabra(roscos[rosco_actual])

                # Tecla 2: letra actual del rosco actual está correcta
                elif event.key == pygame.K_2 and roscos[rosco_actual].no_time == False:
                    correcta(roscos[rosco_actual])

                # Tecla 3: letra actual del rosco actual está incorrecta
                elif event.key == pygame.K_3 and roscos[rosco_actual].no_time == False:
                    incorrecta(roscos[rosco_actual])

            # Paso del tiempo de cada equipo. Si algún tiempo llega a 0, este se detiene.
            if event.type == pygame.USEREVENT:
                if roscos[rosco_actual].timing and roscos[rosco_actual].no_time == False:
                    if rosco_actual == 0:
                        tiempo1 = tiempo1 - 1
                        if tiempo1 == 0:
                            rosco1.no_time = True
                    else:
                        tiempo2 = tiempo2 - 1
                        if tiempo2 == 0:
                            rosco2.no_time = True

        # Colores de cada letra y el fondo en el instante actual
        frame_colors = roscos[rosco_actual].letters
        background_color = team_colors[rosco_actual]

        # Radios del rosco y de cada letra
        R = 350
        r = 30

        # Se dibujan los círculos y las letras, coloréandolas según corresponde
        phi = -np.pi/2.0
        letras = []
        for k in range(N):
            center = (500 + int(R*np.cos(phi)), 450 + int(R*np.sin(phi)))
            center2 = (500 + int(R*np.cos(phi)) - int(r/2), 450 + int(R*np.sin(phi)) - int(r/2))
            pygame.draw.circle(DISPLAY, white, center, r)
            pygame.draw.circle(DISPLAY, colors[int(frame_colors[k])], center, r-2)
            letras.append(font1.render(abc[k], True, white))
            phi = phi + (2.0*np.pi)/N
            DISPLAY.blit(letras[k], center2)

        # Se dibuja cuadro de puntuación del equipo naranja, y se proporcionan los datos
        pygame.draw.rect(DISPLAY, (0,0,0), (10,10, 200,150))
        pygame.draw.rect(DISPLAY, team_colors[0], (12,12, 196,146))
        DISPLAY.blit(font2.render("Equipo Azul", True, white), (45, 18))
        DISPLAY.blit(font2.render("Buenas:", True, white), (22, 58))
        if sum(roscos[0].correct) < 10:
            DISPLAY.blit(font3.render(str(int(sum(roscos[0].correct))), True, (0, 160, 0)),  (150, 54))
        else:
            DISPLAY.blit(font3.render(str(int(sum(roscos[0].correct))), True, (0, 160, 0)),  (140, 54))
        DISPLAY.blit(font2.render("Malas:", True, white), (22, 93))
        if sum(roscos[0].incorrect) < 10:
            DISPLAY.blit(font3.render(str(int(sum(roscos[0].incorrect))), True, (160, 0, 0)),  (150, 89))
        else:
            DISPLAY.blit(font3.render(str(int(sum(roscos[0].incorrect))), True, (160, 0, 0)),  (140, 89))
        DISPLAY.blit(font2.render("Tiempo:", True, white), (22, 128))
        if tiempo1 < 10:
            DISPLAY.blit(font3.render(str(tiempo1), True, white), (150, 123))
        elif tiempo1 < 100:
            DISPLAY.blit(font3.render(str(tiempo1), True, white), (140, 123))
        else:
            DISPLAY.blit(font3.render(str(tiempo1), True, white), (130, 123))

        # Se dibuja cuadro de puntuación del equipo azul, y se proporcionan los datos
        pygame.draw.rect(DISPLAY, (0,0,0), (790,10, 200,150))
        pygame.draw.rect(DISPLAY, team_colors[1], (792,12, 196,146))
        DISPLAY.blit(font2.render("Equipo Naranja", True, white), (805, 18))
        DISPLAY.blit(font2.render("Buenas:", True, white), (802, 58))
        if sum(roscos[1].correct) < 10:
            DISPLAY.blit(font3.render(str(int(sum(roscos[1].correct))), True, (0, 160, 0)),  (920, 54))
        else:
            DISPLAY.blit(font3.render(str(int(sum(roscos[1].correct))), True, (0, 160, 0)),  (910, 54))
        DISPLAY.blit(font2.render("Malas:", True, white), (802, 93))
        if sum(roscos[1].incorrect) < 10:
            DISPLAY.blit(font3.render(str(int(sum(roscos[1].incorrect))), True, (160, 0, 0)),  (920, 89))
        else:
            DISPLAY.blit(font3.render(str(int(sum(roscos[1].incorrect))), True, (160, 0, 0)),  (910, 89))
        DISPLAY.blit(font2.render("Tiempo:", True, white), (802, 128))
        if tiempo2 < 10:
            DISPLAY.blit(font3.render(str(tiempo2), True, white), (920, 123))
        elif tiempo2 < 100:
            DISPLAY.blit(font3.render(str(tiempo2), True, white), (910, 123))
        else:
            DISPLAY.blit(font3.render(str(tiempo2), True, white), (900, 123))

        # Se dibuja círculo que indica las correctas del equipo actual, y se proporciona la información
        pygame.draw.circle(DISPLAY, white, (880, 790), 100)
        pygame.draw.circle(DISPLAY, (156,156,156), (880, 790), 98)
        if sum(roscos[rosco_actual].correct) < 10:
            DISPLAY.blit(font4.render(str(int(sum(roscos[rosco_actual].correct))), True, (0,100,0)), (850, 740))
        else:
            DISPLAY.blit(font4.render(str(int(sum(roscos[rosco_actual].correct))), True, (0,100,0)), (820, 740))

        # Se dibuja círculo que indica el tiempo restante del equipo actual, y se proporciona la información
        pygame.draw.circle(DISPLAY, white, (120, 790), 100)
        pygame.draw.circle(DISPLAY, (156,156,156), (120, 790), 98)
        if rosco_actual == 0:
            if tiempo1 < 10:
                DISPLAY.blit(font4.render(str(tiempo1), True, white), (85, 740))
            elif tiempo1 < 100:
                DISPLAY.blit(font4.render(str(tiempo1), True, white), (55, 740))
            else:
                DISPLAY.blit(font4.render(str(tiempo1), True, white), (25, 740))
        else:
            if tiempo2 < 10:
                DISPLAY.blit(font4.render(str(tiempo2), True, white), (85, 740))
            elif tiempo2 < 100:
                DISPLAY.blit(font4.render(str(tiempo2), True, white), (55, 740))
            else:
                DISPLAY.blit(font4.render(str(tiempo2), True, white), (25, 740))

        # Se dibuja círculo pequeño que indica si el tiempo está corriendo o no
        if roscos[rosco_actual].timing:
            theta = theta + (2.0*np.pi)/700
        pygame.draw.circle(DISPLAY, black, (int(120 + 100*np.cos(theta)), int(790 + 100*np.sin(theta))), 10)
        pygame.draw.circle(DISPLAY, white, (int(120 + 100*np.cos(theta)), int(790 + 100*np.sin(theta))), 9)


        # Se chequean las condiciones de victoria o empate
        # -1 : Ninguno aun
        # 0  : Equipo naranja
        # 1  : Equipo azul
        # 2  : Empate
        winner = -1
        if sum(rosco1.correct) > N - sum(rosco2.incorrect):
            winner = 0
        if sum(rosco2.correct) > N - sum(rosco1.incorrect):
            winner = 1
        if sum(rosco1.correct) > sum(rosco2.correct) and rosco2.no_time:
            winner = 0
        if sum(rosco2.correct) > sum(rosco1.correct) and rosco1.no_time:
            winner = 1
        if min(rosco1.letters) > 1 and min(rosco2.letters) > 1:
            if sum(rosco1.correct) == sum(rosco2.correct):
                winner = 2
        if rosco1.no_time and rosco2.no_time and sum(rosco1.correct) == sum(rosco2.correct):
            if sum(rosco1.incorrect) > sum(rosco2.incorrect):
                winner = 1
            elif sum(rosco1.incorrect) < sum(rosco2.incorrect):
                winner = 0
            else:
                winner = 2

        # En caso de haber algún ganador (o empate), se anuncia
        if winner != -1:
            if winner == 0:
                DISPLAY.blit(font4.render("VICTORIA", True, white), (240, 350))
                DISPLAY.blit(font5.render("Equipo Naranja", True, white), (250, 500))
            elif winner == 1:
                DISPLAY.blit(font4.render("VICTORIA", True, white), (240, 350))
                DISPLAY.blit(font5.render("Equipo Azul", True, white), (300, 500))
            else:
                DISPLAY.blit(font4.render("EMPATE", True, white), (255, 400))

        # Se actualizan el cuadro
        pygame.display.flip()

        # Se limita el programa a 60 FPS
        clock.tick(60)

    # Se finaliza Pygame
    pygame.quit()

# Se ejecuta función main
if __name__ == '__main__':
    main()
