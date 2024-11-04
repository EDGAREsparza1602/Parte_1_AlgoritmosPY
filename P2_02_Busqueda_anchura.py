# Importamos las clases necesarias del módulo `grafos`.
from grafos import Accion 
from grafos import Estado
from grafos import Nodo
from grafos import problema

def anchura(problema):
    raiz = crea_nodo_raiz(problema)
    if problema.es_obj(raiz.estado):
        return raiz
    frontera = [raiz]
    explorados = set()
    
    while True:
        if not frontera:
            return None 
        nodo = frontera.pop(0)
        explorados.add(nodo.estado)
        
        for accion_nombre, accion_estado in problema.acciones.get(nodo.estado.nombre, {}).items():
            accion = Accion(accion_nombre)
            hijo = crea_nodo_hijo(problema, nodo, accion)
            estado_frontera = [nodo.estado for nodo in frontera]
            
            if hijo.estado not in explorados and hijo.estado not in estado_frontera:
                if problema.es_obj(hijo.estado):
                    return hijo
                frontera.append(hijo)

def crea_nodo_raiz(problema):
    estado_raiz = problema.est_inicial
    acciones_raiz = problema.acciones.get(estado_raiz.nombre, {})
    raiz = Nodo(estado_raiz, None, acciones_raiz, None)
    return raiz

def crea_nodo_hijo(problema, padre, accion):
    nuevo_estado = problema.resultado(padre.estado, accion)
    acciones_nuevo = problema.acciones.get(nuevo_estado.nombre, {})
    hijo = Nodo(nuevo_estado, accion, acciones_nuevo, padre)
    padre.hijos.append(hijo)
    return hijo

def muestra_solucion(objetivo=None):
    if not objetivo:
        print("No hay solución")
        return
    nodo = objetivo
    while nodo:
        print(f"Estado: {nodo.estado.nombre}")
        if nodo.accion:
            print(f"<--- {nodo.accion.nombre} ----")
        nodo = nodo.padre

# Definir los sentidos posibles de las acciones.
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
acciones = {
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

objetivo_1 = [sinaloa]
problema_1 = problema(cdmx, objetivo_1, acciones)

# Resolver el problema de búsqueda en anchura y mostrar la solución.
solucion = anchura(problema_1)
muestra_solucion(solucion)