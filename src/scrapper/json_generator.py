import json

from .clean_data import clean_data
from .click_button import click_button
from .config import init_driver, set_driver_options
from .extract_data import extract_data


def save_thesis_json(filename):
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

    print("[i] json exportado correctamente")


def load_thesis_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data
