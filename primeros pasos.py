print("¡Hola!")
nombre="juan"
instructor="Python"
print("me llamo", nombre, "y soy estudiante de", instructor)
print()
print("La Witsi Witsi Araña\nsubió a su telaraña.")
print()
print("Vino la lluvia\ny se la llevó.")
print()
print("curso","de","python",sep="_",end="|")
print()
print("Programming","Essentials","in",sep="***",end="...")
print("Python")
print("    *\n   * *\n  *   *\n *     *\n***   ***")
print("  *   *\n  *   *\n  *****")
print()
print("    *        "*2)
print("   * *       "*2)
print("  *   *      "*2)
print(" *     *     "*2)
print("***   ***    "*2)
print("  *   *      "*2)
print("  *   *      "*2)
print("  *****      "*2)

print("            *")
print("           * *")
print("          *   *")
print("         *     *")
print("        *       *")
print("       *         *")
print("      *           *")
print("     *             *")
print("    ******     ******")
print("         *     *")
print("         *     *")
print("         *     *")
print("         *     *")
print("         *     *")
print("         *     *")
print("         *******")

print("Mi\nnombre\nes\nBond.", end=" ")
print("James Bond.")
print("fish", "chips", sep="&")
print(0o123,"octal") 
print(0x123,"hexadecimal")
print('Me gusta "Monty Python"')
print(+2)
print(-3 ** 2) 
print(-2 ** 3) 
print(-(3 ** 2))
print()
kilometers = 12.25
miles = 7.38
miles_to_kilometers = miles*1.61
kilometers_to_miles = kilometers/1.61
print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")
print()
x = -1
x = float(x)
y = 3*x**3 - 2*x**2 + 3*x - 1
print("y =", y)
j = 6
p = 3
j /= 2 * p
print(j)
anything = input("Dime lo que sea...")
print("Hmm...", anything, "...¿en serio?")
print()
x = float(input("Ingresa el valor para x: "))
y=float(1/(x+1/(x+1/(x+1/x))))
print("y =", y)
print()
hour = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos) "))
mins = mins + dura # encuentra el número total de minutos
hour = hour + mins // 60 # encuentra el número de horas ocultas en los minutos y actualiza las horas
mins = mins % 60
hour = hour % 24
print(hour, ":", mins, sep='')
######
name = input("Ingrese el nombre de la planta:")

if name=="Espatifilo":
    print("Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!")
elif name=="espatifilo":
    print("No, ¡quiero un gran Espatifilo!")
else:
    print("¡Espatifilo!, ¡No",name +"!")
##
numero = float(input("Introduce el ingreso:"))
Maximo=85528
excedente = numero-Maximo
if numero < Maximo:
    impuesto = (numero * 0.18)- 556.02
else:
    impuesto = 14839.02 + (excedente * 0.32)

if impuesto < 0.0:
    impuesto= 0.0

impuesto = round(impuesto, 0)
print("El impuesto es:", impuesto, "pesos")
####
año=int(input("ingrese el año:"))
if año < 1582:
    print ("no esta dengro del calendario gregoriano")
else:
    if año % 4 != 0:
        print("es un año comun")
    elif año % 100 != 0:
        print("es un año bisiesto")
    elif año % 400 != 0:
        print("es un año comun")
    else:
        print("es un año bisiesto")
######## LISTAS
######## LISTAS
######## LISTAS

hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.
# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
hat_list[2]=int(input("Ingrese un nuevo numero entero:"))
# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
del hat_list[4]
# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print(len(hat_list))
print(hat_list)
########
my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)
########
# paso 1
beatles = []
print("Paso 1:", beatles)
# paso 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Paso 2:", beatles)
# paso 3
for i in range(2):
    beatles.append(input("Ingrese nombre del miembro:"))
print("Paso 3:", beatles)
# paso 4
for i in range(2):
    del beatles[-1]
print("Paso 4:", beatles)
# paso 5
beatles.insert(0,"Ringo Starr")
print("Paso 5:", beatles)
# probando la longitud de la lista
print("Los Fav", len(beatles))
########
my_list = [1, 4, 2, 4, 1, 4, 2, 6, 2, 9]
vacia=[]

for i in my_list:
    if i not in vacia:
        vacia.append(i)
my_list=vacia[:]

print("La lista con elementos únicos:")
print(my_list)
########
#comprension de listas
squares = [x ** 2 for x in range(10)]
print(squares)  #genera una lista de diez elementos y la rellena con cuadrados de diez 
#números enteros que comienzan desde cero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)

odds = [x for x in squares if x % 2 != 0 ]
print(odds)#crea una lista con solo los elementos impares de la lista squares
######
def funcion(n):
    print ("yo recibi", n)
    n+=1
    print("Ahora tengo",n)

var = 1## primero se le asigna el valor
funcion(var)##luego se ejecuta la funcion con el valor de la funcion como argumento
print("pero la variable de afuera tiene",var,)##pero la variable de 
## afuera de la funcion no es reemplazada por el valor de la variable de la funcion.
######