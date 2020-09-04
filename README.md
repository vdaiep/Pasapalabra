PASAPALABRA
===========

Extensión visual casera del juego de mesa PASAPALABRA, de Ansaldo y CHV.

Este repositorio contiene 3 programas escritos en Python, para facilitar el desarrollo grupal del juego. El concepto es que el moderador del juego ejecute y manipule estos programas en una pantalla compartida, para permitir un desarrollo más fluido de PALABRAS CRUZADAS, EL AHORCADO y EL ROSCO.


PALABRAS CRUZADAS
-----------------

El programa se ejecuta con la siguiente línea en la terminal:

    python3 cruzadas.py
    
Se solicitarán 8 palabras para cada equipo, las cuales deben proporcionarse separadas por un espacio según se indique en la tarjeta del juego. No se pueden ingresar tildes.

El moderador ahora puede compartir pantalla y desarrollar el juego. Los controles son los siguientes:

* ESPACIO:  Inicia o detiene el tiempo.
* 1-8:      Alterna la palabra en cuestión (1-8) entre respondida correctamente o no (y asigna puntaje).
* C:        Una vez que el tiempo llega a 0, alterna al siguiente equipo o a la pantalla de puntajes finales.
* ESC:      Cierra el programa.

El moderador debe ir leyendo las definiciones en orden, marcando las que se respondieron correctamente (con las teclas 1-8) y saltándoselas en la siguiente vuelta.


EL AHORCADO
-----------

El programa se ejecuta con la siguiente línea en la terminal:

    python3 ahorcado.py
    
Se solicitarán 9 palabras para cada equipo, las cuales deben proporcionarse según se indique en la tarjeta del juego. No se pueden ingresar tildes.

El moderador ahora puede compartir pantalla y desarrollar el juego. Los controles son los siguientes:

* ESPACIO:  Inicia o detiene el tiempo.
* LETRAS:   Cada tecla de letra verifica si dicha letra está o no en la palabra actual. En caso de estar, la marca todas las veces necesarias, de no estar, queda marcada como incorrecta. Una vez que se marcan todas las letras de la palabra, o se agotan las 5 oportunidades de equivocarse, el programa muestra la palabra y pasa a la siguiente, asignando puntaje como corresponda.
* 1:        Marca la palabra como correcta y pasa a la siguiente.
* 2:        Marca la palabra como incorrecta y pasa a la siguiente.
* ESC:      Cierra el programa.

El moderador debe ir marcando las letras que los jugadores indiquen, y en caso de que se intente adivinar la palabra completa, usar las teclas 1 y 2 según corresponda. Una vez que se acaben las 9 palabras o el tiempo de cada equipo, se pasa al equipo siguiente o a la pantalla de puntajes finales.


EL ROSCO
--------

El programa se ejecuta con la siguiente línea en la terminal:

    python3 rosco.py

Se solicitarán los tiempos en segundos correspondientes a cada equipo. El moderador ahora puede compartir pantalla y desarrollar el juego. Los controles son los siguientes:

* CTRL IZQ:  Inicia o detiene el tiempo.
* 1:         Indica la palabra actual como "PASAPALABRA" y detiene el tiempo.
* 2:         Indica la palabra actual como correcta.
* 3:         Indica la palabra actual como incorrecta y detiene el tiempo.
* C:         Alterna entre equipos.
* Z:         Botón de deshacer, limpia la letra anterior, y esta pasa a ser la letra actual.
* ESC:       Cierra el programa.

El moderador debe ir leyendo las definiciones de cada equipo, y marcando las letras según las respuestas de los jugadores. Para más información respecto a las reglas del juego, consultar las instrucciones de este. Una vez que se alcance la condición de victoria para alguno de los equipos, se indicará en pantalla el ganador, pero se podrá seguir jugando hasta que el tiempo de cada equipo se acabe.









