from time import sleep

from selenium.webdriver.common.by import By
from unidecode import unidecode


def extract_data(driver):
    # obtenemos los contenedores de cada año
    years_containers = driver.find_elements(
        By.XPATH, '//div[@class="unidad-docs__grupo agrupador-anualidad"]'
    )
    # init dict para almacenar toda la info
    full_dict = dict()

    for cont in years_containers:
        # obtenemos el texto del año. Importante el punto inicial en la ruta para que sea relativa
        year = cont.find_element(By.XPATH, './/h3[@class="unidad-docs__grupo-titulo"]')
        year = year.text

        # obtenemos los contenedor de cada tesis
        thesis_containers = cont.find_elements(
            By.XPATH, './/li[@class="unidad-docs__item c-doc c-doc--dirigidas"]'
        )

        # init dict para almacenar todas las tesis del año
        year_thesis_dict = dict()

        for i, thesis in enumerate(thesis_containers, 1):

            # init dict para almacenar la indo de cada tesis
            thesis_dict = dict()

            # obtenemos titulo, autor y directores del contenedor
            title = thesis.find_element(By.XPATH, './/span[@class="c-doc__titulo"]')
            author = thesis.find_element(By.XPATH, './/p[@class="c-doc__autores"]')
            directors = thesis.find_element(
                By.XPATH, './/div[@class="c-doc__directores"]'
            )

            sleep(0.0001)  # sleep para que el driver pueda procesar toda la info

            # obtenemos texto
            title = title.text
            author = author.text
            directors = unidecode(directors.text.lower())

            # limpiamos el texto de los directores
            directors = directors.strip().replace("dirigida por ", "")
            # si existen varios, dividimos el texto en dos
            directors = directors.split(" y ")
            directors = list(map(lambda x: x.strip(), directors))
            directors = list(map(lambda x: x.title(), directors))

            # agregamos la informacion al diccionario de la tesis
            thesis_dict["title"] = title
            thesis_dict["author"] = author
            thesis_dict["directors"] = directors

            # asignamos un id a la tesis y guardamos toda la informacion en el dict de las tesis del año
            id_thesis = f"{year}-{i}"
            year_thesis_dict[id_thesis] = thesis_dict

        # agregamos todas las tesis del año al dict completo
        full_dict[year] = year_thesis_dict

    return full_dict
