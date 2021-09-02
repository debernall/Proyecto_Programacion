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
