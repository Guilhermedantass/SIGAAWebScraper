from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach", True)


navegador = webdriver.Chrome(options=options)

navegador.get("https://sigaa.ufrn.br/sigaa")

elem = navegador.find_element(By.NAME, "username")
elem.clear()
elem.send_keys("guilherme.dantas.702")
elem = navegador.find_element(By.NAME, "password")
elem.clear()
elem.send_keys("Guilherme1911!")
elem.send_keys(Keys.RETURN)
elem = navegador.find_element(By.XPATH, '//*[@id="menu_form_menu_discente_j_id_jsp_340461267_98_menu"]/table/tbody/tr/td[1]')
elem.click()
elem = navegador.find_element(By.XPATH, '//*[@id="cmSubMenuID1"]/table/tbody/tr[1]/td[2]')
elem.click()



