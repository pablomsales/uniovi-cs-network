from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def click_button(driver):
    """
    Haz clic en el botón 'See more' hasta que ya no exista.

    Params:
    -------
    driver : WebDriver
        El controlador WebDriver para interactuar con la página web.

    Returns:
    --------
    None
    """

    # Clickamos sobre el botón 'See more' hasta que ya no existe
    remaining_data = True
    while remaining_data:
        try:
            verMas = driver.find_element(By.ID, "verMasButton")
            verMas.click()
            sleep(1)
        except NoSuchElementException:
            print(
                "[INFO] Se ha completado el proceso de clic en el botón 'See more'. Es posible que el botón ya no exista."
            )
            break
