from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def click_button(driver):
    # Clickamos sobre el botón 'See more' hasta que ya no existe
    remaining_data = True
    while remaining_data:
        try:
            verMas = driver.find_element(By.ID, "verMasButton")
            verMas.click()
            sleep(1)
        except NoSuchElementException:
            print(
                "[i] Se ha terminado de clickear el botón 'See more...'. También puede ser que no exista! Asegúrate"
            )
            break
