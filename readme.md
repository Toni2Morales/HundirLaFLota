# Hundir la flota

## En este proyecto he recreado el clásico juego de Hundir la Flota programándolo completamente en Python.

### En este proyecto se puede apreciar:
* La programación orientada a objetos
* El uso de funciones
* El uso de módulos
* El uso de librerías
* Uso de bucles
* Uso de condicionales
* Uso de list comprehension

## Librerías
* Numpy
* OS
* Time
* keyboard

## Clases

### Para este proyecto se han creado las siguientes clases con sus respectuvos métodos:

* Tablero
    * mostrar(Imprime el tablero por pantalla)
    * limpiar(Quita todos los barcos del tablero)
* Barco
    * comprobacion (Comprueba que ningún barco se coloque encima de otro)
* Jugador
    * anadir_barcos (Añade los barcos a la lista de barcos del jugador)
    * colocar_barcos (Añade los barcos de cada jugador a su respectivo tablero)

### El fichero "main.py" es el ejecutable principal para procesar todo el código del juego, en este archivo se importa el modulo "clases.py" que contiene las clases de los objetos que se van a declarar para poder realizar el juego.

### Este es un juego para una persona en el que se juega contra la máquina("no hay opciones de selección de dificultad pero se podria añadir más adelante"), cada uno tiene un tablero de 10x10 en el que se colocarán 4 barcos de 1 de longitud, 3 barcos de 2 de longitud, 2 barcos de 3 de longitud y 1 barco de 4 de longitud y tendrás que intentar derribar los barcos enemigos

## Funcionamiento del juego:

### En este juego se inicia eligiendo una coordenada Y y una coordenada X(desde 0 hasta 9), luego se te pedirá una dirección para orientar el barco(recuerda que son 10 barcos en total).

### Como se puede ver en la imagen de abajo, la tecla para saltarse el tiempo de espera es la "q".

![Imagen1](/HundirLaFLota/Imagenes/1.PNG)

### Después de Haber seleccionado tus barcos llega la hora de empezar a jugar. Ya que este juego es hecho a modo de demostracion los datos del tablero adversario se muestran en pantalla para terminar el juego facilmente. Cada vez que se acierta se vuelve a disparar( Esto ocurre tanto para el jugador como par la máquina). Hay simbolos especiales que muestran visualmente cuando no se ha acertado a un barco, cuando se le ha acertado y cuando se le ha Hundido.

![Imagen1](/HundirLaFLota/Imagenes/2.PNG)

### Al final de la partida se indica el ganador y el perdedor junto a sus tableros y los ataques que han hecho.

![Imagen1](/HundirLaFLota/Imagenes/3.PNG)



