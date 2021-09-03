# Parabolic Shot
Parabolic shot es un juego que simula el lanzamiento de una bala de cañon que debe impactar contra un objetivo, este juego fue diseñado para la enseñanza de la física y surgió como un proyecto de la asignatura Programación e Introducción a los Métodos Numéricos en marzo de 2021. El jugador en cada uno de los diez niveles debe calcular las condiciones de lanzamiento teniendo en cuenta la posición del objetivo, los obstáculos que pueden surgir, la gravedad del planeta y las condiciones de la atmosfera. Para superar todos los niveles es necesario tener conocimientos de mecánica newtoniana y ecuaciones diferenciales.
![](https://github.com/debernall/Proyecto_Programacion/blob/073d4db7e99c910df98961efb65e4c2b750a62d7/img_wiki/2.png)

***
# Antecedentes
En el marco de la asignatura Programación e Introducción a los Métodos Numéricos orientada por el docente Ricardo Amezquita en la Universidad Nacional de Colombia en el semestre 2021-A, los estudiantes Brian Santiago Vasquez Marin, Jeisson Andrés Abril Masmelas, Daniel Eduardo Bernal Lozano, Nelson Andres Rodriguez Mora y Sebastian Augusto Ojeda Franco desarrollamos el proyecto Parabolic Shot. El objetivo de este proyecto consiste en fomentar en los estudiantes de educación media, superior y en general de cualquier persona interesada el conocimiento de la física a partir de la simulación de un disparo de bala de cañon bajo diferentes condiciones.

***
# Instalación
Para sistemas operativos windows descargue una copia del repositorio de Parabolic Shot empleando el siguiente enlace:

 https://github.com/debernall/Proyecto_Programacion/archive/refs/heads/main.zip

Descomprima el archivo descargado y a continuación presione doble click sobre el archivo:
 
 proyecto.exe

Ahora podrá jugar Parabolic Shot.

***
# Instrucciones de juego
## Menú principal de inicio
![](https://github.com/debernall/Proyecto_Programacion/blob/073d4db7e99c910df98961efb65e4c2b750a62d7/img_wiki/1.png)

Esta interfaz gráfica permite al usuario acceder al primer nivel del juego por medio del botón JUGAR. Adicionalmente puede acceder a las instrucciones de juego por medio del botón INSTRUCCIONES y salir del juego usando el botón SALIR. El jugador puede en cualquier momento salir de presionando la tecla escape o cerrando directamente la ventana del juego.

## Menú de gameover
![](https://github.com/debernall/Proyecto_Programacion/blob/d099d11ed6aeae7933228df15506afeba38a0bc9/img_wiki/3.png)
Este submenú permite al jugador acceder a una nueva partida desde el primer nivel presionando el botón VOLVER A JUGAR, volver al menú principal por medio del botón VOLVER A INICIO, ver los créditos o salir del juego. Esta pantalla muestra información acerca del nivel máximo alcanzado por el jugador y el puntaje logrado. Es posible acceder a este menú desde el juego presionando la tecla escape mientras se juega o finalizando todos los niveles. 

## Parabolic Shot
![](https://github.com/debernall/Proyecto_Programacion/blob/32c4cb352484fcbed075ee1bea9935d82be885b0/img_wiki/6.png)

La interfaz gráfica del juego ofrece un conjunto de elementos que permite tanto de manera analítica como intuitiva acertar en el objetivo. En la parte superior de la pantalla se muestra información acerca de el ángulo en grados del lanzamiento de la bala, la velocidad inicial de lanzamiento (m/s), la posición del objetivo (m) y la gravedad del lugar donde se realiza el tiro. Los primeros niveles son llevados a cabo en el vacio por tanto no aparecen efectos debidos a fuerzas de fricción con la atmósfera; sin embargo en los últimos niveles una nueva variable llamada coeficiente de arrastre proporciona información acerca del efecto que tiene la atmósfera sobre el desplazamiento de la bala. Esta última variable aparecerá en la parte inferior derecha de la pantalla. 

Un minimapa a escala se muestra en la parte inferior derecha, este minimapa da una pequeña visual al jugador sobre el desarrollo del juego. Es posible que el jugador requiera en muchas ocasiones usar dicho minimapa para evitar chocar la bala contra los diferentes obstáculos que aparecen en los mundos.

Bajo los cuadros de información de la parte superior el jugador podrá encontrar el nivel que se encuentra jugando así como tambien el puntaje acumulado a lo largo de la partida. Es importante que elija el momento adecuado de su lanzamiento debido a que es probable que impacte en algun momento con satélites o robots exploradores del espacio.

### Controles
![](https://github.com/debernall/Proyecto_Programacion/blob/32c4cb352484fcbed075ee1bea9935d82be885b0/img/teclas_inst.png)

Use las teclas subir y bajar para incrementar o disminuir la velocidad inicial de lanzamiento de la bala. La tecla de desplazamiento izquierdo le permitirá aumentar el ángulo de lanzamiento de la bala mientras que la tecla derecha le permitirá disminuir dicho ángulo medido desde el plano horizontal al cañón.

![](https://github.com/debernall/Proyecto_Programacion/blob/32c4cb352484fcbed075ee1bea9935d82be885b0/img/r.png)

En algunas ocasiones le será necesario mejorar la precisión de su lanzamiento por tanto puede acceder por medio de la tecla R a un ajuste fino de las condiciones iniciales. Para revertir el ajuste fino presione la tecla T, con lo cual podrá incrementar velocidad y angulo de lanzamiento en una unidad.

La tecla ESPACIO le permitirá realizar el lanzamiento de la bala. Si logra acertar con el objetivo o no, se le permitirá repetir el nivel presionando la tecla S o avanzar al siguiente nivel presionando la tecla A. Podrá viajar a los diferentes mundos aunque no logré acertar con el objetivo, sin embargo recuerde que no obtendrá puntos hasta acertar con los diferentes objetivos. Es importante tener en cuenta que si acierta con el objetivo y decide repetir dicho nivel, entonces perderá el punto logrado en dicho nivel.

Para efectos de demostración le podría ser util la tecla N, esta le permitirá previo al lanzamiento perder el nivel y con esto avanzar al siguiente sin necesidad de realizar lanzamientos en cada nivel hasta alcanzar el nivel deseado.

El menú de instrucciones del juego le podrá ofrecer nuevamente las intrucciones del juego.
![](https://github.com/debernall/Proyecto_Programacion/blob/32c4cb352484fcbed075ee1bea9935d82be885b0/img_wiki/5.png)

## Obstáculos, rebotes y límites de pantalla
En cada uno de los niveles y conforme aumenta la dificultad del juego, le aparecerán diferentes obstáculos que podrán ser satélites o robots que se desplazan a través del espacio jugable, naves esféricas, montañas o montículos de piedra que añadiran un poco de dificultad a los cálculos que deberá realizar. Adicionalmente, podrá explotar la física del movimiento calculando los rebotes de la bala, sin embargo deberá recurrir a la información proporcionada en esta página para calcular dicho efecto, esto le será util si su objetivo se encuentra rodeado de naves alienigenas.

### Obstáculos estacionarios
![](https://github.com/debernall/Proyecto_Programacion/blob/2cf7d5372d9a95a11d24eda4829daf9afc746458/img_wiki/7.png) ![](https://github.com/debernall/Proyecto_Programacion/blob/2cf7d5372d9a95a11d24eda4829daf9afc746458/img_wiki/8.png)

En los planetas Trappist-1D y Proxima B se encontrará con obstáculos estacionarios que corresponden al borde una meseta y una gran roca respectivamente que le impedirán alcanzar el objetivo. Considere evitar algunos ángulos de lanzamiento ya que cualquier impacto con estas superficies provocará que la bala detenga su movimiento.

![](https://github.com/debernall/Proyecto_Programacion/blob/25a95035495db3ba623ed8a9ae75ca1bd55156d1/img_wiki/4.png)

En la invasión a Tokio se encontrará con cinco naves alienigenas esféricas suspendidas en el espacio jugable de manera aleatoria. Los impactos con estas naves provocarán el rebote la bala con una consecuente pérdida de velocidad, en algunas ocasiones deberá hacer uso de diferentes rebotes para alcanzar el objetivo en este nivel. 

### Obstáculos móviles
![](https://github.com/debernall/Proyecto_Programacion/blob/25a95035495db3ba623ed8a9ae75ca1bd55156d1/img_wiki/9.png)

En los planetas Marte y Ganimedes se encontrará con los satélites de exploración espacial Rover y Fenix, así como con el robot de exploración de superficies Rover. Debe evitar el contacto con estos importantes objetos de exploración debido a que podría causar su destrucción y perder su nivel. En el planeta Ganimedes se encontrará que el satelite Rover orbitará muy cerca al objetivo por tanto debe elegir el momento adecuado de lanzamiento.

### Rebotes en la superficie
Cada uno de los diferentes planetas que componen Parabolic Shot permiten que la bala rebote de acuerdo a las condiciones de superficie dadas al planeta, algunos planetas rocosos harán que la pelota pierda mucha velocidad en cada impacto contra el suelo, mientras que algunos planetas de superficies lisas permitirán que la bala rebote conservando casi toda su energía tras el impacto. Esta información le podría ser util si debe emplear rebotes para alcanzar el objetivo.

### Límites de pantalla
Todos los mundos tienen como límite de desplazamiento de la bala el borde de la imagen de fondo del planeta, tras alcanzar dicho límite el nivel será perdido.

***
# Física del movimiento parabólico

En el vacio y bajo la acción de un campo gravitatorio, un objeto lanzado experimentará un movimiento parabólico. De las leyes de Newton se obtienen el conjunto de ecuaciones necesarias para resolver el sistema. Considere un sistema coordenado cartesiano con origen en la posición inicial de la bala de cañon, el movimiento de la bala de cañon vendrá definido por el conjunto de ecuaciones:

 m*a_x = 0
 m*a_y = -m*g

Aunque inicialmente en el espacio la gravedad es aproximadamente cero y para lograr acertar solo necesitará usar sus conocimientos básicos de trigonometría, en los siguientes niveles deberá recurrir a integrales para alcanzar el objetivo. 

En los niveles en los cuales aparece un coeficiente de arrastre diferente de cero deberá considerar una aproximación para el efecto de la fuerza de fricción del aire sobre la bala cuando la velocidad de lanzamiento es baja, es decir se desprecian efectos debidos a la turbulencia. El coeficiente de arrastre (b) le es suministrado en la interfaz gráfica del juego. El conjunto de ecuaciones que deberá solucionar es el siguiente: 

 m*a_x = b*v_x
 m*a_y = -m*g + b*v_y

Podrá usar técnicas de solución de ecuaciones diferenciales y es posible que adicionalmente emplee sus habilidades algebraicas para encontrar el ángulo y la velocidad de lanzamiento adecuadas para lograr el correspondiente punto. En cualquier caso deberá recurrir a su experiencia física.

![](https://github.com/debernall/Proyecto_Programacion/blob/04aa31a8dab3352ac2bb1b41e9de4a5c31f8c499/img_wiki/10.png)

***
# Niveles
* Espacio: Consiste en el nivel 0 de Parabolic Shot, en este nivel se asume una gravedad de 0.0001 m/s^2 y condiciones de vacio.  
* Luna: Es un nivel ambientado en la fotográfia tomada durante el alunizaje del Apolo 11 en 1969. Se simula en este nivel las condiciones de vacio debido a la ausencia de una atmósfera y se considera un valor de gravedad de 1.6m/s^2. El objetivo en este nivel se ubicará aleatoriamente sobre la superficie lunar. El coeficiente de restitución (e) tras cada choque con la superficie lunar es de e=0.4.
* Gliese 581-C: Este nivel simula las condiciones del planeta extrasolar Gliese 581-c que orbita la estrella Gliese 581, la cual se encuentra a 20.5 años luz de la tierra. Su masa es aproximadamente 5 veces la masa de la tierra y un radio de 1.5 radios terrestres. Dadas las caracteristicas de este planeta, de manera interactiva no le fue asignada una atmósfera, le fue dada una gravedad de 17.39m/s^2 y un coeficiente de restitución de 0.8.
* Trappist-1D: Este nivel se encuentra ambientado en el exoplaneta ubicado a 40 años luz de la tierra y que orbita la estrella enana ultrafria TRAPPIST-1 que se encuentra en la constelación de acuario. Es uno de los exoplanetas donde se cree puede existir vida, sin embargo se consideran condiciones de vacio. Sus condiciones son similares a las de la tierra, tiene un radio de 0.78 radios terrestres y aproximadamente un tercio de la masa de la tierra. En este nivel se asume una gravedad de 5.7m/s^2 para dar dificultad al juego mediante un obstáculo en forma de meseta que impide el acierto con el objetivo. El objetivo aparacerá en una región ubicada sobre la meseta. Los rebotes poseen un coeficiente de restitución de 0.1.
* Próxima B: Es un nivel inspirado en el exoplaneta que posiblemente alberga vida y orbita la estrella mas cercana al sol, llamada Proxima Centauri. Su radio es aproximadamente 0.14 radios terrestres y posee una masa de 0.1 masas terrestres. Se asumen condiciones de vacio, una gravedad de 19m/s^2 y un coeficiente de restitución de 0.01. En este nivel aparece un obstáculo en forma de roca rectangular gigante, tras la cual se ubica el objetivo en una posición aleatoria. El impacto con la roca provocará que la bala detenga su movimiento.
* Marte: Este nivel representa un lanzamiento en el planeta rocoso marte, a este nivel se le asigna la gravedad estimada para dicho planeta la cual corresponde a 3.721m/s^2. Dada la baja densidad de su atmósfera, se simulan condiciones de vacio. En este nivel aparecerán obstaculos móviles que son representados por los satélites y robots exploradores Rover y Fenix. Los impactos con la superficie presentan un coeficiente de restitución de 0.2.
* Triton: Este sexto nivel se encuentra inspirado en el satélite de Neptuno, Triton. Dadas sus características rocosas, permiten realizar lanzamiento sobre su superficie. A este satélite le fue asignada una gravedad de 0.78 m/s^2 y un coeficiente de restitución de 0.3. Una particularidad de este nivel consiste en la ubicación del cañon, ya que este se coloca sobre la superficie de una gran masa de hielo y el objetivo se ubica a una altura menor. En este nivel no es posible cambiar el ángulo de lanzamiento y se asumen unas condiciones de vacio. 
* Ganimedes: El septimo nivel es una representación del satélite Ganímedes que orbita Júpiter. En este nivel se asume una gravedad de 1.46 m/s^2 y un coeficiente de restitución de 0.2. En este satélite nuevamente aparecerán los satélites y robots de exploración Rover y Fenix con la particularidad que el satélite artificial Rover se encontrará orbitando al rededor del objetivo, dificultando el acierto. Se asumen condiciones de vacio.
* Tierra: Este nivel ambientado sobre una pradera en la tierra presenta un nivel de dificultad superior al aparecer efectos debidos a la fricción con el aire. En este nivel se considera la gravedad de la tierra 9.8 m/s^2, un coeficiente de restitución de 0.2 y un coeficiente de arrastre de 0.01 N*s/m.
* Kepler 22b: Este nivel simula las condiciones del primer exoplaneta descubierto en una zona habitable y con posibles condiciones para encontrar agua en estado liquido. El planeta se encuentra a 600 años luz de la tierra y orbita al rededor de la estrella Kepler 22. Su radio y masa son similares a la de la tierra, sin embargo de manera interactiva en el juego se considera una gravedad de 20 m/s^2 y un coeficiente de restitución de 0.8. Dada la posible presencia de agua, fue considerada una atmósfera densa que incrementa el grado de dificultad de acierto, este nivel presenta un coeficiente de arrastre de 0.3 N*s/m. 
* Invasión alien: El nivel final del juego representa una invasión alienigena de naves esféricas a la ciudad de Tokio, en este nivel la bala de cañon puede rebotar con las naves. Las condiciones son iguales a la del nivel tierra, con la diferencia que le es asignado un valor del coeficiente de restitución igual a 0.8. Las cinco naves aparecerán de manera aleatoria en el espacio jugable e impediran el acierto. Es el nivel más dificil del juego ya que aparecen efectos de fricción del aire y rebotes con obstáculos estáticos.

# Introducción al código
Parabolic Shot es un juego construido mediante la libreria Pygame y en apoyo con librerias como Numpy y Math. El juego se contruyó a partir de la superposición de imagenes cuyas posiciones son dadas por un conjunto de vectores que presentan todas las posiciones de los objetos. El juego se encuentra enfocado en la programación orientada a objetos y se encuentra totalmente escrito en lenguaje Python.

***
# Estructura
Un archivo main llamado proyecto.py y dos archivos librerias llamados mov.py y menu.py constituyen el juego. El script proyecto.py incluye la mayor parte funcional del código, alojando el arranque del juego, el manejo de los menús, la creación de clases y objetos, entre otros. El script mov.py es un módulo de cálculo que permite dadas unas condiciones iniciales establecidas por el main crear un conjunto de vectores que finalmente originan toda la cinemática asociada al juego. Por otra parte el script menu.py pretende almacenar algunas funciones de creación de menús, esto con el fin de dar organización y reducir la extensión del main.

## Modelo de clases
Una clase es empleada en el main del proyecto. La clase mundo permite la creación de los diferentes niveles que se ejecutan a lo largo del juego. Los objetos de la clase mundo, son creados mediante el menú interno del juego, donde se llama directamente a la función main de la clase mundo. Los objetos se contruyen a partir de atributos definidos en diccionarios y que poseen todas las variables necesarias para definir los diferentes niveles, desde sonidos, imagenes, caracteristicas físicas y hasta definiciones de límites dentro de los niveles. 

La principal función de dicha clase es la función main(). Esta función se encarga de la creación de la interfaz gráfica, la reproducción de sonidos, la captura de información desde el teclado, entre otras funciones. Funciones auxiliares son empleadas por la función main() como lo son rotate(), pos_obstaculo(), nueva_pos() y dibujar(). Estas funciones se encargan de ejecutar segmentos de código que se repite frecuentemente dentro de main().

rotate() se encarga de la rotación de imagenes, ofrece una forma fácil de ejecutar movimientos de rotación como la realizada por el jugador sobre el cañon al presionar las teclas izquierda o derecha.

pos_obstaculo() es la función encargada de calcular la rotación del satélite artificial Rover al rededor del objetivo en el planeta Ganimedes. Dado que a lo largo del lanzamiento, los objetos se encuentran en movimiento fue necesario determinar en cada instante la posición de dicho objeto dada las nuevas posiciones del objetivo. Esta función en composición con el movimiento del marco de referencia del juego permite obtener dicho efecto de rotación.

nueva_pos() es la función encargada de calculas las posiciones de los obstáculos con trayectorias independientes Fenix y Rover. Surgió de la reutilización de código previo, esta función se encargaba de calcular las posiciones de todos los objetos del plano del juego dadas las variables: posición inicial, velocidad inicial, gravedad y tiempo. Esta función presenta deficiencias en el cálculo preciso de movimientos debido a que calcula posiciones en intervalos de tiempo marcados mediante ciclos de pygame, dicho tiempo no se correlaciona con el tiempo real.

dibujar() es la función encargada de permitir la visualización en pantalla dadas las imagenes y las posiciones a dibujar.

Previamente a la inicialización del ciclo que permite la ejecución del juego, son declaradas las variables de inicialización del juego tales como step, angle, fino, colision, disparo, etc. Estas variables establecen los valores iniciales y en muchas ocasiones son . 

Dentro de la función main() de la clase mundo se encuentra el ciclo while que permite la ejecución del juego. Allí se establecen las interrupciones de teclado, la captura de información mediante los controles, la visualización de las imagenes, la gestión de las variables de juego como colision, gameover, etc, la visualización de los cuadros informativos y el minimapa.

## Interfaces de menú
El juego presenta diferentes tipos de pantallas, estas interfaces son definidas dentro de funciones. mundo_main(), intro_game(), outro(), creditos() e intrucciones_juego() son las diferentes interfaces empleadas en el juego.

mundo_main() descrita previamente crea la interfaz principal del juego, allí se posicionan las imagenes del juego. Las imagenes del fondo del mapa corresponden a imágenes de tamaño 4000x4000 pixeles, el tamaño de la pantalla que visualiza el jugador corresponde a una porción de pantalla de tamaño 800x750 pixeles. Durante los diferentes movimientos de traslación de la bala, la pantalla que visualiza el jugador mantiene la posición relativa de la bala centrada en la pantalla mientras el resto de imagenes se desplazan. Un ejemplo se muestra en la siguiente figura.

![](https://github.com/debernall/Proyecto_Programacion/blob/d9397d07fcee93604b6500f91aca8c8acbdbe4db/img_wiki/12.png)

Esta interfaz tambien presenta en pantalla un minimapa que presenta un representación a escala de los objetos presentes en el mapa. Dada la gran extensión del mapa, la escala de los objetos como el cañon, la bala, el objetivo o los obstaculos se muestran a una escala mayor, esto con el fin de facilitar su visualización. En el minimapa, el unico elemento que se desplaza es la bala, que para efectos interactivos se representa con color rojo.

La interfaz intro_game() dibuja el menú principal del juego, allí se reproduce el sonido de fondo principal del juego, se da acceso al menú intrucciones y se permite salir del juego. Esta interfaz no direcciona directamente al jugador a los diferentes niveles, sin embargo tras su cierre y gracias a la gestión del menú interno del juego es posible acceder a los diferentes niveles. 

La interfaz outro() corresponde al menú de gameover. Este menú tiene un funcionamiento similar al anterior a diferencia que ofrece acceso a los cŕeditos y un llamado al menú principal. El menú interno del juego activa uno de los bucles del juego mediante dicha interfaz, la inicialización de este bucle while reinicia las variables nivel y puntos que permiten acceder a los diferentes niveles.

Las interfaces creditos() e intrucciones_juego() son pantallas que muestran información extra del juego.

## Menú interno de juego
Dos ciclos while son empleados para la ejecución del juego, inicialmente se ejecuta intro_game() la cual permite la visualización del menú principal, tras su cierre se ejecuta un primer ciclo while que permanece activo siempre. Este ciclo se mantiene gracias a la variable "jugar" que nunca cambia su estado, tras cada ciclo se establecen condiciones de inicialización de juego como nivel=0 y puntos=0. Este bucle while permite al jugador reiniciar el juego y recorrer todos los niveles desde el principio.

Un segundo bucle while se ejecuta posteriormente, este se mantiene activo gracias a jugar_outro=True, variable que si puede cambiar su valor si el jugador ha pasado a través de todos los niveles. Un conjunto de condicionales dirigidos por la variable nivel permiten la creación de los objetos mundo y su consecuente ejecución. Las teclas A y S durante la ejecución de la función mundo.main() retornan un valor de True que se carga en la variable jugar_outro, manteniendo este segundo bucle while activo. La única forma de finalizar este bucle consiste en superar el nivel 10 o por medio del comando pygame.quit() que se ejecuta con la tecla escape o cerrando la ventana.

Al finalizar el segundo bucle, se muestra el menú de gameover. El cual permitirá al jugador si lo desea reiniciar los contadores nivel y puntos para jugar de nuevo.

        jugar=True
        jugar_outro=True
        intro_game()
        while jugar:
          nivel=0
          puntos=0
          while jugar_outro:
              if nivel==0:
                  jugar_outro=mundo.main(space)
              elif nivel==1:
                  jugar_outro=mundo.main(luna)
              elif nivel==2:
                  jugar_outro=mundo.main(gliese)
              elif nivel==3:
                  jugar_outro=mundo.main(ross)
              elif nivel==4:
                  jugar_outro=mundo.main(proximab)
              elif nivel==5:
                  jugar_outro=mundo.main(marte)
              elif nivel==6:
                  jugar_outro=mundo.main(triton)
              elif nivel==7:
                  jugar_outro=mundo.main(ganimedes)
              elif nivel==8:
                  jugar_outro=mundo.main(tierra)
              elif nivel==9:
                  jugar_outro=mundo.main(kepler)
              elif nivel==10:
                  jugar_outro=mundo.main(tokio)
              else:
                  jugar_outro=False

          jugar_outro=outro('Menú','intentalo de nuevo')`

***
# Funcionamiento
## Creación de niveles
Los objetos de la clase mundo corresponde a los diferentes niveles o mundos que recorre el jugador. El constructor de la clase mundo recibe un diccionario con 27 variables que definen las propiedades de un nivel. Un ejemplo de dicho diccionario para el ultimo nivel se muestra a continuación:

    `p_tokio={'g':9.8,
          'im_fondo': "img/tokio.jpg",
          'son_mundo':"sound/tokio.wav",
          'factor_perdida':0.8,
          'nombre_planeta':'INVASIÓN ALIEN',
          'vlimt':3000,
          'im_min':"img/tokiomini.jpg",'px':0,
          'py':-3000,
          'yi':200,
          'yf':3350,
          'mountain':1,
          'little_mountain':1,
          'im_objetivo':1,
          'im_objetivo1':1,
          'im_objetivo2':1,
          'im_roversito':1,
          'im_rovertierrita':1,
          'im_fenixito':"img/nave.png",
          'py2':-3000,
          'lim_angle':0,
          'vinf':50,
          'im_piedra':1,
          'piedrita':1,
          'lim_anglesup':90,
          'b':0.01,
          'tipo':1,
          'n_obj_mov':5
          }`

Las diferentes variables son:
* g: Gravedad
* im_fondo: La imagen del mapa de juego en tamaño 4000x4000 pixeles en formato jpg
* son_mundo: La pista a reproducir durante la ejecución del nivel, debe ser de formato wav para evitar incompatibilidad con diferentes sistemas operativos
* factor_perdida: Coeficiente de restitución
* nombre_planeta: Nombre asignado al nivel
* vlimt: Máxima velocidad de lanzamiento permitida
* im_min: Imagen de fondo a escala, su tamaño debe ser de 200x200 pixeles
* px: Posición inicial horizontal de la imagen de fondo
* py: Posición inicial vertical de la imagen de fondo
* yi: Posición vertical minima del espacio jugable
* yf: Posición vertical máxima del espacio jugable
* mountain: Carga una imagen de montaña en el mapa, el valor 1 deja esta variable sin efecto en el juego
* little_mountain: Carga una imagen miniatura de montaña en el minimapa, el valor 1 deja esta variable sin efecto en el juego
* im_objetivo: Carga una imagen del satélite Rover en el mapa, el valor 1 deja esta variable sin efecto en el juego
* im_objetivo1: Carga una imagen del robot Rover en el mapa, el valor 1 deja esta variable sin efecto en el juego 
* im_objetivo2: Carga una imagen del satélite Fenix en el mapa, el valor 1 deja esta variable sin efecto en el juego
* im_roversito: Carga una imagen miniatura del satélite Rover en el minimapa, el valor 1 deja esta variable sin efecto en el juego
* im_rovertierrita: Carga una imagen miniatura del robot Rover en el minimapa, el valor 1 deja esta variable sin efecto en el juego 
* im_fenixito: Carga una imagen miniatura del satélite Fenix en el minimapa o carga la imagen de nave alienígena en el nivel 10, el valor 1 deja esta variable sin efecto en el juego
* py2: Establece un límite inferior para rebote de la bala
* lim_angle: Establece un límite inferior al ángulo de rotación del cañón
* vinf: Establece la velocidad minima de lanzamiento
* im_piedra: Carga una imagen de roca en el mapa, el valor 1 deja esta variable sin efecto en el juego
* piedrita: Carga una imagen miniatura de roca en el minimapa, el valor 1 deja esta variable sin efecto en el juego
* lim_anglesup: Establece un límite superior al ángulo de rotación del cañón
* b: Coeficiente de arrastre
* tipo: (0) condiciones de vacio, (1) aproximación para bajas velocidad del efecto de fricción del aire proporcional a la velocidad de desplazamiento, (2) efecto de fricción del aire para altas velocidades sin embargo no se emplea este último en el juego
* n_obj_mov: Número de naves obstaculo presentes en el mapa

La función mundos.main() inicialmente permite la carga de imagenes que se van a usar dependiendo las variables establecidas, posteriormente carga los sonidos a reproducir, establece las posiciones iniciales de cada uno de los objetos a dibujar en pantalla e inicializa las variables de juego. Un ajuste a la variable clock.tick() permite establecer la velocidad de ejecución del ciclo while(running) del juego. Una variable t1 inicializada en cero mantiene el juego estático mientras el jugador elige las condiciones de lanzamiento. Tras accionar el disparo, t1 marca un tiempo dado por pygame, el cual es escalado a segundos y almacenado en la variable k2.



Previo al disparo, mediante interrupciones del teclado el jugador modifica las variables speed y angle que determinan las condiciones de lanzamiento de la bala. Las teclas R y T permiten intercambiar entre ajuste fino (0.1) y grueso (1) para la graduación de las variables speed y angle mediante teclado. Un llamado a la función mov.pseg() permite calcular la altura máxima alcanzada por la bala, si dicha altura supera el límite establecido para el mapa, no se permite el incremento adicional de las variables speed y angle; por el contrario decrecen en una unidad. Esto evita que la bala se salga del mapa en la parte superior. La variable angle, permite realizar en cada ciclo la correcta rotación de la imagen del cañón y sus diferentes elementos. 

Funcionalidades adicionales permiten que la imagen de explosión de desvanezca con el paso del tiempo, esto se logra incrementando el valor del canal alfa de la imagen explosión.

Diferentes condicionales permiten elegir las imagenes a graficar y el orden en que surgen. Posteriormente se calculan las futuras posiciones de los elementos a visualizar. Esto se logra mediante la variable k2 que almacena el tiempo en s del juego.

Al presionar la tecla de disparo (espacio), el sistema recopila la información de las condiciones iniciales de lanzamiento y por medio de la función mov.calc_vector se obtienen un conjunto de vectores que describen el movimiento de la bala. Tres vectores son relevantes, (x,y,t). Un aproximación permite encontrar el valor mas cercano a k2 en el vector t y se obtiene la posición k de dicho elemento dentro del vector. Dicha posición k define para un instante: el tiempo y las posiciones x,y. Posteriormente por medio de un conjunto de traslaciones y reflexiones se obtienen las posiciones de cada elemento del juego.

En cada ciclo y bajo la presencia de obstáculos móviles, se calcula la distancia del centro de la bala al centro de cada obstáculo. Si esta distancia es menor a cierto umbrál, el juego activa variables de gameover que permiten detener la animación y perder el nivel.

Las variables colision y gameover establecen la detención del tiempo y la activación de las interrupciones de teclado mediante las teclas A y S.

Un conjunto de condicionales evitan que los diferentes obstáculos móviles se salgan del mapa, invirtiendo su velocidad al alcanzar los límites del mapa.

Finalmente, sobre las imágenes cargadas de los diferentes elementos se cargan las imágenes de los cuadros indicadores.
## Funciones de posición
Dos funciones de posición son definidas, la primera mov.parabolaseguridad() limita la velocidad y el angulo de lanzamiento para evitar la salida de la bala fuera del mapa y mov.calc_vect() retorna las posiciones de la bala tras el lanzamiento.
### Implementación de vectores de posición
La tecnica de los vectores de posición reduce la cantidad de cálculos realizados en mundos.main() debido a que un conjunto de vectores almacenan todas las posiciones del elemento a desplazar. Esto permite encontrar el comportamiento de la bala empleando ecuaciones diferenciales evitando con ello encontrar las ecuaciones de movimiento de la misma. Adicionalmente, es posible incluir efectos de rebote en el movimiento.
### Aproximación por métodos numéricos
Por medio de una aproximación mediante métodos numéricos usando Runge-Kutta de orden 4 es posible encontrar los vectores x,y,v_x,v_y,t dadas unas condiciones iniciales y un conjunto de ecuaciones diferenciales. Una función mov.runge_kutta() genera como resultado un conjunto de vectores que posteriormente bajo ciertas condiciones de juego son recortados y almacenados en otros vectores que recopilan todo el movimiento de la bala, incluyendo interacciones de tipo rebote, colisión y límites de pantalla.

### Obtención de vectores de posición
mov.calc_vect() 

### Parábolas de seguridad

***
# Instalable
## Windows

## Linux

***
# Como contribuir con el proyecto
## Interfaz de creación de mundos
## Ecuaciones de movimiento
## Obstáculos
## Optimización


Los textos y las imágenes que aparecen en la interfaz se cargan en archivos de texto y png respectivamente. Luego se define una función para cada parte de la interfaz, es decir, créditos e introducción, y mediante condicionales que funcionan mientras el ciclo while de cada función
continúe, se hace que pygame reconozca los clics del mouse para continuar. Luego se definió la clase mundo, la cual admite una lista de 27 parámetros, con los datos sobre la gravedad, obstáculos, factor de pérdida en colisión contra el suelo, factor de resistencia del aire, posición del objetivo, etc.

La posición del objetivo se define entre unos rangos que vienen de los parámetros de la clase mundo, y se genera mediante una función random en ese rango de posiciones. 

Hay obstáculos en movimiento y estacionarios, en todos los casos cuando se produce el choque se pierde. Y la colisión se determina calculando la distancia entre los centros de la bola y el obstáculo, y con un condicional se pone el radio a partir del cual se considera colisión, y este radio está relacionado con el tamaño de la imagen del obstáculo. Los obstáculos tienen movimientos periódicos, por lo que es relativamente fácil predecir sus posiciones. Con condicionales se invierten las velocidades cuando llegan a los bordes del mapa.

En otra carpeta se definieron las funciones que calculan las posiciones, por lo que desde la carpeta principal se importan las funciones, con estas se guardan las posiciones en un vector y ya solo es llamar las componentes, y no es necesario hacer más cálculos después de usada, es decir, ya se tiene toda la trayectoria en el vector.

El juego es interactivo ya que permite al jugador cambiar el ángulo y la velocidad inicial, y esto se hace mediante condicionales dentro del ciclo principal, los cuales dan opción al jugador de aumentar o disminuir el ángulo y la velocidad inicial a partir de las flechas del teclado. Y se hizo un mini mapa, el cual es una versión a escala del principal, por lo que se hizo fue multiplicar las variables por un factor de escala y pintarlos nuevamente, con imágenes cargadas en tamaño reducido.

#********************************** USO DE LA FUNCION POSICIONES *******************************

         ##################  COLOCAR LAS CONDICIONES INICIALES DEL LANZAMIENTO EN S.I.
         # x0=0                            #POSICION INICIAL DE LA BALA EN X
         # y0=0                            #POSICION INICIAL DE LA BALA EN Y  
         # theta0=1.6*math.pi/4            #ANGULO DE LANZAMIENTO
         # v0=16                           #MAGNITUD DE VELOCIDAD INICIAL
         # g=9.8                           #GRAVEDAD
         # e=0.8                           #FACTOR DE PERDIDA DE VELOCIDAD
         # xlim=100                        #LONGITUD MAXIMA DEL TABLERO EN X
         # ylim=10000                      #LONGITUD MAXIMA DEL TABLERO EN Y
         # epsilon=0.0001                  #ESPACIAMIENTO DEL VECTOR TIEMPO
         # impactos=((20,3,1.1,False),(35,8,2,True),(10,8,2,False))    #VECTOR DE OBSTACULOS Y OBJETIVO: (X_CENTRO,Y_CENTRO,RADIO,TRUE:OBJETIVO/FALSE:OBSTACULO)
         # max_rebotes=10                  #PERMITE ESTABLECER UN MAXIMO DE REBOTES

         ################   FUNCION QUE DA COMO RESULTA UN 4 VECTORES: X(t), Y(t), t y de nuevo devuelve impactos
         #(x,y,t,impactos)=posiciones.posiciones(x0,y0,theta0,v0,g,e,xlim,ylim,epsilon,impactos,max_rebotes)
         #posiciones.graficar(a[3],a[0],a[1])

         ################    LOS VECTORES ENCONTRADOS DEFINEN LA TRAYECTORIA DE LA BALA
         ################    para obtener el efecto de desplazamiento se deben aplicar transformaciones
         ################    1. Las reflexiones en x,y se obtienen con x'=-x, y'=-y
         ################    2. Las traslaciones permiten ubicar cada elemento en un posicion primada
         ################    3. Aplicar un escalado de los puntos que esta relacionado por la proporcion metros/pixel

         ################    UN CONJUNTO DE VECTORES DETERMINAN EL DESPLAZAMIENTO TOTAL DEL SISTEMA
         ################    no es necesario calcular repetidamente dicho vector, se debe calcular una sola vez
         ################    teniendo en cuenta que x,y son funciones de t. Las coordenadas en un tiempo dado
         ################    deben calcularse asi:
         ################    1. Establecer un t1(s) en el bucle principal del juego
         ################    2. Buscar con k=np.where(t>t1)[0] la posicion del elemento del vector que cumple la condicion
         ################    3. La posicion obtenida (x,y) para un t1 dado será: (x[k],y[k])
         ################    4. Aplicar las transformaciones necesarias
         ################    Conviene definir un origen en la parte inferior derecha (traslacion1)
         ################    Luego calcular las posiciones de los objetos respecto a dicho nuevo origen (traslacion2)
         ################    Aplicar una reflexión sobre el sistema de puntos para obtener el efecto de desplazamiento
         ################    Aplicar el escalado de los puntos
         ################    El minimapa puede ser obtenido de manera similar pero con un segundo escalado
