
# %% Accion

class Accion:
    def __init__ (self, nombre):
        self.nombre = nombre
    
    def __str__ (self):
        return self.nombre
    
# %% Estado

class Estado:
    def __init__ (self, nombre, acciones):
        self.acciones = acciones
        self.nombre = nombre
    def __str__ (self):
        return self.nombre


# %% Problema

class problema:
    def __init__(self, est_inicial, est_objetivo, acciones, costes=None, heuristicas=None):
        self.est_inicial = est_inicial
        self.est_objetivo = est_objetivo
        self.acciones = acciones
        self.heuristicas = heuristicas
        self.costes = costes if costes is not None else {}
        self.infinito = 99999

        if not self.costes:
            for estado_inicial in self.acciones.keys():
                self.costes[estado_inicial] = {}
                for accion in self.acciones[estado_inicial].keys():
                    self.costes[estado_inicial][accion] = 1

        if not self.heuristicas:
            self.heuristicas = {}
            for estado_inicial in self.acciones.keys():
                self.heuristicas[estado_inicial] = {}
                for objetivo in self.est_objetivo:
                    self.heuristicas[estado_inicial][objetivo] = self.infinito

    def __str__(self):
        msg = "Estado inicial: {0} -> objetivo: {1}"
        return msg.format(self.est_inicial, self.est_objetivo)

    def es_obj(self, estado):
        return estado in self.est_objetivo

    def resultado(self, estado, accion):
        if estado.nombre not in self.acciones:
            return None
        acciones_estado = self.acciones[estado.nombre]
        if accion.nombre not in acciones_estado:
            return None
        return acciones_estado[accion.nombre]

    def coste_accion(self, estado, accion):
        if estado.nombre not in self.costes:
            return self.infinito
        costes_estado = self.costes[estado.nombre]
        if accion.nombre not in costes_estado:
            return self.infinito
        return costes_estado[accion.nombre]

    def coste_camino(self, nodo):
        total = 0
        while nodo.padre:
            total += self.coste_accion(nodo.padre.estado, nodo.accion)
            nodo = nodo.padre
        return total
        
class Nodo: 
    def __init__(self, estado, accion=None, acciones=None, padre=None):
        self.estado = estado
        self.accion = accion
        self.acciones = acciones
        self.padre = padre
        self.hijos = []
        self.coste = 0
        self.heuristicas = {}
        self.valores = {}
    

    def __str__(self):
        return self.estado.nombre 
    
    def expandir(self, problema):
        self.hijos = []
        if not self.acciones:
            if self.estado.nombre not in problema.acciones.keys():
                return self.hijos
            self.acciones = problema.acciones[self.estado.nombre]  
        
        for accion in self.acciones.keys():
            accion_hijo = Accion(accion)
            nuevo_estado = problema.resultado(self.estado, accion_hijo)
            # Verificar si nuevo_estado es None antes de proceder
            if nuevo_estado is None:
                continue
            acciones_nuevo = {}
            if nuevo_estado.nombre in problema.acciones.keys():
                acciones_nuevo = problema.acciones[nuevo_estado.nombre]
            
            # Corrige 'acciones_hijo' a 'accion_hijo'
            hijo = Nodo(nuevo_estado, accion_hijo, acciones_nuevo, self)
            coste = self.padre.coste if self.padre else 0
            coste == problema.coste_accion(self.estado, accion_hijo)
            self.hijos.append(hijo)
        return self.hijos
    
    def hijo_menor(self, problema):
        if not self.hijos:
            return None
        mejor = self.hijos[0]
        for hijo in self.hijos:
            for objetivo in problema.es_obj:
                coste_camino_hijo = problema.coste_camino(hijo)
                coste_camino_mejor = problema.coste_camino(mejor)
                if (coste_camino_hijo < coste_camino_mejor):
                    mejor = hijo  
        return mejor