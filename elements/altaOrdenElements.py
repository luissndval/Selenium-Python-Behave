################################### Sales #######################################

salesButton = "//a[@href='#collapse-4'][contains(.,'Sales')]"
ordersButton = "(//a[contains(text(),'Orders')])[1]"
addNewButton = "//a[@aria-label='Add New']"

################################# formularioCustomer #####################################

customerButton = "//strong[text()='Customer']//..//..//..//..//button[@type='button']"
customerInput = "//input[@placeholder='Customer']"
firstNameInput = "//input[contains(@id,'input-firstname')]"
lastNameInput = "//input[@id='input-lastname']"
emailInput = "//input[@id='input-email']"
telephoneInput = "//input[@id='input-telephone']"
confirmCustomerBotton = "//button[@id='button-customer']"
customerValidate = "//div[@class='alert alert-success alert-dismissible']"
exitCustomerButton = "//h5[text()='Customer']//..//button[@class='btn-close']"

############################### selectionProduct #############################

carBuyButton = "//button[@data-bs-target='#modal-cart']"
productInput = "//input[@name='product']"
addProductButton = "//button[@id='button-product-add']"
exitCarButton = "//h5[text()='Add Item']//..//button"

############################### paymentAddress #############################

paymentFirsNameInput = "//input[@id='input-payment-firstname']"
paymentLastNameInput = "//input[@id='input-payment-lastname']"
paymentCompanyInput = "//input[@id='input-payment-company']"
paymentsAddresInput = "//input[@id='input-payment-address-1']"
paymentcityInput = "//input[contains(@id,'input-payment-city')]"
paymentPostCodeInput = "//input[contains(@id,'input-payment-postcode')]"
paymentCountrySelect = "//select[@name='country_id']"
paymentCountryOption = "//option[text()='Argentina']"
paymentZoneSelect = "//select[@id='input-payment-zone']"
paymentCityOption = "//option[text()='Buenos Aires']"
paymentAddresButton = "//button[@id='button-payment-address']"
paymentAlertValidate = "//div[@class='alert alert-success alert-dismissible'][contains(.,'Success: Payment address has been set!')]"
paymentExitButton = "//h5[text()='Payment Address']//..//button[@class='btn-close']"

############################### shippingAddress #############################


shipgButton = "//button[@data-bs-target='#modal-shipping-address']"
shipFirstName = "//input[@id='input-shipping-firstname']"
shipLastName = "//input[@id='input-shipping-lastname']"
shipCustomer = "//input[contains(@id,'input-shipping-company')]"
shipAddres = "//input[@id='input-shipping-address-1']"
shipCity = "//input[@id='input-shipping-city']"
shipPostcode = "//input[@id='input-shipping-postcode']"
shipCountry = "//select[@id='input-shipping-country']"
shipCountryOption = "(//option[@value='10'][normalize-space()='Argentina'])[2]"
shipZone = "//select[@id='input-shipping-zone']"
shipZoneOption = "(//option[@value='156'][normalize-space()='Buenos Aires'])[2]"
shipConfirmAddres = "//button[contains(@id,'button-shipping-address')]"
shipValidates = "//div[@class='alert alert-success alert-dismissible'][contains(.,'Success: Shipping address has been set!')]"
shipButtonClose = "//h5[text()='Shipping Address']//..//button[@class='btn-close']"

############################### shippingMethod #############################

shippingMethod = "//button[@id='button-shipping-method']"
shippingMethodInput = "//select[@id='input-shipping-method']"
shippingOptionMethod="//option[@value='flat.flat']"

############################### PaymentMetho #############################

PaymentMethodButton = "//button[@id='button-payment-method']"
PaymentMethodSelect = "//select[@id='input-payment-method']"
PaymentgOptionMethod = "//option[text()='Cash On Delivery']"

############################### confirmarOrden #############################

confirmOrder = "//button[text()=' Confirm']"

############################### backButton #################################

backButton = "//a[@data-bs-original-title='Back']"

################## click_configuration_payment_addres ######################

addresButtonConfiguration = "//button[@data-bs-target='#modal-payment-address']"

################################## Logut ##################################

logoutButton = "//span[text()='Logout']"
