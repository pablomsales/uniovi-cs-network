from typing import Dict

from unidecode import unidecode


def unify_duplicated_names(name1: str, name2: str) -> str:
    """
    Unifica dos nombres potencialmente duplicados.

    Params:
    -------
    name1 : str
        El primer nombre a ser unificado.

    name2 : str
        El segundo nombre a ser unificado.

    Returns:
    --------
    str
        El nombre unificado, preferentemente seleccionando el más completo y normalizado.
    """

    # quitamos acentos y pasamos a minusculas
    name1 = unidecode(name1.lower())
    name2 = unidecode(name2.lower())
    # splitteamos
    name1 = name1.split(" ")
    name2 = name2.split(" ")

    counter = 0
    for word in name1:
        # nos aseguramos de que el numero de veces que aparece la palabra
        # es el mismo en los dos nombres. Esto es importante en personas
        # cuyos apellidos son el mismo dos veces
        # P. ej: pablo gonzalez gonzalez
        if name1.count(word) == name2.count(word):
            counter += name2.count(word)

    # si todas las palabras de un nombre estan dentro del otro,
    # se asume que es la misma persona
    if counter == min(len(name1), len(name2)):
        name1 = " ".join(name1)
        name1 = name1.title()

        name2 = " ".join(name2)
        name2 = name2.title()

        return name2


def clean_data(
    data: Dict[str, Dict[str, Dict[str, str]]]
) -> Dict[str, Dict[str, Dict[str, str]]]:
    """
    Limpia los datos de tesis, normalizando los nombres de autores y directores.

    Params:
    -------
    data : Dict[str, Dict[str, Dict[str, str]]]
        Un diccionario que contiene la información de las tesis, organizada por año y ID.

    Returns:
    --------
    Dict[str, Dict[str, Dict[str, str]]]
        Un diccionario con los datos limpios, donde los nombres de autores y directores están normalizados y unificados.
    """

    # obtenemos un conjunto con los nombres únicos de directores de tesis
    directors_names_set = set()

    for year in data.keys():
        for id in data[year].keys():
            names = data[year][id]["directors"]
            directors_names_set.update(names)

    # convertimos a lista para poder iterarlo
    directors_names_list = list(directors_names_set)

    # iteramos sobre todos los nombres del json (autores y directores)
    for year in data.keys():
        for id in data[year].keys():
            # procesamos autor
            author = data[year][id]["author"]
            author = unidecode(author)  # eliminamos acentos

            # si el autor tiene una coma, le damos la vuelta al nombre
            if "," in author:
                author = author.split(",")
                author.reverse()
                author = list(map(lambda name: name.strip(), author))
                author = " ".join(author)

            # guardamos el nombre procesado
            data[year][id]["author"] = author.title()

            # para los directores, comprobar si su nombre aparece mas de una vez
            # y quedarnos con un formato de nombre unificado
            for director in directors_names_list:
                result_name = unify_duplicated_names(author, director)
                if result_name:
                    data[year][id]["author"] = result_name

    return data
