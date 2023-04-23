import time

#import geckodriver_autoinstaller
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from allure_commons.types import AttachmentType
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options




class funciones_2_0:
    def __init__(self, driver):
        self.driver = driver

    ############################################################################################
    ################################## Navegador ###############################################
    ############################################################################################
    def driver_Firefox(self):
        self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        # options = Options()
        # options.headless = True
        #
        # self.driver = webdriver.Firefox(options=options)



    def driver_Chrome(self):
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


    ############################################################################################
    ################################## element_to_be_clickable##################################
    ############################################################################################

    def browser(self, link):
        try:
            self.driver.get(link)
            self.driver.maximize_window()
            print("Página abierta: " + str(link))
        except Exception as ex:
            print(ex)
            print("No se Ejecuto el Navegador")

    def input_Texto(self, tipo, selector, texto):
        try:
            WebDriverWait(self.driver, timeout=5).until(EC.element_to_be_clickable((tipo, selector))).send_keys(texto)
            time.sleep(1)
            print("\n Escribir en el campo {} el texto -> {} ".format(selector, texto))
        except Exception as ex:
            print(ex)
            print(f"No se Completa el campo {selector}")

    def click_Field(self, tipo, selector):
        try:
            WebDriverWait(self.driver, timeout=5).until(EC.element_to_be_clickable((tipo, selector))).click()
            time.sleep(2)
            print("\n Click sobre el elemento -> {} ".format(selector))
        except Exception as ex:
            print(ex)
            print(f"No se Encontro el Elemento {selector}")

    def clear_Field(self, tipo, selector):
        try:
            WebDriverWait(self.driver, timeout=5).until(EC.element_to_be_clickable((tipo, selector))).clear()
            print("\n Texto eliminado -> {} ".format(selector))
        except Exception as ex:
            print(ex)
            print("Texto no se pudo eliminar" + selector)

    def validates(self, tipo, selector):
        try:
            element = WebDriverWait(self.driver, timeout=5).until(EC.presence_of_element_located((tipo, selector))).text
            print(element)
            print("\n Elemento Validado -> {} ".format(selector))
        except Exception as ex:
            print(ex)
            print("\n No se pudo validar el Elemento -> {} ".format(selector))

    def subirArchivo(self, tipo, selector, ruta):
        try:
            val = self.driver.find_element(tipo, selector)
            val.send_keys(ruta)
            print("\n Elemento Cargado -> {} ".format(selector))
        except Exception as ex:
            print(ex)
            print(f"No se pudo subir el archivo {ruta}")

    def scrollToElement(self, tipo, elemento):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((tipo, elemento)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            print("\n Desplazando al elemento -> {} ".format(elemento))
        except Exception as ex:
            print(ex)
            print(f"No se pudo desplazar al elemento {elemento}")

        ###################################################################################

    ########################## Allure-Report ##########################################
    ###################################################################################

    def screenShot(self, nombre):
        allure.attach(self.driver.get_screenshot_as_png(), name=nombre, attachment_type=AttachmentType.PNG)

    ###################################################################################
    ########################## ACTION CHAINS ##########################################
    ###################################################################################

    def input_Texto_ActionChains(self, tipo, selector, texto):
        action = ActionChains(self.driver)
        try:
            val = self.driver.find_element(tipo, selector, texto)
            action.click(val).perform()
            action.send_keys(texto).perform()
            time.sleep(1)
        except Exception as ex:
            print(ex)
            print(f"No se Completa el campo {selector}")

    def clickAction(self, tipo, selector):
        action = ActionChains(self.driver)
        try:
            val = self.driver.find_element(tipo, selector)
            action.click(val).perform()
            time.sleep(1)
        except Exception as ex:
            print(ex)
            print(f"No se Completa el campo {selector}")

    def key_Up_Key_Down(self, tecla):
        action = ActionChains(self.driver)
        try:
            action.key_down(tecla).perform()
            action.key_up(tecla).perform()
            time.sleep(1)
        except Exception as ex:
            print(ex)

    ############################################################################################
    ############################ visibility_of_element_located #################################
    ############################################################################################

    def input_Texto_visibility(self, tipo, selector, texto):
        try:
            WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((tipo, selector))).send_keys(
                texto)
            time.sleep(1)
            print("\n Escribir en el campo {} el texto -> {} ".format(selector, texto))
        except Exception as ex:
            print(ex)
            print(f"No se Completa el campo {selector}")

    def click_Field_visibility(self, tipo, selector):
        try:
            WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((tipo, selector))).click()
            time.sleep(2)
            print("\n Click sobre el elemento -> {} ".format(selector))
        except Exception as ex:
            print(ex)
            print(f"No se Encontro el Elemento {selector}")

    def clear_Field_visibility(self, tipo, selector):
        try:
            WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((tipo, selector))).clear()
            print("\n Texto eliminado -> {} ".format(selector))
        except Exception as ex:
            print(ex)
            print("Texto no se pudo eliminar" + selector)

    def validates_visibility(self, tipo, selector):
        try:
            element = WebDriverWait(self.driver, timeout=5).until(
                EC.visibility_of_element_located((tipo, selector))).text
            print(element)
            print("\n Elemento Validado -> {} ".format(selector))
        except Exception as ex:
            print(ex)
            print("\n No se pudo validar el Elemento -> {} ".format(selector))

    def subirArchivo_visibility(self, tipo, selector, ruta):
        try:
            val = self.driver.find_element(tipo, selector)
            val.send_keys(ruta)
            print("\n Elemento Cargado -> {} ".format(selector))
        except Exception as ex:
            print(ex)
            print(f"No se pudo subir el archivo {ruta}")

    def scrollToElement_visibility(self, tipo, elemento):
        try:
            val = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((tipo, elemento)))
            self.driver.execute_script("arguments[0].scrollIntoView();", val)
            print("\n Desplazando al elemento -> {} ".format(elemento))
        except Exception as ex:
            print(ex)
            print(f"No se pudo desplazar al elemento {elemento}")
