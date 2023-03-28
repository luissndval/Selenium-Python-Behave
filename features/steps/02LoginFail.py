import logging

from behave import *

from pages.LoginPage import LoginPage

logging.basicConfig(level=logging.INFO)


@then(u'validar Notificacion  "No match for Username and/or Password."')
def step_impl(context):
    try:
        LoginPage.ValidacionCredencialesIncorrectas(context)
        context.driver.close()
    except Exception:
        context.driver.close()
        assert False, "La prueba fallo en Validar Notificacion (No match for Username and/or Password)"
