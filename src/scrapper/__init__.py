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
