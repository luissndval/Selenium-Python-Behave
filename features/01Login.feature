Feature: Inicio de Sesion con Datos Validos
  Background:
    Given  Iniciando Navegador en la Web https://demo.opencart.com/admin

    Scenario Outline: Se observan los campos UserName y Password
      When Escribiendo campo  Username :"<Username>"
      When Escribiendo campo password :"<Password>"
      When Click en boton Login
      When validar Inicio Sesion
      Then Click en cerrar sesion


       Examples:
         | Username | Password |
         | demo     | demo     |
