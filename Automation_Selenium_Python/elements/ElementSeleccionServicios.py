#########VALIDAR FACTIVIDAD#############


Region = "//input[contains(@id,'region')]"
Comuna = "//input[contains(@id,'commune')]"
Calle = "//input[contains(@id,'street')]"
NumeroCalle = "//input[contains(@id,'number')]"
NombreApellido = "//input[contains(@id,'name')]"
Telefono = "(//input[@name='phone'][@data-bind='textInput: phone, event: {input: changeOnStep}'])[1]"
CorreoElectronico = "//input[contains(@id,'hiring')]"
ValidarDatos = "//p[contains(.,'Validar Datos')]"
RutServicio = "//input[@id='rut']"
Depto = "//input[contains(@data-bind,'enable: loadedFlats, textInput: searchFlats')]"

#########Seleccion Plan e Interes #########

ConfirmarPlan = "//p[contains(.,'Confirmar Plan')]"
TambienInteresConfirmar = "//p[contains(.,'Continuar')]"

########### Fecha/Horario #############


Horario = "(//li[@class='clsAvailableHour'])[1]"
COntinuarHorario = "//p[contains(.,'Continuar')]"

########## CONFIRMAR##############
RutPatPass="(//input[@name='custom_attributes[rut]'][@placeholder='Ej: 12345678-9'])[3]"
SeriePatPass="(//input[contains(@name,'1]')])[3]"
rut = "(//span[text()='RUT']//..//..//div//input[@name='custom_attributes[rut]'])[2]"
rutBoleta = "(//input[@name='custom_attributes[rut]'])[3]"
SerieBoleta= "(//input[contains(@name,'1]')])[3]"
Serie = "(//input[contains(@name,'1]')])[2]"
AceptoTyC = "//span[contains(@id,'check4')]"
ContinuarDatos = "//span[contains(.,'Continuar')]"

################ PATPASS ##############

TarjetaPasPass = "//input[@id='formulario:tarjeta_th']"
ListaCity = "//select[@id='formulario:ciudadesCombo']"
AceptarPATPASS = "//input[@id='formulario:gotoWebPay']"
Transbankvalidar = "//img[@src='images/transbank.gif']"
TransbankRutClientInput = "//input[@id='rutClient']"
TransbankPassClientInput = "//input[@id='passwordClient']"
TransbankSubmitButton = "//input[@type='submit']"
TransbankConfirmarPago = "//input[@type='submit']"
PatPassInformacionConfirmar = "//span[contains(.,'Información de Pago')]"
PatpassCheckTyC = "//input[@type='checkbox']"
PatPassSuscribir = "//input[@id='formulario:suscribirStep3']"
validate = "//h1[contains(@class,'page-title')]"
IDValidateGTD = "//div[@class='id-orden']"

###############TELEFONO#################
TelefonoTELSUR = "(//input[@placeholder='Ingresa tu teléfono'])[2]"
