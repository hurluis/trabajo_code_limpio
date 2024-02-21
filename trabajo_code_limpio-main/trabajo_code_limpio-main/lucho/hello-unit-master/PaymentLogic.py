

def calcPayment(purchase_amount,interest_rate,num_payments):
    """
    Calcula la cuota a pagar por una compra con una tarjeta de crédito
    compra : Valor de la compra con la tarjeta
    tasa : Debe ser un porcentaje entre 1 y 100
    plazo : numero de cuotas a diferir la compra

    El resultado no esta redondeado
    """
    
    if interest_rate>3.8:
        raise Exception("ERROR: el interes supera el interes de usura")
    
    if purchase_amount==0:
        raise Exception("Error: su compra no puede ser cero")

    if num_payments==1:
        return purchase_amount
    if interest_rate==0:
        return purchase_amount/num_payments
    else:
        i = interest_rate
        i= i/100
        return (purchase_amount * i) / (1 - (1 + i) ** (-num_payments))



