from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Inicializa el driver de Chrome con las opciones especificadas
driver = webdriver.Chrome(options=chrome_options)

# Abre la página web
driver.get("https://resultadostyt.icfes.gov.co/login")








# Espera hasta que el iFrame del CAPTCHA esté disponible y cambia a él
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe")))

# Encuentra el elemento del CAPTCHA y espera hasta que sea clickeable
captcha_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]')))

# Hace clic en el elemento del CAPTCHA
captcha_element.click()
