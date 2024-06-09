# Simulación de Eventos Discretos, Teoría de Colas

## Integrantes

- José Miguel Zayas Pérez (tlgrm: @nex25k) C312
- Adrian Hernández Santos (tlgrm: @ahdez929) C311

## Introducción

El problema que hemos decidido abordar es el 6.10(Central Telefónica) del libro "Aplicando Teoría de Colas en
Dirección de Operaciones".

La compañía aérea “Siberia” tiene una centralita de teléfonos con 3 líneas. La
empresa tiene un pico de llamadas durante 3 horas, en las que algunos clientes no
pueden ponerse en contacto con la empresa debido al intenso tráfico de llamadas
(se sabe que si las tres líneas están siendo utilizadas al cliente no se le puede
retener). La compañía estima que, debido a la fuerte competencia, el 60% de las
llamadas no respondidas utiliza otra compañía. Durante las horas punta las
llamadas siguen una distribución de Poisson con una media de 20 llamadas hora y
cada telefonista emplea 6 minutos por cada llamada (distribución exponencial). El
beneficio medio de un viaje es de 210 euros, ¿cuánto dinero se pierde diariamente
debido a llamadas no contestadas? Se supone que durante las horas que no son
críticas se cogen todas las llamadas. Si cada empleado cuesta a la compañía 24
euros/hora y un empleado debe trabajar 8 horas al día, ¿cuál es el número óptimo
de empleados? Las horas punta siempre son a la misma hora. La centralita no se
cierra nunca y la puede atender un solo empleado cuando no hay hora punta. Se
asume que el coste de añadir una línea es despreciable.

## Objetivos y metas

El objetivo de este proyecto es simular el sistema de la centralita de la compañía aérea "Siberia" para poder responder a las siguientes preguntas:

- ¿Cuánto dinero se pierde diariamente debido a llamadas no contestadas?
- ¿Cuál es el número óptimo de empleados?

Además también se desea:

- Comparar los resultados obtenidos con los resultados experimentales.
- Realizar un análisis estadístico de la simulación.
- Analizar como varían los resultados al modificar los valores de las variables del sistema.

## Sistema y variables de interés

- Patrón de llegada de llamadas: Poisson con una media de 20 llamadas por hora.
  - Como se trata de un proceso de Poisson, el tiempo entre llegadas de llamadas sigue una distribución exponencial con media igual al inverso de la original, la cual es 1/3 (lo que representa 1 llamada cada 3 minutos de media). Por lo tanto, el tiempo entre llegadas de llamadas es una variable aleatoria exponencial con media 3 minutos.
- Tiempo de atención de llamadas: Exponencial con media de 6 minutos.
- Número de líneas inicial: 3. En la descripción del problema se asume que el coste de añadir una línea es despreciable, por lo que no se tiene en cuenta para la simulación.
  - Si todas las líneas están ocupadas, el cliente no puede ser retenido.
- Horas punta: 3 horas al día. Durante estas horas, el 60% de las llamadas no contestadas utiliza otra compañía.
- Beneficio medio de un viaje: 210 euros.
- Coste de cada empleado: 24 euros por hora.
- Horas de trabajo de cada empleado: 8 horas al día.

Nuestro problema se puede modelar como un sistema de colas `M/M/c/c/FIFO`, donde:

- M: Proceso de llegada de llamadas sigue una distribución de Poisson.
- M: Tiempo de atención de llamadas sigue una distribución exponencial.
- c: Número de servidores (Lineas o empleados en horario pico).
- c: Capacidad del sistema. Existen restricciones respecto al número de clientes que pueden esperar en la cola, la cual es 0, no hay cola pues como se refiere a llamadas telefónicas, si las tres líneas están ocupadas, el cliente no puede ser retenido, por lo que la capacidad total del sistema es igual a la cantidad de servidores.
- FIFO: First In First Out. Las llamadas se atienden en el orden en que llegan, siempre y cuando haya un servidor disponible.

Todas las variables son modificables en el código de la simulación para poder analizar cómo varían los resultados al modificar los valores de las variables del sistema. Estos valores iniciales son los propuestos en el problema.

## Detalles de Implementación

Para la implementación de la simulación, se ha utilizado el lenguaje de programación Python y la librería SimPy. SimPy es una biblioteca de simulación de eventos discretos basada en procesos que se ejecutan en un entorno de simulación. Permite modelar y simular sistemas complejos y es muy útil para la simulación de sistemas de colas.

El código de la simulación se divide en las siguientes partes:

- `simulation.py`: Contiene la implementación de una simulación y devuelve un array de duplas que corresponde a la cantidad de llamadas atendidas, siendo el primer valor el momento en que llegó la llamada y el segundo valor el tiempo de duración de la llamada.
- `analysis.py`: Contiene la clase Analizer que se encarga de separar los resultados obtenidos de la simulación.
- `utils.py`: Contiene funciones útiles para el manejo de los datos obtenidos de la simulación así como para la generación de gráficos.
- `queue-simulation.ipynb`: Jupyter Notebook que contiene la simulación principal y el análisis de los resultados.

Se llevan a cabo una cantidad determinada de simulaciones para diferente cantidad de empleados, luego se recogen los resultados y se analizan para determinar el número óptimo de empleados.

## Modelo matemático

Dado que nuestro problema es un clásico problema de teoría de colas de la forma `M/M/c/c`, podemos aplicar el modelo de Erlang, el cual queda definido por las siguientes fórmulas:

- Probabilidad de que el sistema esté lleno:
 `poner formulita de Pc aqui en latex`
- Número medio de clientes del sistema:
  `poner formulita de L aqui en latex`
- Tiempo medio de estancia de los clientes en el sistema:
  `poner formulita de W aqui en latex`

Nuestro sistema posee los siguientes parámetros iniciales:

- lambda = 1/3
- mu = 1/6
- c = 3

Asi que los resultados teoricos acorde al modelo para c = 3 serian:

- Pc = 4/19 = 0.21
- L = 30/19 = 1.5789
- W = 6

Pero se desea buscar un valor optimo de c tal que minimice la perdida de la compañia, asi que realizaremos nuestras simulaciones con diferente cantidad de lineas telefonicas, ya que se tiene como supuesto que el costo de agregar una nueva no varia.

## Resultados y Experimentos

Dado que el objetivo principal de la simulación es determinar el número óptimo de empleados, se realizan varias simulaciones variando el número de empleados y se analizan los resultados obtenidos. Se busca determinar cuánto dinero se pierde diariamente debido a llamadas no contestadas y cuál es el número óptimo de empleados para minimizar estas pérdidas.

Importante tener en cuenta que el valor de un empleado es de 24 euros por hora y debe trabajar 8 horas al día, siendo un total de 192 euros por día.

Los siguientes análisis se realizaron con 2000 simulaciones por cada cantidad de empleados, al volver a ejecutar el notebook se obtendrán valores muy ligeramente diferentes.

### Análisis para 3 empleados

Consideramos que el primer valor significativo a analizar es para un total de 3 empleados durante el horario pico (3h) pues con un número menor de empleados se perderían una cantidad considerable de llamdas, como se muestra en la simulación.

Media de llamadas perdidas: 11.9945

![alt text](/images/image-1.png)

Media de dinero perdido para tres empleados: 1511.307

![alt text](/images/image.png)

Considerando que añadir un nuevo empleado cuesta 192 euros al día, se puede observar que dicho coste es mucho menor que el dinero perdido por llamadas no contestadas. Por lo tanto, parece indicar que el número óptimo de empleados es mayor a 3.

### Análisis para 4 empleados

Media de llamadas perdidas: 5.4165

![alt text](/images/image-2.png)

Media de dinero perdido: 682.479

![alt text](/images/image-3.png)

Se observa que al añadir un cuarto empleado, la cantidad de llamadas perdidas disminuye considerablemente, lo que resulta en una reducción significativa del dinero perdido. Por lo tanto, parece indicar que el número óptimo de empleados es mayor o igual a 4.

### Análisis para 5 empleadoss

Media de llamadas perdidas: 2.124

![alt text](/images/image-4.png)

Media de dinero perdido: 267.624

![alt text](/images/image-5.png)

En este caso, al añadir un quinto empleado, la cantidad de llamadas perdidas es cercana a dos, lo que resulta en una reducción adicional del dinero perdido. Como la diferencia entre el dinero perdido con 4 empleados y 5 empleados es mayor que el coste de añadir un empleado adicional, parece indicar que el número óptimo de empleados es mayor o igual a 5.

### Análisis para 6 empleados

Media de llamadas perdidas: 0.711

![alt text](/images/image-6.png)

Media de dinero perdido: 89.586

![alt text](/images/image-7.png)

Con seis empleados se obtiene una cantidad de llamadas perdidas muy baja, promedio inferior a una llamada. Es importante destacar que la diferencia de dinero perdido entre 5 y 6 empleados es de 178 lo que es menor que añadir el empleado adicional, por lo que a primera instancia pareciera que se gana más dinero sin añadir a dicho empleado número 6 ya que costaría más que el dinero que se ganaría.

### Análisis para 7 empleados

Media de llamadas perdidas: 0.186

![alt text](/images/image-8.png)

Media de dinero perdido: 23.436

![alt text](/images/image-9.png)

La diferencia respecto a 6 empleados no es significativa y el dinero que se gana es considerablemente menor que el coste de añadir un empleado adicional, por lo que se concluye que el número óptimo de empleados es menor que 7.

### Análisis final

Es evidente que la cantidad óptima de empleados obtenida a partir de la simulación ronda entre los 5 o 6, pues con 5 empleados se maximizan las ganancias ya que la diferencia entre el dinero perdido con 5 empleados y 6 empleados es mayor que el coste de añadir un empleado adicional.
Sin embargo dicha diferencia es de 178 euros y un empleado cuesta 192 euros al día. Dada la naturaleza del problema y la pequeña diferencia entre 5 y 6 empleados consideramos que la cantidad óptima de empleados es 6 pues a pesar de que se pierde una pequeña cantidad de dinero respecto a 5 empleados, se gana en el largo plazo dado que se pierden menos llamadas como promedio garantizando la fidelidad y satisfacción del cliente.

- Número óptimo de empleados(durante horario pico): 6

## Parada de la simulación

Dada la naturaleza del problema la parada de la simulación se realiza por una cantidad de tiempo fija, en este caso son 3 horas o debido a que el tiempo de la simulación es en minutos, 180 minutos.

Dicho valor puede ser modificado y analizado para otros casos. (Debe ser un valor menor o igual a 8h, pues se asume que un empleado trabaja 8 horas al día).

## Asunciones y restricciones

- En la descripción del problema se asume que el coste de añadir una línea es despreciable, por lo que no se tiene en cuenta para la simulación.
- Además se dice que fuera de las horas punta se cogen todas las llamadas y un solo empleado puede atender la central, por lo que no se tienen en cuenta las llamadas no contestadas fuera de las horas punta.
- Se tiene en cuenta que un empleado tiene que trabajar 8 horas al día, por lo que al añadir nuevos empleados en la hora pico su costo es por las 8 horas que debería trabajar.
- Se asume que el horario pico(<=8h) está dentro de una jornada laboral de 8 horas y no ocupa dos de ellas.
- El problema que el 60% de las llamadas no respondidas las utiliza otra compañía, por lo que de las llamadas perdidas solo se cuenta el 60% como dinero perdido. (Se asume que el 40% restante se atiende en otro momento).

## Modelo Matemático
