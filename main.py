import json
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
# agregamos user-agent para evitar que detecte el programa como bot
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)
# options.add_experimental_option(
#     "detach", True
# )  # si queremos que el navegador no cierre
options.add_argument("--headless")  # si queremos que el proceso ocurra en 2o plano

# instanciamos webdriver
chromedriver_path = "/usr/bin/chromedriver"  # path to chromedriver
driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)

driver.get("https://portalinvestigacion.uniovi.es/unidades/6069/tesis")
# driver.maximize_window()


# Clickeamos sobre el botón 'See more' hasta que ya no existe
remaining_data = True
while remaining_data:
    try:
        verMas = driver.find_element(By.ID, "verMasButton")
        verMas.click()
        sleep(1)
    except NoSuchElementException:
        print(
            "Se ha terminado de clickear el botón 'See more...'. También puede ser que no exista! Asegúrate"
        )
        break

# # obtenemos los autores
# autores = driver.find_elements(By.XPATH, '//p[@class="c-doc__autores"]')
# autores = list(map(lambda autor: autor.text.lower(), autores))  # a minusculas


# años
years_containers = driver.find_elements(
    By.XPATH, '//div[@class="unidad-docs__grupo agrupador-anualidad"]'
)
# init dict que almacenara toda la info
full_dict = dict()

for cont in years_containers:
    # obtenemos el texto del año. Importante el punto inicial en la ruta para que sea relativa
    year = cont.find_element(By.XPATH, './/h3[@class="unidad-docs__grupo-titulo"]')
    year = year.text

    # obtenemos los contenedor de cada tesis
    thesis_containers = cont.find_elements(
        By.XPATH, './/li[@class="unidad-docs__item c-doc c-doc--dirigidas"]'
    )

    # init dict con las tesis del año
    year_thesis_dict = dict()

    for i, thesis in enumerate(thesis_containers, 1):

        # init dict por cada tesis
        thesis_dict = dict()

        # obtenemos titulo, autor y directores del contenedor
        title = thesis.find_element(By.XPATH, './/span[@class="c-doc__titulo"]')
        author = thesis.find_element(By.XPATH, './/p[@class="c-doc__autores"]')
        directors = thesis.find_element(By.XPATH, './/div[@class="c-doc__directores"]')

        sleep(0.0001)
        # obtenemos texto
        title = title.text
        author = author.text.title()
        directors = directors.text.lower()

        # limpiamos el texto de los directores
        directors = directors.strip().replace("dirigida por ", "")
        # si existen varios, dividimos el texto en dos
        directors = directors.split(" y ")
        directors = list(map(lambda x: x.strip(), directors))
        directors = list(map(lambda x: x.title(), directors))

        thesis_dict["title"] = title
        thesis_dict["author"] = author
        thesis_dict["directors"] = directors

        id_thesis = f"{year}-{i}"
        year_thesis_dict[id_thesis] = thesis_dict

    full_dict[year] = year_thesis_dict


with open("thesis.json", "w", encoding="utf-8") as file:
    # ensure_ascii=False para que procese bien los acentos
    file.write(json.dumps(full_dict, indent=4, ensure_ascii=False))

print("json exportado")
