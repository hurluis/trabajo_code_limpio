#Toda excepcion personalizada es hija de la clase exception, por ello hereda de esta
class ExcesiveInterestError(Exception):
    pass #indica que no tiene cuerpo la clase, solo usa los metodos de la clase exception

class InavlidPurchaseError(Exception):
    pass #indica que no tiene cuerpo la clase, solo usa los metodos de la clase exception
    

class InvalidPaymentsError(Exception):
    pass

def calcPayment(purchase_amount,interest_rate,num_payments):
    """
    Calcula la cuota a pagar por una compra con una tarjeta de crédito
    compra : Valor de la compra con la tarjeta
    tasa : Debe ser un porcentaje entre 1 y 100
    plazo : numero de cuotas a diferir la compra

    El resultado no esta redondeado
    """
    
    if interest_rate>3.8:
        raise ExcesiveInterestError("ERROR: el interes supera el interes de usura")
    
    if purchase_amount==0:
        raise InavlidPurchaseError("Error: su compra no puede ser cero, esta debe ser mayor a cero")
    
    if num_payments<=0:
        raise InvalidPaymentsError("Error: su compra no puede diferirse a cero cuoutas o una cuota menor a cero")
        

    if num_payments==1:
        return purchase_amount
    if interest_rate==0:
        return purchase_amount/num_payments
    else:
        i = interest_rate
        i= i/100
        return (purchase_amount * i) / (1 - (1 + i) ** (-num_payments))



