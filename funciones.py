def obtener_existencia( cantidad_de_filas : int, cantidad_de_columnas : int , valor_inicial : any ):
    matriz = []
    for i in range(cantidad_de_filas):
        fila = [valor_inicial] * cantidad_de_columnas
        matriz += [fila]
    return matriz

def mostrar_matriz(matriz : list):
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            print( matriz [i][j], end = " ")
        print(" ")

def estimar_stock(matriz : list , camisetas : list , provincias : list , minimo1 = 10000):

    lista_retorno = ([0] *len(camisetas))
    for i in range(len(matriz)):
        acumulador = 0
        for j in range (len(matriz[i])):
            acumulador += matriz [i][j]
        
        if acumulador < minimo1 :
            pass
        
        else:
            lista_retorno [i] = acumulador
            print(f"esta provincia tiene mas de 10000 camisetas almacenadas :  {provincias[i]}")


def calcular_maximo_de_camisetas(matriz : list , provincias : list , camisetas : list):
    for i in range (len(camisetas)):
        bandera = True
        for j in range (len(provincias)):
            if bandera == True :
              maximo = matriz[j][i]
              documentos = provincias[i]
              bandera == False

            elif matriz [j][i] > maximo:
               maximo = matriz [j][i]
               documentos = provincias[j] 
            else :
               pass
        print(f"el deposito con mas camisetas del {camisetas[i]} es:  {documentos} ")

def calcular_recaudacion(matriz: list, lista_precios: list =[100,100,100,100,100]) -> list:
    lista_retorno = [0] * (len(matriz))

    for i in range (len(matriz)):
        recaudación = 0
        for j in range(len(matriz[i])):
            recaudación += (matriz[i][j] * lista_precios[j])
        lista_retorno = recaudación
    return lista_retorno



def mostrar_traspuesta(matriz):
    traspuesta = []
    for i in range (len(matriz[0])):
        fila_traspuesta = []
        for j in range (len(matriz)):
            fila_traspuesta.append(matriz[j][i])
        traspuesta.append(fila_traspuesta)
    return traspuesta

def suma_de_sus_diagonales(matriz):
    n = len(matriz)
    suma_principal = 0
    suma_secundaria = 0
    for i in range (n):
        suma_principal += matriz [i][i]
        suma_secundaria += matriz [i][n - 1 - i]
    return suma_principal , suma_secundaria