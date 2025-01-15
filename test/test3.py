from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import unittest
import time

# Configurar opciones para el navegador Chrome
options = Options()
options.add_argument('--headless') # Ejecuta Chrome en modo headless
options.add_argument('--no-sandbox') # Recomendado en entornos de CI como GitHub Actions
options.add_argument('--disable-dev-shm-usage') # Ayuda a evitar algunos errores en contenedores

class eis_test(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome(options=options)

	def test_load(self):
		browser = self.browser
		browser.get("https://www.tucarro.com.co/")
		time.sleep(2)
		browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/button').click()
		carrusel = browser.find_elements(By.CSS_SELECTOR, ".andes-carousel-snapped__slide")
		self.assertGreater(len(carrusel),4)	
		
		
	def tearDown(self):
		self.browser.quit()

if __name__ == '__main__':
	unittest.main()