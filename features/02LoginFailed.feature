Feature: Inicio de Sesion con Datos Invalidos
  Background:
    Given  Iniciando Navegador en la Web https://demo.opencart.com/admin

    Scenario Outline: Se observan los campos UserName y Password
      When Escribiendo campo  Username :"<Username>"
      When Escribiendo campo password :"<Password>"
      When Click en boton Login
      Then validar Notificacion  "No match for Username and/or Password."



       Examples:
         | Username | Password |
         | demo     | 125635   |




