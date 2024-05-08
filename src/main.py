from scrapper.json_generator import load_thesis_json, save_thesis_json


def main():
    save_thesis_json()
    data = load_thesis_json("thesis.json")


if __name__ == "__main__":
    main()
