from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def set_driver_options() -> Options:
    """
    Configura las opciones del controlador WebDriver.

    Returns:
    --------
    Options
        Un objeto Options configurado con las opciones deseadas.
    """

    options = Options()
    # agregamos user-agent para evitar que detecte el programa como bot
    options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    )
    options.add_argument("--headless")  # si queremos que el proceso ocurra en 2o plano
    return options


def init_driver(options: Options, chromedriver_path: str) -> webdriver.Chrome:
    """
    Inicializa el controlador WebDriver con las opciones y la ubicación del archivo del controlador especificados.

    Params:
    -------
    options : Options
        Objeto Options configurado con las opciones deseadas.

    chromedriver_path : str
        La ruta al archivo ejecutable de chromedriver.

    Returns:
    --------
    webdriver.Chrome
        Un objeto Chrome WebDriver inicializado con las opciones y la ubicación del archivo del controlador especificados.
    """

    # instanciamos webdriver
    driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)
    return driver
