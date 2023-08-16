from Automation_Selenium_Python.Funciones.Funciones import funciones_2_0
from behave import *
from Automation_Selenium_Python.pages.GTDServicioPage import SeleccionServicio


@given(u'Iniciando Navegador en la Web : "{Web}"')
def step_impl(context, Web):
    try:
        SeleccionServicio.OpenBrowser(context, Web)

    except:
        funciones_2_0.screenShot(context, "Fallo al iniciar navegador")
        context.driver.close()
        assert False, "La prueba fallo en: ----->>> Iniciando Navegador"


@when(u'Se selecciona region: "{Region}"')
def step_impl(context, Region):
    try:
        SeleccionServicio.InputSeleciconRegion(context, Region)
    except:
        funciones_2_0.screenShot(context, "Se selecciona region: '{Region}'")
        context.driver.close()
        assert True, "La prueba Fallo en: ----->>> Seleccione Region"


@when(u'Se selecciona Comuna: "{Comuna}')
def step_impl(context, Comuna):
    try:
        SeleccionServicio.SeleccionComuna(context, Comuna)
    except Exception:
        funciones_2_0.screenShot(context, "Se selecciona Comuna: '{Comuna}'")
        context.driver.close()
        assert False, "La prueba fallo en: ----->>> se Selecciona Comuna"


@when(u'Se selecciona Calle y Numero: "{Calle}" , "{Numero}"')
def step_impl(context, Calle, Numero):
    try:
        SeleccionServicio.CalleyAltura(context, Calle, Numero)
    except:
        funciones_2_0.screenShot(context, "Se selecciona Calle y Numero: '{Calle}' '{Numero}'")
        context.driver.close()
        assert False, "La prueba fallo: ----->>> en Seleccionar calle y numero"
@when('Se selecciona Calle y Numero: "{Calle}" , "{Numero}", Depto [{Depto}]')
def seleccionar_calle_numero_depto(context, Calle, Numero, Depto):
    try:
        Depto = Depto.strip('[]"')
        if Depto and len(Depto.strip()) > 0 and not Depto.strip() == ",":
            SeleccionServicio.CalleyAlturaDepto(context, Calle, Numero, Depto)
            funciones_2_0.screenShot(context, f"Se selecciona Calle y Numero: '{Calle}' '{Numero}'{Depto}")
        else:
            SeleccionServicio.CalleyAltura(context, Calle, Numero)
            funciones_2_0.screenShot(context, f"Se selecciona Calle y Numero: '{Calle}' '{Numero}'")
    except:
        funciones_2_0.screenShot(context, f"Se selecciona Calle y Numero: '{Calle}' '{Numero}'")
        context.driver.close()
        assert False, "La prueba fallo: ----->>> en Seleccionar calle y numero"

@when(u'Se ingresa Nombre y Apellido : "{Nombre}"')
def step_impl(context, Nombre):
    try:
        SeleccionServicio.NombreApellido(context, Nombre)
    except:
        funciones_2_0.screenShot(context, 'Se ingresa Nombre y Apellido : "{Nombre}"')
        context.driver.close()
        assert False, "La prueba fallo: ----->>> Se ingresa Nombre y Apellido : '{Nombre}'"


@when(u'se ingresa Numero de contacto: "{Contacto}"')
def step_impl(context, Contacto):
    try:
        SeleccionServicio.Contacto(context, Contacto)
    except:
        funciones_2_0.screenShot(context, 'se ingresa Numero de contacto: "{Contacto}"')
        context.driver.close()
        assert False, "La prueba fallo en : ----->>> ingresar numero de contacto"


@when(u'se ingresa Correo electronico : "{Email}"')
def step_impl(context, Email):
    try:
        SeleccionServicio.CorreoElectronico(context, Email)
    except:
        funciones_2_0.screenShot(context, 'se ingresa Correo electronico : "{Email}"')
        context.driver.close()
        assert False, "La prueba fallo en: ----->>> ingresar correo electronico"


@when(u'Seleccionar Cobertura: "{Cobertura}" y Realizar click en Confirmar Plan')
def step_impl(context, Cobertura):
    try:
        SeleccionServicio.SeleccionarCobertura(context, Cobertura)
    except:
        funciones_2_0.screenShot(context, 'Seleccionar Cobertura: "{Cobertura}" y Realizar click en Confirmar Plan')
        context.driver.close()
        assert False, "la prueba fallo: ----->>> en realizar click confirmar plan"


@when(u'Seleccionar Algun Interes: "{Interes}"')
def step_impl(context, Interes):
    try:
        SeleccionServicio.InteresesOpciones(context, Interes)
    except:
        funciones_2_0.screenShot(context, 'Seleccionar Algun Interes: "{Interes}"')
        context.driver.close()
        assert False, "Seleccionar Algun Interes: '{Interes}'"


@when(u'Seleccionar Fecha y horario Disponible')
def step_impl(context):
    try:
        SeleccionServicio.SeleccionarFecha(context)
    except:
        funciones_2_0.screenShot(context, 'Seleccionar Fecha y horario Disponible')
        context.driver.close()
        assert False, "La prueba fallo en:  ----->>> Seleccionar fecha y horario"


@when(u'Confirmar contratacion, Elegir metodo de Pago "{Pago}" ingresar Rut "{Rut}" ingresar "{Serie}"')
def step_impl(context, Pago, Rut, Serie):
    try:
        SeleccionServicio.ConfirmarContratacion(context, Pago, Rut, Serie)
    except:
        funciones_2_0.screenShot(context,
                                 'Confirmar contratacion, Elegir metodo de Pago "{Pago}" ingresar Rut "{Rut}" ingresar "{Serie}"')
        context.driver.close()
        assert False, "La prueba fallo en :  ----->>> Confirmar contratacionRut"


@when(u'Se visualiza Ventana Patpass, se completan los campos Numero de Tarjeta: "{Tar}" y Ciudad')
def step_impl(context, Tar):
    try:
        SeleccionServicio.PatPass(context, Tar)
    except:
        funciones_2_0.screenShot(context,
                                 'Se visualiza Ventana Patpass, se completan los campos Numero de Tarjeta: "{Tar}" y Ciudad')
        context.driver.close()
        assert False, "La prueba fallo en :  ----->>> Confirmar contratacionRut"


@when(u'Se visualiza Pantalla Transbank se Completa Rut: "{RutPago}" y  Clave: "{Clave}"')
def step_impl(context, RutPago, Clave):
    try:
        SeleccionServicio.transbank(context, RutPago, Clave)
    except:
        funciones_2_0.screenShot(context,
                                 'Se visualiza Pantalla Transbank se Completa Rut: "{RutPago}" y  Clave: "{Clave}"')
        context.driver.close()
        assert False, "La prueba fallo en :  ----->>> Confirmar contratacionRut"


@when(u'Se tilda la casilla "Acepto terminos y condiciones" , se realiza click Continuar.')
def step_impl(context):
    try:
        context.driver.refresh()
        SeleccionServicio.ValPatPass(context, )
    except:
        funciones_2_0.screenShot(context,
                                 'Se tilda la casilla "Acepto terminos y condiciones" , se realiza click Continuar.')
        context.driver.close()
        assert False, "La prueba fallo en :  ----->>> Se tilda la casilla Acepto terminos y condiciones"

@then(u'Se valida la obtencion del id de la solicitud realizada')
def step_impl(context):
    try:
        SeleccionServicio.ValidarSolicitud(context)
        SeleccionServicio.AlmacenamientoId(context)
        context.driver.close()
    except:
        funciones_2_0.screenShot(context, 'Se valida la obtencion del id de la solicitud realizada')
        context.driver.close()
        assert False, "La prueba fallo en :  ----->>> Se tilda la casilla Acepto terminos y condiciones"
