# Proyecto_Programacion
 Proyecto para la enseñanza en física


 Introducción

 Los textos y las imágenes que aparecen en la interfaz se cargan en archivos de texto y png respectivamente. Luego se define una función para cada parte de la interfaz, es decir, créditos e introducción, y mediante condicionales que funcionan mientras el ciclo while de cada función continúe, se hace que pygame reconozca los clics del mouse para continuar. Luego se definió la clase mundo, la cual admite una lista de 27 parámetros, con los datos sobre la gravedad, obstáculos, factor de pérdida en colisión contra el suelo, factor de resistencia del aire, posición del objetivo, etc.

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
