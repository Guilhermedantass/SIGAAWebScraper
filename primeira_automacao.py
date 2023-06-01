from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SIGAAWebScraper:
    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option("detach", True)
        self.navegador = webdriver.Chrome(options=self.options)

    def fazer_login(self, username, password):
        self.navegador.get("https://sigaa.ufrn.br/sigaa")
        elem_username = self.navegador.find_element(By.NAME, "username")
        elem_username.clear()
        elem_username.send_keys(username)
        elem_password = self.navegador.find_element(By.NAME, "password")
        elem_password.clear()
        elem_password.send_keys(password)
        elem_password.send_keys(Keys.RETURN)

    def acessar_pagina_nota(self):
        elem_menu_discente = self.navegador.find_element(By.XPATH, '//*[@id="menu_form_menu_discente_j_id_jsp_340461267_98_menu"]/table/tbody/tr/td[1]')
        elem_menu_discente.click()
        elem_cm_submenu = self.navegador.find_element(By.XPATH, '//*[@id="cmSubMenuID1"]/table/tbody/tr[1]/td[2]')
        elem_cm_submenu.click()

    def obter_nota(self):
        elem_nota = self.navegador.find_element(By.XPATH, '//*[@id="relatorio"]/div/table/tbody').text
        return elem_nota

    def fechar_navegador(self):
        self.navegador.quit()


# Exemplo de uso da classe SIGAAWebScraper
scraper = SIGAAWebScraper()
scraper.fazer_login("", "")
scraper.acessar_pagina_nota()
nota = scraper.obter_nota()
print(nota)
scraper.fechar_navegador()
