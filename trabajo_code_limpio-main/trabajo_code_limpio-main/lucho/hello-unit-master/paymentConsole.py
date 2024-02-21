#interfaz de usuario tipo consola para la funcionalidad de calxular la cuota de la tarjeta de credito

from PaymentLogic import calcPayment

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
