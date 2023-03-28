from behave import *

from pages.AltaOrdenPage import AltaOrdenPage


#############VERIFICADO###############

@when(u'Se ubica el panel de Navigation y se selecciona la opcion Sales > Orders')
def step_impl(context):
    try:
        AltaOrdenPage.salesClick(context)
    except Exception:
        context.driver.close()
        assert False, " la prueba fallo: Sales_order"


#############VERIFICADO###############
@when(u'Se localiza el boton add new y se realiza click')
def step_impl(context):
    try:
        AltaOrdenPage.addNewClick(context)
    except Exception:
        context.driver.close()
        assert False, "La prueba Fallo en:  add new"


#############VERIFICADO###############
@when(u'Se realiza click sobre el boton de configuracion ubicado en la opcion Customer')
def step_impl(context):
    try:
        AltaOrdenPage.customerButton(context)
    except Exception:
        context.driver.close()
        assert False, "La prueba Fallo en: Configuraciot_customer"


#############VERIFICADO###############
@when(
    u'Se ingresa el nombre del Customer: "{Customer}", se completa el formulario con los datos: FirstName,  "{FirstName}", LastName: "{LastName}", Email: "{Email}",Telephone: "{Telephone}"')
def step_impl(context, Customer, FirstName, LastName, Email, Telephone):
    try:
        AltaOrdenPage.formularioCustomer(context, Customer, FirstName, LastName, Email, Telephone)
    except Exception:
        context.driver.close()
        assert False, "La prueba Fallo en: Formulario"


#############VERIFICADO###############

@when(u'Se realiza click en Save y se valida Notificacion con mensaje "You have successfully modified customers".')
def step_impl(context):
    try:
        AltaOrdenPage.saveCustomer(context)
    except Exception:
        context.driver.close()
        assert False, "La prueba Fallo en: save_customer"


#############VERIFICADO###############

@when(u'Se agrega Producto "{Product}" se selecciona cantidad y se guarda la orden')
def select_Product(context, Product):
    try:
        AltaOrdenPage.selectionProduct(context, Product)
    except Exception:
        context.driver.close()
        assert False, "La prueba Fallo en: select_Product"


#############VERIFICADO###############

@when(u'Se realiza click sobre el boton de configuracion ubicado en la opcion Payment Address')
def Configuracion_payment_method(context):
    try:
        AltaOrdenPage.click_configuration_payment_addres(context, )
    except Exception:
        context.driver.close()
        assert False, "La prueba Fallo en: Configuracion_payment_method"


#############VERIFICADO###############

@when(
    u'se completa el formulario PaymentAddress con los siguientes datos:  FirstName, "{FirstName}", LastName: "{LastName}", Customer: "{Customer}", Address : "{Address}",  City : "{City}" ,  PostCode : "{PostCode}"')
def PaymentAddress(context, FirstName, LastName, Customer, Address, City, PostCode):
    try:
        AltaOrdenPage.paymentAddress(context, Customer, FirstName, LastName, Address, PostCode, City)
    except Exception:
        context.driver.close()
        assert False, "La prueba Fallo en: PaymentAddress"


#############VERIFICADO###############

@when(
    u'se completa el formulario ShippingAddress con los siguientes datos:  FirsName, "{FirstName}", LastName: "{LastName}", Customer: "{Customer}", Address : "{Address}",  City : "{City}" ,  PostCode : "{PostCode}"')
def ShippingAddress(context, Customer, FirstName, LastName, Address, PostCode, City):
    try:
        AltaOrdenPage.shippingAddress(context, Customer, FirstName, LastName, Address, PostCode, City)
    except Exception:
        context.driver.close()
        assert False, "La prueba Fallo en: ShippingAddress"


#############VERIFICADO###############

@when(u'Se selecciona metodo de envio y PaymentMethod')
def method_shipping_Payment(context):
    try:
        AltaOrdenPage.shippingMethod(context)
    except Exception:
        context.driver.close()
        assert False, "La prueba Fallo en: method_shipping_Payment"


#############VERIFICADO###############

@when(u'Se realiza click en el boton Confirm')
def button_confirmar(context):
    try:
        AltaOrdenPage.confirmarOrden(context)
    except Exception:
        context.driver.close()
        assert False, "La prueba Fallo en: button_confirmar"


#############VERIFICADO###############

@when(u'Se realiza click sobre el boton Back / Ubicado en la parte superior Derecha.')
def Back(context):
    try:
        AltaOrdenPage.backButton(context)
    except Exception:
        context.driver.close()
        assert False, "La prueba Fallo en: Back"


#####################################################################################

@then(u'Se realiza el logout de la plataforma.')
def step_impl(context):
    try:
        AltaOrdenPage.logout(context)
        context.driver.close()
    except Exception:
        context.driver.close()
        assert False, "La prueba Fallo en:"

#####################################################################################
