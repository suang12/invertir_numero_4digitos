

print(".......................................................")
print("............ INVERTIR NUMERO DE 4 DIGITOS .............")
print(".......................................................")

#input

n = int(input("Digite el numero de 4 digitos: "))

#processing
d1 =((n%10)*1000)
pe =((n//10))
d2 =((pe%10)*100)
pe =((pe//10))
d3 =((pe%10)*10)
d4 =(pe//10)
ni =(d1+d2+d3+d4)

#output
print("................................")
print(".......... RESULTADOS ..........")
print("................................")

print("resultado numero invertido: " + str(ni))