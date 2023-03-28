import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from Funciones.Funciones_2_0 import funciones_2_0
from elements import altaOrdenElements

t=1




class AltaOrdenPage(funciones_2_0):


    def __init__(self, driver):
        super().__init__(driver)

    def salesClick(self):
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.salesButton)
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.ordersButton)
        time.sleep(t)


    def addNewClick(self):
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.addNewButton)


    def customerButton(self):
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.customerButton)

    def formularioCustomer(self, Customer, FirstName, LastName, Email, Telephone):

        funciones_2_0.input_Texto(self, By.XPATH, altaOrdenElements.customerInput, Customer)
        funciones_2_0.input_Texto(self, By.XPATH, altaOrdenElements.firstNameInput, FirstName)
        funciones_2_0.input_Texto(self, By.XPATH, altaOrdenElements.lastNameInput, LastName)
        funciones_2_0.input_Texto(self, By.XPATH, altaOrdenElements.emailInput, Email)
        funciones_2_0.input_Texto(self, By.XPATH, altaOrdenElements.telephoneInput, Telephone)
        time.sleep(t)

    def saveCustomer(self):
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.confirmCustomerBotton)
        funciones_2_0.validates(self, By.XPATH, altaOrdenElements.customerValidate)
        funciones_2_0.screenShot(self, "Notificacion-Positiva")
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.exitCustomerButton)
        time.sleep(t)

    def selectionProduct(self,Product):
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.carBuyButton)
        time.sleep(t)
        funciones_2_0.click_Field(self,By.XPATH,altaOrdenElements.productInput)
        funciones_2_0.input_Texto(self,By.XPATH,altaOrdenElements.productInput,Product)
        funciones_2_0.key_Up_Key_Down(self,Keys.ARROW_DOWN)
        funciones_2_0.key_Up_Key_Down(self,Keys.ENTER)
        time.sleep(t)
        funciones_2_0.click_Field(self,By.XPATH,altaOrdenElements.addProductButton)
        funciones_2_0.click_Field(self,By.XPATH,altaOrdenElements.exitCarButton)

    def paymentAddress(self, Customer, FirstName, LastName, Address, PostCode, City):
        funciones_2_0.input_Texto(self, By.XPATH,altaOrdenElements.paymentFirsNameInput, FirstName)
        funciones_2_0.input_Texto(self, By.XPATH, altaOrdenElements.paymentLastNameInput, LastName)
        funciones_2_0.input_Texto(self, By.XPATH, altaOrdenElements.paymentCompanyInput, Customer)
        funciones_2_0.input_Texto(self, By.XPATH, altaOrdenElements.paymentsAddresInput, Address)
        funciones_2_0.input_Texto(self, By.XPATH, altaOrdenElements.paymentcityInput, City)
        funciones_2_0.input_Texto(self, By.XPATH, altaOrdenElements.paymentPostCodeInput, PostCode)
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.paymentCountrySelect)
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.paymentCountryOption)
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.paymentZoneSelect)
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.paymentCityOption)
        funciones_2_0.click_Field(self, By.XPATH,altaOrdenElements.paymentAddresButton )
        funciones_2_0.validates(self, By.XPATH,altaOrdenElements.paymentAlertValidate)
        funciones_2_0.screenShot(self, "paymentAddress")
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.paymentExitButton)

    def shippingAddress(self, Customer, FirstName, LastName, Address, PostCode, City):
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.shipgButton)
        funciones_2_0.input_Texto(self, By.XPATH, altaOrdenElements.shipFirstName, FirstName)
        funciones_2_0.input_Texto(self, By.XPATH, altaOrdenElements.shipLastName, LastName)
        funciones_2_0.input_Texto(self, By.XPATH, altaOrdenElements.shipCustomer, Customer)
        funciones_2_0.input_Texto(self, By.XPATH, altaOrdenElements.shipAddres, Address)
        funciones_2_0.input_Texto(self, By.XPATH, altaOrdenElements.shipCity, City)
        funciones_2_0.input_Texto(self, By.XPATH, altaOrdenElements.shipPostcode, PostCode)
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.shipCountry)
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.shipCountryOption)
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.shipZone)
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.shipZoneOption)
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.shipConfirmAddres)
        funciones_2_0.validates(self, By.XPATH,altaOrdenElements.shipValidates)
        funciones_2_0.screenShot(self, "shippingAddress")
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.shipButtonClose)

    def shippingMethod(self):
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.shippingMethod)
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.shippingMethodInput)
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.shippingOptionMethod)
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.PaymentMethodButton)
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.PaymentMethodSelect)
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.PaymentgOptionMethod)
        funciones_2_0.screenShot(self, "shippingMethod")
        time.sleep(1)

    def confirmarOrden(self):
        val0 = WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, altaOrdenElements.confirmOrder)))
        self.driver.execute_script("arguments[0].scrollIntoView();", val0)
        time.sleep(1)
        val0.click()
        time.sleep(1)

    def backButton(self, ):
        val0 = WebDriverWait(self.driver, timeout=5).until(EC.visibility_of_element_located((By.XPATH, altaOrdenElements.backButton)))
        self.driver.execute_script("arguments[0].scrollIntoView();", val0)
        time.sleep(3)
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.backButton)
        time.sleep(2)

    def click_configuration_payment_addres(self, ):
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.addresButtonConfiguration)
        time.sleep(1)

    def logout(self, ):
        funciones_2_0.click_Field(self, By.XPATH, altaOrdenElements.logoutButton)
        time.sleep(2)
