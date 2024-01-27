# CTF_UdG

## Conceptos Basicos
#### 1. ¿Qué son los sistemas tolerantes a fallas?
Un sistema tolerante a fallas, como lo dice su nombre, es un sistema que puede soportar fallas sin dejar de funcionar, o un sistema preparado para fallar, 
cuando intentamos asegurarnos que un sistema sea tolerante a fallas, buscamos puntos únicos de falla y encontramos maneras de añadir redundancia en esos puntos.

#### 2. ¿Qué es una falla?
La falla es la revelación del defecto al utilizar el sistema,  
es un término general que se utiliza para designar que un componente, equipo o máquina ha fallado en servicio. 
Es la manifestación de un error que encontramos al utilizar el equipo, producto, sistema, etc, que fue creado con un error.
#### 3. ¿Qué es un error?
Es una acción humana que produce un resultado incorrecto, o el error humano y
dentro de la relación de fallo, defecto y error, el error es lo que origina un defecto y la falla es el defecto encontrado al utilizar el equipo.
#### 4. ¿Qué es la latencia de un fallo?
 El tiempo que transcurre entre un fallo y la representación de su error
#### 5. ¿Cuál es la latencia de un error?
Es el tiempo que transcurre entre un error y un fallo. 
_Para leer el documento, [AQUI](https://docs.google.com/document/d/1_8OKN61mIKXfYk3GFOrs-uRX9D1J38tUp6hcpT2WUO8/edit?usp=sharing)_

## Herramientas para el manejo de Errores
Las herramientas para el manejo de errores son mas que herramientas creadas para ello son formas de usar las herramientas que ya tienen los lenguajes para idear como validar nuestras entradas y salidas para que los errores que puedan salir de ellos no afecten el programa en general.
#### *Try Catch*
Nos permite “atrapar” errores para que el script pueda, en lugar de morir, hacer algo más razonable.

```
try {
  // código...
} catch (err) {
  // manipulación de error
}
```
Lo que esta dentro de try se ejecuta en un estado de vigilancia por asi decirlo, si llegara a haber un error de esos que romper el codigo, como por ejemplo de una excepcion o un error de ejecucion, en cualquier linea del try la ejecucion de ese bloque se cortara y entrara al bloque catch, en caso de no haber ningun error, el catch no sera ejecutado.
Ademas en lenguajes como Python existe en Try...Except que hace lo mismo que hace este try catch sin embargo puede cachar errores de excepcion especificos y darles una subritina a cada uno ademas de que se agregar un ultimo bloque el bloque else que permite darle una subrutina al codigo en caso de no haber fallado o caido en alguna excepcion.
``` 
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")
```
Ademas de un finally para cerrar el bloque de prueba, estas herramientas en codigo especificamente construidas para cachar errores siempre son las herramientas predilectas para cdumplir ese objetivo para el que fueron construidas, sin embargo hay otros tips o tecnicas que usan otras sentencias para no solo cachar errores eficientemente sino para hacer el codigo mas facil de leer y analizar.
#### *Guard Clauses Technique*
Es una tecnica derivada del *fail-fast method* que tiene el objetivo de usar sentencias condicionales para cachar errores significativos antes de que se conviertan en errores mas profundos, digamos, evitar un efecto domino de errores que podrian derivarse de errores sencillos
```
public User GetUser(string userName)
{
  if (userName == null) throw new NullArgumentException(nameof(userName));
  // Continuar con la condicion
} 
```
Aqui por ejemplo validamos que la entrada no sea nula antes de escribir todo el demas procedimiento, asi no nos preocupamos de revisarlo mas adentro en la logica de esta funcion.
Otra cosa que hace esta tecnica es evitar hacer las horribles estructuras de if anidados infinitos que pueden volverse terriblemente dificil de leer, aqui un ejemplo:
```
void anyfunction() { 
	if(wifi){
		if(login){
			if(admin){
				seeAdminPanel();
			}else{
				return error();
			}
		}else{
			return error();
		}
	}else{
  return error();
	}
}
```
En esta funcion tenemos 3 if anidados que validan que haya wifi, que haya un login y que ese login sea el admin solo para poder mostrar una funcion, y despues de ello en los else retornan errores, este quiza no se muy grande pero ahora imaginate esto pero con codigo realista para saber si hay wifi, si hay un login y si ese es el admin, esto puede empeorar muy rapido, sin embargo esta tecnica ofrece esta solucion.
```
void anyfunction() { 
  if(!wifi){
   return error();
  }if(!login){
   return error();
  }if(!admin){
   return error()ñ
  }else{
   seeAdminPanel();
  }
}
```
Esto por otro lado es mucho mas facil de leer y entender, esto a tra ves de manejar errores antes, pensar en que hacer con el error antes de asumir que la entrada es la que esperamos hace el codigo mas delgado y facil de leer y entender que anidar infinitamente ifs.
#### **Fail-Fast**
Los desarrolladores también se refieren al código como "fail-fast" si intenta fallar lo más pronto posible durante la inicialización de variables u objetos. En la programación orientada a objetos, un objeto diseñado con el enfoque "fail-fast" inicializa el estado interno del objeto en el constructor, lanzando una excepción si algo está mal (en lugar de permitir objetos no inicializados o parcialmente inicializados que fallarán más tarde debido a un "setter" incorrecto). Luego, el objeto puede hacerse inmutable si no se esperan más cambios en el estado interno.

En las funciones, el código "fail-fast" verificará los parámetros de entrada en la precondición. En arquitecturas cliente-servidor, "fail-fast" verificará la solicitud del cliente justo al llegar, antes de procesarla o redirigirla a otros componentes internos, devolviendo un error si la solicitud falla (parámetros incorrectos, ...). El código diseñado con el enfoque "fail-fast" disminuye la entropía del software interno y reduce el esfuerzo de depuración.

## Ejemplo de uso
```
class Calculator {
  add(a, b) {
    this.validate(a, b);
    return a + b;
  }

  subtract(a, b) {
    this.validate(a, b);
    return a - b;
  }

  validate(a, b) {// Esta funciona vaida que lo que se ingreso sean numero
    if (typeof a !== 'number' || typeof b !== 'number') {
      throw new Error('Los dos numeros deben ser numeros');// sino lanza un error throw
    }
  }
}

// Uso de la calculadora
const calculator = new Calculator();

// Uso correcto, no lanzara error
const result1 = calculator.add(5, 10);
console.log('Resultado de la suma:', result1);

const result2 = calculator.subtract(10, 3);
console.log('Resultado de la resta:', result2);

// Intentando usar valores no numéricos
calculator.add('5', 10); // Esto lanzará una excepción Error()
```
Esta clase calculadora puede cachar errores de ejecucion sin la necesidad de usar try catch.
