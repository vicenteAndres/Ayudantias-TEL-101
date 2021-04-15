Te = 600 
Galletas = 300
Sandwich = 800

cantidadTe = int(input("Ingrese la cantidad de té: "))
cantidadGalletas = int(input("Ingrese la cantidad de galletas: "))
cantidadSandwich = int(input("Ingrese la cantidad de Sandwich: "))

nombre = input("Ingrese su nombre: \n")

valorTotal = (Te*cantidadTe)+(Galletas*cantidadGalletas)+(Sandwich*cantidadSandwich)

montoPago = int(input("Ingrese con cuanto va a pagar: "))

print("Generando boleta:")

print("-"*10)


print("Kiosko Python")

print("Cliente ", nombre)

print("Té ", cantidadTe, " x ", Te)
print("Galletas ", cantidadGalletas, " x ", Galletas)
print("Sandwich ", cantidadSandwich, " x ", Sandwich)

print("Su pago", valorTotal)

print("Su monto",montoPago)

print("Su vuelto es: ", (montoPago-valorTotal))

