
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
    def __init__ (self, est_inicial, est_objetivo, acciones):
        self.est_inicial = est_inicial
        self.est_objetivo = est_objetivo
        self.acciones = acciones
    def __str__(self):
        msg = "Estado inicial: {0} -> objetivo: {1}"
        return msg.format(self.est_inicial, self.est_objetivo)
    def es_obj (self, estado):
        return estado in self.est_objetivo
    
    def resultado(self, estado, accion):
        if estado.nombre not in self.acciones.keys():
            return None
        acciones_estado = self.acciones[estado.nombre]
        if accion.nombre not in acciones_estado.keys():
            return None
        return acciones_estado[accion.nombre]

class Nodo: 
    def __init__(self, estado, accion=None, acciones=None, padre=None):
        self.estado = estado
        self.accion = accion
        self.acciones = acciones
        self.padre = padre
        self.hijos = []
    def __str__(self):
        return self.estado.nombre  # Corrige 'selft' a 'self'
    
    def expandir(self, problema):
        self.hijos = []
        if not self.acciones:
            if self.estado.nombre not in problema.acciones.keys():
                return self.hijos
            self.acciones = problema.acciones[self.estado.nombre]  # Corrige 'self.acciines' a 'self.acciones'
        
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
            self.hijos.append(hijo)
        
        return self.hijos


# Se define los sentidos hacia el cual nos podremos mover. 

if __name__ == '__main__':
    acN = Accion('norte')
    acS = Accion('Sur')
    acE = Accion('Este')
    acO = Accion('Oeste')

# Crear los estados con conexiones aproximadas de acuerdo a la ubicación geográfica

jalisco = Estado('A Jalisco', [acN, acS, acE, acO])
nayarit = Estado('Nayarit', [acS, acE])
zacatecas = Estado('Zacatecas', [acS, acE])
aguascalientes = Estado('Aguascalientes', [acN, acE])
guanajuato = Estado('Guanajuato', [acN, acO])
san_luis_potosi = Estado('San Luis Potosi', [acN, acS, acE])
colima = Estado('Colima', [acN])
michoacan = Estado('Michoacan', [acN, acE, acO])
guerrero = Estado('Guerrero', [acN])
puebla = Estado('Puebla', [acN, acS, acO])
veracruz = Estado('Veracruz' , [acN, acS, acE, acO])
oaxaca = Estado('Oaxaca', [acN, acS])
chiapas = Estado('Chiapas', [acN, acE])
tabasco = Estado('Tabasco', [acN, acO])
yucatan = Estado('Yucatan', [acO])
quintana_roo = Estado('Quintana Roo', [acO])
campeche = Estado('Campeche', [acN, acE, acO])
tlaxcala = Estado('Tlaxcala', [acN, acO])
cdmx = Estado('Ciudad de Mexico', [acS, acO])
edo_mex = Estado('Estado de Mexico', [acN, acS, acE, acO])
morelos = Estado('Morelos', [acN])
queretaro = Estado('Queretaro', [acN, acS, acO])
hidalgo = Estado('Hidalgo', [acN, acS])
nuevo_leon = Estado('Nuevo Leon', [acN, acS])
tamaulipas = Estado('Tamaulipas', [acS])
coahuila = Estado('Coahuila', [acN, acS])
durango = Estado('Durango', [acN, acE])
sinaloa = Estado('Sinaloa', [acN, acS])
sonora = Estado('Sonora', [acN, acS])
chihuahua = Estado('Chihuahua', [acN, acS])
baja_california = Estado('Baja California', [acS])
baja_california_sur = Estado('Baja California Sur', [acN])

# Se crea la accion viajar 
# Se el diccionario con el cual conextamos todos los estados con las acciones antes comentadas
viajar = {
    'Aguascalientes': {'Norte': zacatecas, 'Sur': jalisco},
    'Baja California': {'Sur': baja_california_sur, 'Este': sonora},
    'Baja California Sur': {'Norte': baja_california},
    'Campeche': {'Norte': yucatan, 'Oeste': tabasco, 'Este': quintana_roo},
    'Ciudad de Mexico': {'Norte': edo_mex, 'Sur': morelos, 'Este': puebla, 'Oeste': michoacan},
    'Coahuila': {'Norte': chihuahua, 'Sur': zacatecas, 'Este': nuevo_leon},
    'Colima': {'Norte': jalisco},
    'Chiapas': {'Norte': oaxaca, 'Este': tabasco},
    'Chihuahua': {'Sur': durango, 'Este': coahuila},
    'Durango': {'Norte': chihuahua, 'Sur': zacatecas, 'Este': coahuila, 'Oeste': sinaloa},
    'Guanajuato': {'Norte': san_luis_potosi, 'Sur': michoacan, 'Este': queretaro},
    'Guerrero': {'Norte': michoacan, 'Este': oaxaca},
    'Hidalgo': {'Norte': san_luis_potosi, 'Sur': edo_mex, 'Este': veracruz},
    'Jalisco': {'Norte': zacatecas, 'Sur': colima, 'Este': aguascalientes, 'Oeste': nayarit},
    'Estado de Mexico': {'Norte': hidalgo, 'Sur': cdmx, 'Este': puebla, 'Oeste': michoacan},
    'Michoacan': {'Norte': guanajuato, 'Sur': guerrero, 'Este': edo_mex, 'Oeste': jalisco},
    'Morelos': {'Norte': cdmx, 'Sur': guerrero},
    'Nayarit': {'Sur': jalisco, 'Este': durango},
    'Nuevo Leon': {'Norte': coahuila, 'Sur': tamaulipas},
    'Oaxaca': {'Norte': puebla, 'Sur': chiapas, 'Oeste': guerrero, 'Este': veracruz},
    'Puebla': {'Norte': tlaxcala, 'Sur': oaxaca, 'Este': veracruz, 'Oeste': edo_mex},
    'Queretaro': {'Norte': san_luis_potosi, 'Sur': cdmx, 'Este': hidalgo},
    'Quintana Roo': {'Oeste': campeche, 'Norte': yucatan},
    'San Luis Potosí': {'Norte': zacatecas, 'Sur': queretaro, 'Este': veracruz, 'Oeste': guanajuato},
    'Sinaloa': {'Sur': nayarit, 'Norte': sonora},
    'Sonora': {'Sur': sinaloa, 'Norte': baja_california},
    'Tabasco': {'Norte': campeche, 'Oeste': veracruz, 'Este': chiapas},
    'Tamaulipas': {'Norte': nuevo_leon, 'Sur': veracruz},
    'Tlaxcala': {'Norte': hidalgo, 'Sur': puebla},
    'Veracruz': {'Norte': tamaulipas, 'Sur': oaxaca, 'Oeste': hidalgo, 'Este': tabasco},
    'Yucatan': {'Sur': campeche, 'Este': quintana_roo},
    'Zacatecas': {'Norte': coahuila, 'Sur': san_luis_potosi, 'Este': aguascalientes, 'Oeste': durango}
}

problema_michoacan_bcn = problema(michoacan, [chiapas], viajar)

# Se crea la primer accion que seria estar en jalisco
# Michoacan 
acciones_michoacan = problema_michoacan_bcn.acciones['Michoacan']
nodo_michoacan = Nodo(michoacan, None, acciones_michoacan, None)
hijos_michoacan = nodo_michoacan.expandir(problema_michoacan_bcn)
print("Los destinos cercanos de {0} son: " .format(nodo_michoacan.estado.nombre))
print([hijo.estado.nombre for hijo in hijos_michoacan])
# Guerrero 
sur_guerrero = problema_michoacan_bcn.resultado(michoacan, acS)
print("\n{0}".format(sur_guerrero.nombre))
acciones_guerrero = problema_michoacan_bcn.acciones['Guerrero']
nodo_guerrero = Nodo(guerrero, None, acciones_guerrero, None)
hijos_guerrero = nodo_guerrero.expandir(problema_michoacan_bcn)
print("Los destinos cercanos de {0} son: " .format(nodo_guerrero.estado.nombre))
print([hijo.estado.nombre for hijo in hijos_guerrero])
# Oaxaca 
este_oaxaca = problema_michoacan_bcn.resultado(nodo_guerrero.estado, acE)
print("\n{0}".format(sur_guerrero.nombre))
acciones_oaxaca = problema_michoacan_bcn.acciones['Oaxaca']
nodo_oaxaca = Nodo(oaxaca, None, acciones_oaxaca, None)
fin = problema_michoacan_bcn.es_obj(nodo_oaxaca.estado)
print("Llegamos: {0}".format('Si' if fin else 'No'))
hijos_oaxaca = nodo_oaxaca.expandir(problema_michoacan_bcn)
print("Los destinos cercanos de {0} son: " .format(nodo_oaxaca.estado.nombre))
print([hijo.estado.nombre for hijo in hijos_oaxaca])
# chiapas
sur_chiapas = problema_michoacan_bcn.resultado(nodo_oaxaca.estado, acS)
print("\n{0}".format(este_oaxaca.nombre))
acciones_chiapas = problema_michoacan_bcn.acciones['Chiapas']
nodo_chiapas = Nodo(chiapas, None, acciones_chiapas, None)
fin = problema_michoacan_bcn.es_obj(nodo_chiapas.estado)
print("Llegamos: {0}".format('Si' if fin else 'No'))
hijos_chiapas = nodo_chiapas.expandir(problema_michoacan_bcn)
print("Los destinos cercanos de {0} son: " .format(nodo_chiapas.estado.nombre))
print([hijo.estado.nombre for hijo in hijos_chiapas])