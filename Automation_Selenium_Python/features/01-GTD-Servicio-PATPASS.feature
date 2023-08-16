Feature: Como usuario se desea realizar la contratacion de los servicios ofrecidos por GTD, realizando el pago a traves de patpass

  Scenario Outline: Solicitud Servicio "<TestCase>"
    Given  Iniciando Navegador en la Web : "<Web>"
    When Se selecciona region: "<Region>"
    When Se selecciona Comuna: "<Comuna>
    When Se selecciona Calle y Numero: "<Calle>" , "<Numero>", Depto ["<Depto>"]
    When Se ingresa Nombre y Apellido : "<Nombre>"
    When se ingresa Numero de contacto: "<Contacto>"
    When se ingresa Correo electronico : "<Email>"
    When Seleccionar Cobertura: "<Cobertura>" y Realizar click en Confirmar Plan
    When Seleccionar Algun Interes: "<Interes>"
    When Seleccionar Fecha y horario Disponible
    When Confirmar contratacion, Elegir metodo de Pago "<Pago>" ingresar Rut "<Rut>" ingresar "<Serie>"
    When Se visualiza Ventana Patpass, se completan los campos Numero de Tarjeta: "<Tar>" y Ciudad
    When Se visualiza Pantalla Transbank se Completa Rut: "<RutPago>" y  Clave: "<Clave>"
    When Se tilda la casilla "Acepto terminos y condiciones" , se realiza click Continuar.
    Then Se valida la obtencion del id de la solicitud realizada

    Examples:
      | Web                                                    | Depto | Region        | Comuna   | Calle                     | Numero | Nombre          | Contacto  | Email                           | Cobertura         | Interes            | Pago                  | Rut      | Serie | TestCase | Tar                 | Clave | RutPago      |
      | https://mcstaging.tienda.gtd.cl/plan-internet-800.html |       | METROPOLITANA | VITACURA | ALCALDE JOSE RAMON CASTRO | 2441   | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Plan Internet 800 | Router Eero Amazon | Pago Automático (PAT) | 98499482 | XXXX  | GTD-2    | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.gtd.cl/plan-internet-giga.html                              |       | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Plan Internet GIGA                                    | Router Eero Amazon    | Pago Automático (PAT) | 366288783 | XXXX  | GTD-3    | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.gtd.cl/plan-internet-2-gigas.html                           |       | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Plan Internet 2 Gigas                                 | Router Eero Amazon    | Pago Automático (PAT) | 366288783 | XXXX  | GTD-4    | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.gtd.cl/duopack-600-internet-fibra-television.html           |       | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 600 (Internet fibra + GTD TV)                 | TNT Sport Premium     | Pago Automático (PAT) | 366288783 | XXXX  | GTD-5    | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.gtd.cl/duopack-800-internet-fibra-television.html           |       | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 800 (Internet fibra + GTD TV)                 | TNT Sport Premium     | Pago Automático (PAT) | 366288783 | XXXX  | GTD-6    | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.gtd.cl/duopack-600-internet-fibra-telefonia.html            |       | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 600 (Internet fibra + Telefonía)              | Router Eero Amazon    | Pago Automático (PAT) | 366288783 | XXXX  | GTD-9    | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.gtd.cl/duopack-800-internet-fibra-telefonia.html            |       | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack 800 (Internet fibra + Telefonía)              | Router Eero Amazon    | Pago Automático (PAT) | 366288783 | XXXX  | GTD-10   | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.gtd.cl/duopack-giga-internet-fibra-telefonia.html           |       | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Duopack GIGA (Internet fibra + Telefonía)             | Router Eero Amazon    | Pago Automático (PAT) | 366288783 | XXXX  | GTD-11   | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.gtd.cl/tripack-600-internet-fibra-television-telefonia.html |       | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Tripack 600 (Internet fibra + GTD TV + Telefonía)     | TNT Sport Premium     | Pago Automático (PAT) | 366288783 | XXXX  | GTD-12   | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
#      | https://mcstaging.tienda.gtd.cl/tripack-800-internet-fibra-television-telefonia.html |       | METROPOLITANA | LAS CONDES | CERRO PROVINCIA | 125    | Testing Balloon | 957544722 | luis.sandoval@balloon-group.com | Tripack 800 (Internet fibra + Televisión + Telefonía) | Router Eero Amazon    | Pago Automático (PAT) | 366288783 | XXXX  | GTD-13   | 4051-8856-0044-6623 | 123   | 11.111.111-1 |
