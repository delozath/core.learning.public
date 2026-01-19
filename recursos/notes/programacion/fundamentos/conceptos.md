# Definiciones operativas y abstracciones
## La necesidad de calcular
La humanidad ha desarrollado las matemáticas como una herramienta para comprender y describir el mundo que nos rodea. Desde los albores de la civilización, las personas han utilizado cálculos para resolver problemas prácticos, desde la agricultura hasta la construcción y el comercio. A medida que la sociedad ha evolucionado, también lo han hecho nuestras necesidades de cálculo, impulsando avances en tecnología y ciencia. Si bien, actualmente diversos campos de las matemáticas son tan abstractos que pueden no tener una interpretación en nuestro mundo físico, tomaremos momentaneamente las matemáticas que sí la tienen para el resto de nuestra discusión.

Supongamos que necesitamos sumar 1035819 + 9583927. Podemos realizar esta operación utilizando lápiz y papel, y muy probablemente obtendremos el resultado correcto. Ahora supongamos que queremos sumar 10000 números de 7 dígitos cada uno. En este caso, tenemos dos inconvenientes: 1) el tiempo que nos tomaría realizar la operación manualmente y 2) el aumento de la probabilidad de cometer errores al realizar cálculos repetitivos. Por cierto, realizar este tipos de sumas es un caso típico de las operaciones que realizan los sistemas de inteligencia artificial actualmente, por lo que no es una aplicación fuera de contexto o que solo sirve para un ejemplo académico.

Bien, entonces la pregunta que surge es: ¿Cómo realizar cálculos de manera más rápida, precisa y consistente? La humanidad ha desarrollado diversas herramientas a lo largo de su historia para resolver este problema. Entre los que encontramos  el ábaco, las reglas de cálculo, las calculadoras mecánicas (pascalinas) y electrónicas, y finalmente las computadoras digitales.

Sin embargo, si necesitamos realizar esta operación millones de veces, o si necesitamos realizar cálculos mucho más complejos, hacerlo manualmente se vuelve impráctico y propenso a errores. Aquí es donde entran en juego las computadoras.

Las computadoras, en sus aplicaciones más básicas, son máquinas diseñadas para ejecutar instrucciones de manera precisa, repetitiva y consistente. Esto utilizando cuatro abstracciones fundamentales:
1) Memoria: es la unidad en donde se almacenan datos y las instrucciones a ejecutar.
2) Procesador: es la unidad que interpreta las instrucciones almacenadas en memoria y las ejecuta. Si las instrucciones generan resultados, estos se almacenan nuevamente en memoria.
3) Dispositivos de entrada/salida: son los medios a través de los cuales la computadora interactúa con el mundo exterior, ya sea recibiendo datos (entrada) o enviando resultados (salida).
4) Programa: es una secuencia de instrucciones codificadas en un lenguaje que la computadora puede interpretar y ejecutar.

Los elementos 1, 2 y 3 son componentes físicos de la computadora a los que se les denomina *hardware*, mientras que el programa es una entidad lógica que reside en la memoria y guía el comportamiento del procesador y los dispositivos de entrada/salida por lo que físicamente simplemente es almacenado en la memoria, a este componente lógico se le denomina *software*.

El lenguaje humano es inherentemente ambiguo y contextual, lo que puede llevar a malentendidos y errores en la comunicación. En programación, esta ambigüedad puede resultar en código difícil de entender, mantener y depurar. Por ello, es fundamental adoptar prácticas que promuevan la claridad y la precisión en la escritura del código. Es por eso que podría denominarse como un lenguaje circular, ya que el significado de una instrucción puede depender del contexto en el que se utiliza. Aquí el contexto importa mucho.

Por otra parte, para poder realizar una tarea específica es necesario expresarla en sus componentes más básicos para que pueda ser interpretada y ejecutada adecuadamente, de forma consistente y predecible cada vez. Por lo que expresarla en lenguaje humano puede no ser la mejor opción.

A diferencia de los humanos, las computadoras no pueden interpretar el lenguaje natural con todas sus sutilezas y ambigüedades. Por lo tanto, es esencial que las instrucciones que se les proporcionan sean claras, específicas y estructuradas de manera lógica.