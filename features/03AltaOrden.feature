Feature:  Iniciada Sesion crear ordenes agregando Customer, Payment method, Payment address.

  Background:
    Given  Iniciando Navegador en la Web https://demo.opencart.com/admin

  Scenario Outline: Alta de ordenes
    When Escribiendo campo  Username :"<Username>"
    When Escribiendo campo password :"<Password>"
    When Click en boton Login
    When Se ubica el panel de Navigation y se selecciona la opcion Sales > Orders
    When Se localiza el boton add new y se realiza click
    When Se realiza click sobre el boton de configuracion ubicado en la opcion Customer
    When Se ingresa el nombre del Customer: "<Customer>", se completa el formulario con los datos: FirstName,  "<FirstName>", LastName: "<LastName>", Email: "<Email>",Telephone: "<Telephone>"
    When Se realiza click en Save y se valida Notificacion con mensaje "You have successfully modified customers".
    When Se agrega Producto "<Product>" se selecciona cantidad y se guarda la orden
    When Se realiza click sobre el boton de configuracion ubicado en la opcion Payment Address
    When se completa el formulario PaymentAddress con los siguientes datos:  FirstName, "<FirstName>", LastName: "<LastName>", Customer: "<Customer>", Address : "<Address>",  City : "<City>" ,  PostCode : "<PostCode>"
    When se completa el formulario ShippingAddress con los siguientes datos:  FirsName, "<FirstName>", LastName: "<LastName>", Customer: "<Customer>", Address : "<Address>",  City : "<City>" ,  PostCode : "<PostCode>"
    When Se selecciona metodo de envio y PaymentMethod
    When Se realiza click en el boton Confirm
    When Se realiza click sobre el boton Back / Ubicado en la parte superior Derecha.
    Then Se realiza el logout de la plataforma.


    Examples:
      | Username | Password | Customer     | FirstName | LastName  | Email          | Telephone  | Product | Address     | City            | PostCode |
      | demo     | demo     | MKT          | Jorge     | Rigo      | ls12@m.com     | 1133335544 | iMac    | Moreno 3065 | Capital Federal | 1406     |
#      | demo     | demo     | MountanRider | Frank     | Virgolini | ls12@gmail.com | 1133555544 | iMac    | Catamarca30 | Capital Federal | 1406     |
