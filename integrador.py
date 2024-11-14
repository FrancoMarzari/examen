from  funciones import *


""""Se debe modularizar correctamente, utilizar parámetros opcionales y cumplir reglas de estilo.
No puede haber código repetido, ni funciones que realicen múltiples tareas. No se puede
utilizar sets, diccionarios, ni tuplas.
Una empresa se dedica al almacenamiento y posterior distribución de camisetas de fútbol en
todo el país. Para ello cuentan con 6 depósitos: Tierra del Fuego, Tucumán, Mendoza, Bs
As, Misiones y Santa Fé.
Los depósitos almacenan camisetas de 5 equipos que son las que más se venden:
Barcelona, Inter Miami, PSG, Manchester City y Real Madrid.
Los puntos 2 y 3 deben utilizar la misma función (calcular_totales). La misma debe poder
sumar por filas o por columnas. Además, deberán utilizar la función estimar_stock que recibe
una lista de totales, una lista de strings con el nombre de cada total y reciba por parámetro
cuál es el límite que debe tomar para informar."""

menu1 =\
"""
1. Obtener existencias: para ello deberá generar una función que cargue
secuencialmente, de tal forma que la intersección de cada fila y cada columna
corresponda a la cantidad de camisetas de un equipo en un depósito. Esto es carga
secuencial.
2. Mostrar depósitos que tienen en stock más de 10.000 camisetas.
3. Mostrar equipos que hay en stock más de 5.000 camisetas.|
4. Obtener máxima cantidad de camisetas de cada equipo. Mostrar en qué depósito se
encuentra.
5. Cargar ventas: se deberá poder cargar ventas de un determinado producto para un
determinado depósito. Esto es carga distribuida o aleatoria. Al cargarse las ventas
se deben restar los productos vendidos del stock y generar una matriz con la
recaudación que reciba el listado de precios por parámetro, en caso de no recibir un
listado deberá tener un precio de 100 cada producto. Utilizar parámetro opcional."""
""""""
"""provincias = ["Tierra del Fuego", "Tucumán", "Mendoza", "BsAs", "Misiones","Santa Fé"]

camisetas = ["Barcelona" , "Inter Miami" , "PSG" , "Manchester City" , "Real Madrid"]

matriz_ejercicio1 = [0,0,0,0,0] , [0 , 0, 0 , 0 , 0] , [0,0,0,0,0] , [0,0,0,0,0] ,[0,0,0,0,0]

respuesta = "si"

carga = False

while respuesta == "si":
    menu = input(menu1)

    match menu:
        case "1":
            if carga == False:
                matriz_ejercicio1 = obtener_existencia(len(provincias),len(camisetas),0)

                for i in range(len(provincias)):
                    for j in range(len(camisetas)):

                        cantidad = int(input(f"ingrese la cantidad de {camisetas} en {provincias} "))
                        matriz_ejercicio1[i][j] = cantidad
                carga = True
            else:
                mostrar_matriz(matriz_ejercicio1)
                
        case "2":
            estimar_stock(matriz_ejercicio1 , camisetas , provincias)

        case "3":
            pass
        case "4":
            calcular_maximo_de_camisetas(matriz_ejercicio1 , provincias , camisetas)
        case "5":
            matriz_venta = [[100,100,100,100,100],
                            [100,100,100,100,100],
                            [100,100,100,100,100],
                            [100,100,100,100,100],
                            [100,100,100,100,100]]
            recaudciones = calcular_recaudacion(matriz_venta)
            bandera = True

            for i in range (len(recaudciones)):
                if bandera == True :
                    max_recaudacion = recaudciones[i]
                    max_provincia = provincias[i]
                    bandera = False
                elif recaudciones[i] > max_recaudacion:
                    max_recaudacion = recaudciones[i]
                    max_provincia = provincias[i]
                else:
                    pass
            print(f"{max_provincia}")"""""








matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print ("la matriz sin modificar: ")

for fila in  matriz:
    print(fila)

matriz_traspuesta = mostrar_traspuesta(matriz)
print("la matriz traspuesta es : ")
for fila in matriz_traspuesta:
    print(fila)
suma_principal,suma_secundaria = suma_de_sus_diagonales(matriz)
print(f"la suma principal es :  {suma_principal}")
print(f"la suma secundaria es :  {suma_secundaria}")