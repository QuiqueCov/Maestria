# Test Optimization
Es el proceso de mejorar la eficiencia, velocidad y calidad de la ejecución de pruebas de software.<br>
No busca "probar mas rapido, sino probar más inteligente.<br>
Se busca obtener el máximo feedback sobre la calidad del código en el menor tiempo posible y con el menor consumo de recursos.<br>

## Estrategias Clave
Existen varias tecnicas para lograr esta optimizacion:
- Seleccion de pruebas (Test Selection): En lugar de ejecutar todas las pruebas cada vez que se hace un cambio(esto es muy lento), se utilizan herramientas para identificar que pruebas especificas cubren el codigo que se modifico y se ejecutan solo esas.
- Priorizacion de pruebas: Ordenar las pruebas para que las mas criticas, o las que historicamente han fallado mas, se ejecuten primero. Si algo va a fallar, quieres saberlo en el minuto 1, no en la hora 3.
- Eliminacion de "Flaky Tests" (Pruebas Inestables): Identificar pruebas que a veces pasan y a veces fallan sin razon aparente (falsos positivos/negativos). Estas pruebas se deben reparar aislar o eliminar, ya que arruinan la confianza en el sistema.
- Paralelizacion: Ejecutar multiples pruebas simultanenamente en diferentes servidores o hilos, en lugar de una tras otra (secuencialmente).
- Gestion de Datos de Prueba: Asegurarse de que los datos nececsarios para las pruebas esten disponibles y limpios rapidamente, evitando cuellos de botella en la preparacion del entorno.