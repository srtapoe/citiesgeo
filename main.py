from geopy.distance import great_circle

cidades = ["Nova York", "Los Angeles", "San Diego", "Chicago", "Houston"]

for cidade in cidades:
    print(cidade)

coordenadas_cidades = {
    "Nova York": (40.7128, -74.0060),
    "Los Angeles": (34.0522, -118.2437),
    "San Diego": (32.8153, -117.135),
    "Chicago": (41.881832, -87.623177),
    "Houston": (29.749907, -95.358421),
}


def calcular_distancia(cidade_origem, cidade_destino):
    if cidade_origem in coordenadas_cidades and cidade_destino in coordenadas_cidades:
        origem = coordenadas_cidades[cidade_origem]
        destino = coordenadas_cidades[cidade_destino]
        distancia = great_circle(origem, destino).kilometers
        return distancia
    else:
        return None


for cidade_origem in cidades:
    for cidade_destino in cidades:
        if cidade_origem != cidade_destino:
            distancia = calcular_distancia(cidade_origem, cidade_destino)
            if distancia is not None:
                print(f"A distância entre {cidade_origem} e {cidade_destino} é {distancia} km")
