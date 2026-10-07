# ==========================================
# EJERCICIOS Y EJEMPLOS DE PYTHON
# Arath Valenzuela
# (NC:0148)
# ==========================================

# ------------------------------------------
# 1. PYTHON CONDITIONS (if)
# Ref: https://www.w3schools.com/python/python_conditions.asp
# (NC:0148)
# ------------------------------------------

# Ejemplo 1.1: Comparación simple entre dos variables
a = 33
b = 200
if b > a:
    print("[1.1] b es mayor que a")

# Ejemplo 1.2: Evaluar si un número es positivo
numero = 15
if numero > 0:
    print("[1.2] El número es positivo")


# ------------------------------------------
# 2. PYTHON IF ... ELIF
# Ref: https://www.w3schools.com/python/python_if_elif.asp
# (NC:0148)
# ------------------------------------------

# Ejemplo 2.1: Evaluar igualdad si la primera condición no se cumple
a = 33
b = 33
if b > a:
    print("[2.1] b es mayor que a")
elif a == b:
    print("[2.1] a y b son iguales")

# Ejemplo 2.2: Clasificación de notas por rangos
score = 75
if score >= 90:
    print("[2.2] Calificación: A")
elif score >= 80:
    print("[2.2] Calificación: B")
elif score >= 70:
    print("[2.2] Calificación: C")


# ------------------------------------------
# 3. PYTHON IF ... ELSE
# Ref: https://www.w3schools.com/python/python_if_else.asp
# (NC:0148)
# ------------------------------------------

# Ejemplo 3.1: Estructura completa if / elif / else
a = 200
b = 33
if b > a:
    print("[3.1] b es mayor que a")
elif a == b:
    print("[3.1] a y b son iguales")
else:
    print("[3.1] a es mayor que b")

# Ejemplo 3.2: Comprobar si un número es par o impar
numero_evaluar = 7
if numero_evaluar % 2 == 0:
    print("[3.2] El número es par")
else:
    print("[3.2] El número es impar")


# ------------------------------------------
# 4. PYTHON FOR LOOPS
# Ref: https://www.w3schools.com/python/python_for_loops.asp
# (NC:0148)
# ------------------------------------------

# Ejemplo 4.1: Recorrer una lista de elementos
frutas = ["manzana", "banana", "cereza"]
print("[4.1] Lista de frutas:")
for x in frutas:
    print(" -", x)

# Ejemplo 4.2: Uso de range() para iterar un número determinado de veces
print("[4.2] Números del 0 al 4 usando range(5):")
for x in range(5):
    print("  Número:", x)


# ------------------------------------------
# 5. PYTHON WHILE LOOPS
# Ref: https://www.w3schools.com/python/python_while_loops.asp 
# (NC:0148)
# ------------------------------------------

# Ejemplo 5.1: Bucle while básico con incremento 
i = 1
print("[5.1] Conteo con while:")
while i < 6:
    print("  i =", i)
    i += 1

# Ejemplo 5.2: Bucle while usando la instrucción break para salir antes
i = 1
print("[5.2] Conteo interrumpiendo en 3:")
while i < 6:
    print("  i =", i)
    if i == 3:
        break
    i += 1

print("Arath Valenzuela")
print("NC:0148")