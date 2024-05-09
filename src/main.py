import os

from scrapper.json_generator import load_thesis_json, save_thesis_json


def main():
    # hacemos el scrapping si no tenemos los datos
    if not os.path.exists("thesis.json"):
        save_thesis_json()

    # cargamos los datos
    data = load_thesis_json("thesis.json")


if __name__ == "__main__":
    main()
