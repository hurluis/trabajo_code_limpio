#interfaz de usuario tipo consola para la funcionalidad de calxular la cuota de la tarjeta de credito

from PaymentLogic import calcPayment

try:
#bloque protegido es todo lo que esta dentro del try y el except
#obtener los datos de entrada 
    purchase_amount = float(input("ingrese el valor de la compra: "))
    num_payments = int(input("ingrese el numero de cuotas de la compra: "))
    interest_rate = float(input("ingrese el interes de la compra: "))

    while interest_rate >3.8:
        interest_rate = float(input("ingrese el interes de manera valida no puede superar el 3.8 de interes: "))
    else:
    #reliazar el proceso 
        payment= calcPayment( purchase_amount, interest_rate, interest_rate )    

    #obtener los datos de salida 

        print(f"El valor de la cuota es: {payment}")

#en la variable the_exeption se guarda el error
except ValueError as the_error:
    print(f"El valor ingresado es incorrecto: {the_error}")

#en la variable the_exeption se guarda el error
except Exception as the_exception:
    #bloque de manejo de excepcion
    print( f"No puedo continuar ocurrio un error{the_exception}")
    