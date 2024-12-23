# Tenemos un arreglo de tamaño 2n de la forma {C1, C2, C3, … Cn, D1, D2, D3, … Dn}, 
# tal que la cantidad total de elementos del arreglo es potencia de 2 (por ende, n también lo es). 
# Implementar un algoritmo de División y Conquista que modifique el arreglo de tal forma que 
# quede con la forma {C1, D1, C2, D2, C3, D3, …, Cn, Dn}, sin utilizar espacio adicional 
# (obviando el utilizado por la recursividad). Indicar y justificar su complejidad temporal.

# Pista: Pensar primero cómo habría que hacer si el arreglo tuviera 4 elementos ({C1, C2, D1, D2}). 
# Luego, pensar a partir de allí el caso de 8 elementos, etc… para encontrar el patrón.

def alternar(arr):
    return _alternar(arr, 0, len(arr) - 1)

def _alternar(arr, ini, fin):
    if fin - ini < 2:
        return arr

    medio = (ini + fin) // 2

    arr = _alternar(arr, ini, medio)
    arr = _alternar(arr, medio + 1, fin)

    for i in range(1, medio-ini+2, 2):
        arr[ini+i], arr[medio+i] = arr[medio+i], arr[ini+i]
    return arr