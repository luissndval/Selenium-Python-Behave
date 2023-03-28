import time
from selenium.webdriver.common.by import By
from configuration.config import Datatest
from Funciones.Funciones_2_0 import funciones_2_0
from elements import loginElement

t = 2


class LoginPage(funciones_2_0):

    def __init__(self, driver):
        super().__init__(driver)

    def OpenBrowser(self):
        funciones_2_0.driver_Firefox(self)
        # funciones_2_0.driver_Chrome(self)
        funciones_2_0.browser(self, Datatest.URL)

    def inputUserName(self, Username):
        funciones_2_0.input_Texto(self, By.XPATH, loginElement.usernameInput, Username)

    def inputPassword(self, Password):
        time.sleep(2)
        funciones_2_0.input_Texto(self, By.XPATH, loginElement.passwordInput, Password)
        time.sleep(2)
        # fun.captura_pantalla("Set-Datos")

    def clickLogin(self):
        funciones_2_0.click_Field(self, By.XPATH, loginElement.loginButton)
        time.sleep(1)
        funciones_2_0.click_Field(self, By.XPATH, loginElement.alertClose)
        time.sleep(1)

    def validacionLogin(self):
        # funciones_2_0.Screenshot(self, "Validado")

        funciones_2_0.validates(self, By.XPATH, loginElement.dashboardValidate)
        funciones_2_0.screenShot(self, "Validacion--credencial-invalida")

    def Logout(self):
        funciones_2_0.click_Field(self, By.XPATH, loginElement.logoutButton)
        funciones_2_0.screenShot(self, "name")

    def ValidacionCredencialesIncorrectas(self):
        funciones_2_0.validates(self, By.XPATH, loginElement.alertValidate)
        funciones_2_0.screenShot(self, "Validacion--credencial-invalida")
