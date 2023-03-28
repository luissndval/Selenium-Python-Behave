from behave import *

from pages.LoginPage import LoginPage


@given(u'Iniciando Navegador en la Web https://demo.opencart.com/admin')
def step_impl(context):
    try:
        LoginPage.OpenBrowser(context)
    except Exception:
        context.driver.close()
        assert False, "La prueba Fallo en Iniciar Navegador en la web https://demo.opencart.com/admin "


@when(u'Escribiendo campo  Username :"{Username}"')
def step_impl(context, Username):
    try:
        LoginPage.inputUserName(context, Username)
    except Exception:
        context.driver.close()
        assert False, "La prueba fallo en Ingresar Nombre de usuario"


@when(u'Escribiendo campo password :"{Password}"')
def step_impl(context, Password):
    try:
        LoginPage.inputPassword(context, Password)
    except Exception:
        context.driver.close()
        assert False, "La prueba fallo en Ingresar Password"


@when(u'Click en boton Login')
def step_impl(context):
    try:
        LoginPage.clickLogin(context)
    except Exception:
        context.driver.close()
        assert False, "La prueba fallo en pulsar boton Login"


@when(u'validar Inicio Sesion')
def step_impl(context):
    try:
        LoginPage.validacionLogin(context)
    except Exception:
        context.driver.close()
        assert False, "La prueba fallo validar Inicio Sesion"


@then(u'Click en cerrar sesion')
def step_impl(context):
    try:
        LoginPage.Logout(context)
        context.driver.close()
    except Exception:
        context.driver.close()
        assert False, "La prueba fallo en pulsar boton Login"
