counter = 5
while counter:
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)
####
secret_number=777
number = int(input("Escoja un numero:"))
while number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    number = int(input("Escoja un numero:"))
if number == secret_number:
    print("!Bien echo, eres libre")
##
i = 0
while i < 10:
    # do_something()
    i += 1
    print(i)
###
import time

for i in range(1,6):
    print(i,"mississippi")
    time.sleep(1)
print("¡Listos o no, ahí voy!")
###
largest_number = -99999999
counter = 0

number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))

if counter:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")
###
palabra = input("ingrese una palabra:")

while palabra != "chupacabra":
    if palabra == "chupacabra":
        break
    else:
        palabra = input("ingrese una palabra:")
print("Has dejado el bucle con éxito.")
####
user_word=input("ingrese una palabra:")
user_word = user_word.upper()
word_without_vowels = ""
for letter in user_word:
    ##if (letter== "A" or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U'):
    if letter=="A":
        continue
    elif letter=="E":
        continue
    elif letter=="I":
        continue
    elif letter=="O":
        continue
    elif letter=="U":
        continue
    else:
        word_without_vowels += letter
print(word_without_vowels)
##
c0=int(input("ingrese cualquier número entero que no sea negativo y que no sea cero:"))
pasos=0
while c0 != 1:
    if c0 % 2 == 0:
        c0//=2
        pasos+=1
        print(c0)
    else:
        c0 = 3 * c0 + 1
        pasos+=1
        print(c0)
print("pasos=",pasos)
##

for digit in "0165031806510":
    if digit == "0":
        print("x",end="")
        continue
    print(digit,end="")
    ##
    