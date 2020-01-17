# supermarket-model
Supermarket simulation project. First university project for programming class.
Made in Python 3.6.8
### Language
The function names and descriptions are in spanish.
The names of variables are (mostly) in spanish.
The tasks (completed or not) are in spanish.
### Execution
To start the program you need to execute the `sucursal.py` file.
### Objectives
The project consisted of a lot of small functions that the supermarket had to be
able to do in order to call the project completed.
```
[x] Agregar un nuevo producto.
[x] Eliminar un producto dado su código.
[x] Listar todos los productos de una forma prolija.
[x] Actualizar el stock cuando se vende un producto.
[x] Actualizar el precio unitario de un producto determinado en un cierto procentaje.
[x] Determinar la existencia de un producto para poder vender la cantidad solicitada.
[x] Reponer un producto cuando el stock está por debajo de un mínimo requerido.
[x] Pedir los datos de un cliente para hacer envío a domicilio.
[x] Determinar cuál es el artículo más vendido.
[x] Eliminar del supermercado (guardarlos en un otro diccionario) los artículos que estén
vencidos.
[x] Simular la venta a un cliente y emitir el ticket de venta.
[x] Agregar información adicional al producto para saber si un determinado producto tiene o no
descuento.
[x] Si el producto vence en una semana hacer un 10% de descuento.
[ ] Determinar el producto más vendido dependiendo del tipo de producto.
```

The last objective has not been completed because it requires a `'Tipo de Producto'` key in my inventory dictionary that I'm unwilling to fill in.

### Problems
I started implementing a solution to the assignment right away without planning or design. In hindsight, this would obviously lead to problems thereafter but, with my inexperience it wasn't clear at the time. Thus, the structure ofthe code is bad. I had coded a structure that supported classes and would create instances of the objects, but halfway into the project decided that it was best to work directly with a dictionary. It was easier for me to manipulate strings and dictionaries than to work with classes. I was very ambicious and tried to punch above my weight. 
--Project Coded as (01/12/2019), --Hindsight as (17/01/2020).
I suppose I will restructure the code sometime soon during summer in order to make it more clean and will opt for one of the two structures: a) keep working with dictionaries or b) create a program that supports object's instances; and work with that.
