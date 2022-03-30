'''
    Función que calcula la distancia entre dos coordenadas polares.
    Para notaciones de E/W, N/S, utilizar valores positivos y negativos, respectivamente.
    Esta función utiliza la fórmula de Haversine, la cual contiene un leve margen de error
    que se agrava con distancias demasiado grandes,dado que considera la tierra como una 
    esfera en vez de un elipse. Usar con discreción.

    Author: Mateo Battilana.
    Created: 14/03/2022
    Modified: 17/03/2020
'''

from math import sin, cos, sqrt, atan2, radians


def dist_calc(lat1: float, lon1: float, lat2: float, lon2: float):

    # Checking for correct values
    args = [lat1, lon1, lat2, lon2]
    for v in args:
        if type(v) not in [int, float]:
            raise TypeError("The values must be of type [int] or [float] in degrees.")
    for v in args:
        if v < -90.0 or v > 90.0:
            raise ValueError("Polar coordinates cannot be higher than 90º nor lower than -90º")
    
    # Converting angle coordinates to radians for calculation
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    r = 6373.0  # Approximate earth radius in km

    # Calculating the difference between both locations
    dlon = lon2 - lon1
    dlat = lat2 - lat1

    # Calculating orthodromic distance using Haversine Formula
    a = (sin(dlat / 2)) ** 2 + cos(lat1) * cos(lat2) * (sin(dlon / 2)) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = r * c    # Apply earth radius
    return distance     # In km
