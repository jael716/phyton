sandwich_de_potito = 10000
cervezas = 5000
papapleto = 2000
arepas = 13000
leche_de_palta = 17000
catidad_producto1 = int(input("¿cuantos Sandwich de Potito uno quiere? "))
catidad_producto2 = int(input("¿cuantas Cervezas quiere? "))
catidad_producto3 = int(input("¿cuantas porciones de papapleto quiere? "))
catidad_producto4 = int(input("¿cuantas arepas quiere? "))
catidad_producto5 = int(input("¿cuantos litros de  Leche de Palta quiere? "))

suma = catidad_producto1 * sandwich_de_potito + catidad_producto2 * cervezas  + catidad_producto3 * papapleto  + catidad_producto4 * arepas + catidad_producto5 * leche_de_palta

print("El Valor Neto es $  " + str(suma))
print("El IVA a Pagar es $  " + str(suma*0.19))
print("El Total es $  " + str(suma*1.19))


""""Existen varias ventajas en utilizar un entorno virtual en Python:

    Aislamiento de dependencias: Los entornos virtuales permiten crear un ambiente aislado del sistema operativo y otros proyectos de Python, lo que evita posibles conflictos con versiones de librerías y dependencias.

    Control de versiones: Los entornos virtuales permiten especificar las versiones exactas de las librerías y dependencias que se requieren para un proyecto. De esta manera, se asegura que el código pueda ser reproducido en un futuro con las mismas librerías y dependencias.

    Flexibilidad: Los entornos virtuales permiten crear distintos ambientes para distintos proyectos, incluso si estos requieren versiones distintas de las mismas librerías y dependencias.

    Portabilidad: Los entornos virtuales pueden ser creados y utilizados en distintos sistemas operativos y plataformas, lo que hace más fácil la distribución y colaboración en proyectos de Python.

    Facilidad de configuración: Los entornos virtuales son fáciles de configurar y administrar, y no requieren permisos de administrador para ser creados.

En resumen, el uso de entornos virtuales en Python permite una gestión más eficiente de dependencias y versiones de librerías, lo que hace más fácil el desarrollo y mantenimiento de proyectos de Python."""
