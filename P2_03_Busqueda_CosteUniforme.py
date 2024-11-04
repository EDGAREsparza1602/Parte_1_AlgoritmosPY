from grafos import Accion 
from grafos import Estado
from grafos import Nodo
from grafos import problema

def coste_uniforme(problema):
    raiz = crea_nodo_raiz(problema)
    frontera = [raiz]
    explorados = set()
 
    while True:
        if not frontera:
            return None 
        nodo = frontera.pop(0)
        if problema.es_obj(nodo.estado): 
            return nodo
        explorados.add(nodo.estado) 
        for accion_nombre, accion_estado in problema.acciones.get(nodo.estado.nombre, {}).items():
            accion = Accion(accion_nombre)
            hijo = crea_nodo_hijo(problema, nodo, accion)
            estado_frontera = [nodo.estado for nodo in frontera]
            
            if hijo.estado not in explorados and hijo.estado not in estado_frontera:
                if problema.es_obj(hijo.estado):
                    return hijo
                frontera.append(hijo)
            else: 
                buscar = [nodo for nodo in frontera 
                    if nodo.estado == hijo.estado]
                if buscar:
                    if hijo.coste < buscar[0].coste:
                        indice = frontera.index(buscar[0])
                        frontera[indice] = hijo
            frontera.sort(key=lambda nodo: nodo.coste)
            
def crea_nodo_raiz(problema):
    estado_raiz = problema.est_inicial
    acciones_raiz = problema.acciones.get(estado_raiz.nombre, {})
    raiz = Nodo(estado_raiz, None, acciones_raiz, None)
    raiz.coste = 0
    return raiz

def crea_nodo_hijo(problema, padre, accion):
    nuevo_estado = problema.resultado(padre.estado, accion)
    acciones_nuevo = problema.acciones.get(nuevo_estado.nombre, {})
    hijo = Nodo(nuevo_estado, accion, acciones_nuevo, padre)
    coste = padre.coste
    coste += problema.coste_accion(padre.estado, accion)
    hijo.coste = coste 
    padre.hijos.append(hijo)
    return hijo

def muestra_solucion(objetivo=None):
    if not objetivo:
        print("No hay solución")
        return
    nodo = objetivo
    while nodo:
        msg = "Estado: {0} \n Coste total: {1}"
        estado = nodo.estado.nombre
        coste_total = nodo.coste 
        print(msg.format(estado, coste_total))
        if nodo.accion:
            accion = nodo.accion.nombre
            padre = nodo.padre.estado
            coste = problema_resolver.coste_accion(padre, nodo.accion)
            print(f"<--- {accion, coste} ----")
        nodo = nodo.padre

# Crear los estados con conexiones aproximadas de acuerdo a la ubicación geográfica
# Definir los sentidos posibles de las acciones.
if __name__ == '__main__':
    acN = Accion('norte')
    acS = Accion('Sur')
    acE = Accion('Este')
    acO = Accion('Oeste')

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

costes = {
    'Aguascalientes': {'Norte': 113, 'Sur': 220},  # Zacatecas: 113 km, Jalisco: 220 km
    'Baja California': {'Sur': 1483, 'Este': 897},  # Baja California Sur: 1483 km, Sonora: 897 km
    'Baja California Sur': {'Norte': 1483},  # Baja California: 1483 km
    'Campeche': {'Norte': 380, 'Oeste': 177, 'Este': 489},  # Yucatán: 380 km, Tabasco: 177 km, Quintana Roo: 489 km
    'Ciudad de Mexico': {'Norte': 60, 'Sur': 90, 'Este': 135, 'Oeste': 120},  # Edo. Mex: 60 km, Morelos: 90 km, Puebla: 135 km, Michoacán: 120 km
    'Coahuila': {'Norte': 565, 'Sur': 413, 'Este': 300},  # Chihuahua: 565 km, Zacatecas: 413 km, Nuevo León: 300 km
    'Colima': {'Norte': 217},  # Jalisco: 217 km
    'Chiapas': {'Norte': 241, 'Este': 155},  # Oaxaca: 241 km, Tabasco: 155 km
    'Chihuahua': {'Sur': 625, 'Este': 350},  # Durango: 625 km, Coahuila: 350 km
    'Durango': {'Norte': 625, 'Sur': 361, 'Este': 310, 'Oeste': 218},  # Chihuahua: 625 km, Zacatecas: 361 km, Coahuila: 310 km, Sinaloa: 218 km
    'Guanajuato': {'Norte': 171, 'Sur': 115, 'Este': 67},  # San Luis Potosí: 171 km, Michoacán: 115 km, Querétaro: 67 km
    'Guerrero': {'Norte': 209, 'Este': 233},  # Michoacán: 209 km, Oaxaca: 233 km
    'Hidalgo': {'Norte': 162, 'Sur': 63, 'Este': 134},  # San Luis Potosí: 162 km, Edo. Mex: 63 km, Veracruz: 134 km
    'Jalisco': {'Norte': 401, 'Sur': 217, 'Este': 220, 'Oeste': 188},  # Zacatecas: 401 km, Colima: 217 km, Aguascalientes: 220 km, Nayarit: 188 km
    'Estado de Mexico': {'Norte': 63, 'Sur': 60, 'Este': 135, 'Oeste': 120},  # Hidalgo: 63 km, CDMX: 60 km, Puebla: 135 km, Michoacán: 120 km
    'Michoacan': {'Norte': 115, 'Sur': 209, 'Este': 120, 'Oeste': 217},  # Guanajuato: 115 km, Guerrero: 209 km, Edo. Mex: 120 km, Jalisco: 217 km
    'Morelos': {'Norte': 90, 'Sur': 233},  # CDMX: 90 km, Guerrero: 233 km
    'Nayarit': {'Sur': 188, 'Este': 283},  # Jalisco: 188 km, Durango: 283 km
    'Nuevo Leon': {'Norte': 300, 'Sur': 340},  # Coahuila: 300 km, Tamaulipas: 340 km
    'Oaxaca': {'Norte': 339, 'Sur': 217, 'Oeste': 233, 'Este': 277},  # Puebla: 339 km, Chiapas: 217 km, Guerrero: 233 km, Veracruz: 277 km
    'Puebla': {'Norte': 31, 'Sur': 339, 'Este': 231, 'Oeste': 135},  # Tlaxcala: 31 km, Oaxaca: 339 km, Veracruz: 231 km, Edo. Mex: 135 km
    'Queretaro': {'Norte': 67, 'Sur': 200, 'Este': 80},  # San Luis Potosí: 67 km, CDMX: 200 km, Hidalgo: 80 km
    'Quintana Roo': {'Oeste': 489, 'Norte': 318},  # Campeche: 489 km, Yucatán: 318 km
    'San Luis Potosí': {'Norte': 413, 'Sur': 171, 'Este': 271, 'Oeste': 230},  # Zacatecas: 413 km, Querétaro: 171 km, Veracruz: 271 km, Guanajuato: 230 km
    'Sinaloa': {'Sur': 218, 'Norte': 500},  # Nayarit: 218 km, Sonora: 500 km
    'Sonora': {'Sur': 500, 'Norte': 897},  # Sinaloa: 500 km, Baja California: 897 km
    'Tabasco': {'Norte': 177, 'Oeste': 317, 'Este': 155},  # Campeche: 177 km, Veracruz: 317 km, Chiapas: 155 km
    'Tamaulipas': {'Norte': 340, 'Sur': 310},  # Nuevo León: 340 km, Veracruz: 310 km
    'Tlaxcala': {'Norte': 134, 'Sur': 31},  # Hidalgo: 134 km, Puebla: 31 km
    'Veracruz': {'Norte': 310, 'Sur': 277, 'Oeste': 134, 'Este': 317},  # Tamaulipas: 310 km, Oaxaca: 277 km, Hidalgo: 134 km, Tabasco: 317 km
    'Yucatan': {'Sur': 380, 'Este': 318},  # Campeche: 380 km, Quintana Roo: 318 km
    'Zacatecas': {'Norte': 565, 'Sur': 361, 'Este': 113, 'Oeste': 413}  # Coahuila: 565 km, San Luis Potosí: 361 km, Aguascalientes: 113 km, Durango: 413 km
}

objetivo_1 = [sinaloa]
problema_1 = problema(cdmx, objetivo_1, acciones, costes)

objetivo_2 = [quintana_roo]
problema_2 = problema(sinaloa, objetivo_2, acciones, costes)

problema_resolver = problema_2
# Resolver el problema de búsqueda en anchura y mostrar la solución.
solucion = coste_uniforme(problema_resolver)
muestra_solucion(solucion)