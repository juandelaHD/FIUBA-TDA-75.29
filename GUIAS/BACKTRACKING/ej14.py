from graphs_src import grafo

"""
Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, 
tal que para todo vértice de G: o bien (i) pertenece a D; o bien (ii) es adyacente a un vértice en D. 
Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con la mínima cantidad de vértices.
"""

def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()
    sol_optima = set(vertices)
    sol_parcial = set(vertices)
    return list(_dominating_set_min(grafo, list(vertices), 0, sol_parcial, sol_optima))

def _dominating_set_min(grafo, vertices, index, sol_parcial, sol_optima):
    if index == len(vertices):
        return set(sol_parcial) if len(sol_parcial) < len(sol_optima) else sol_optima 

    sol_parcial.remove(vertices[index])

    if es_dominating_set(grafo, sol_parcial):
        sol_optima = _dominating_set_min(grafo, vertices, index+1, sol_parcial, sol_optima)

    sol_parcial.add(vertices[index])
    return _dominating_set_min(grafo, vertices, index+1, sol_parcial, sol_optima)

def es_dominating_set(grafo, sol_parcial):
    visitados = set()
    for v in sol_parcial:
        visitados.add(v)
        for w in grafo.adyacentes(v):
            visitados.add(w)
    for v in grafo.obtener_vertices():
        if v not in visitados:
            return False
    return True
