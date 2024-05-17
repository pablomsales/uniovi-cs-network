import json
from typing import Dict

from .clean_data import clean_data
from .click_button import click_button
from .config import init_driver, set_driver_options
from .extract_data import extract_data


def save_thesis_json(filename: str) -> None:
    """
    Extrae datos de tesis de un sitio web, limpia los datos y los guarda en un archivo JSON.

    Params:
    -------
    filename : str
        El nombre del archivo JSON en el que se guardarán los datos.

    Returns:
    --------
    None
    """

    # path to chromedriver
    chromedriver_path = "/usr/bin/chromedriver"

    options = set_driver_options()
    driver = init_driver(options, chromedriver_path)

    driver.get("https://portalinvestigacion.uniovi.es/unidades/6069/tesis")
    click_button(driver)

    data = extract_data(driver)
    data = clean_data(data)

    # guardamos el json
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json.dumps(data, indent=4, ensure_ascii=False))

    print("[INFO] json exportado correctamente")


def load_thesis_json(path: str) -> Dict[str, Dict[str, Dict[str, str]]]:
    """
    Carga los datos de tesis desde un archivo JSON.

    Params:
    -------
    path : str
        La ruta al archivo JSON que contiene los datos de las tesis.

    Returns:
    --------
    Dict[str, Dict[str, Dict[str, str]]]
        Un diccionario que contiene la información de las tesis, organizada por año y ID.
        El primer nivel de claves corresponde a los años, el segundo nivel corresponde a los IDs de las tesis,
        y el tercer nivel corresponde a los atributos de cada tesis (title, author, directors).
    """

    with open(path, "r") as f:
        data = json.load(f)
    return data
