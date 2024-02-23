# Todas las prueba sunitarias importan la biblioteca unittest
import unittest
# Las pruebas importan los modulos que hacen el trabajo
import PaymentLogic 


# Debe existir por lo menos una clase que contenga las pruyebas unitarias
# descediente de unittest.TestCase
class CreditCardTest(unittest.TestCase):

    # Cada prueba unitaria es un metodo la clase
    def testPayment1(self):
        # Cada metodo de prueba debe llamar un metodo assert
        # para comprobar si la prueba pasa
        compra = 200000
        tasa = 0.031
        plazo = 36
        cuota = 9297.96
        resultado = PaymentLogic.calcPayment( compra, tasa, plazo )
        # Prueba que dos variables sean iguales
        self.assertAlmostEqual( cuota, resultado, 2  )
        
    
    def testPayment1zerointerst(self):
        # Cada metodo de prueba debe llamar un metodo assert
        # para comprobar si la prueba pasa
        compra = 480000
        tasa = 0
        plazo = 48
        cuota = 10000
        resultado = PaymentLogic.calcPayment( compra, tasa, plazo )
        # Prueba que dos variables sean iguales
        self.assertAlmostEqual( resultado , cuota, 2)
        
    """        
    def testExcesiveInterest(self):
        #Entradas
        purchase_amount=50000
        num_payments=36
        interest_rate=0.124

        try:
            #Llamar al proceso
            result=PaymentLogic.calcPayment(purchase_amount,interest_rate,num_payments)
            print("no ocurrio ninguna excepcion")        
            self.assertTrue(False, "no disparo la excepcion")
        except:
            #aqui es donde llega el control cuando se genera una excepcion
            print("si ocurrio una excepcion")
            pass #indica que la prueba fue exitosa


        #verificar el resultado
        #debe retornar error para que indique que el interes es excesivo
        expected_result="ERROR"
        self.assertEqual(result, expected_result)
        """
        # codigo largo
    
    def testExcesiveInterest(self):
        #Entradas
        purchase_amount=50000
        num_payments=36
        interest_rate=0.124
        
        self.assertRaises(PaymentLogic.ExcesiveInterestError, PaymentLogic.calcPayment, purchase_amount,interest_rate,num_payments)

    def testPurchase_amount_zero(self):
        #Entradas
        purchase_amount=0
        num_payments=36
        interest_rate=0.031
        
        self.assertRaises(PaymentLogic.InavlidPurchaseError, PaymentLogic.calcPayment, purchase_amount,interest_rate,num_payments)
        
    def ZeroPayments(self):
        #Entradas
        purchase_amount=80000
        num_payments=0
        interest_rate=0.024
        self.assertRaises(PaymentLogic.InvalidPaymentsError, PaymentLogic.calcPayment, purchase_amount,interest_rate,num_payments)
        
    def NegativePayments(self):
        #Entradas
        purchase_amount=50000
        num_payments=-10
        interest_rate=0.01
        self.assertRaises(PaymentLogic.InvalidPaymentsError, PaymentLogic.calcPayment, purchase_amount,interest_rate,num_payments)
        
        
test = CreditCardTest()
test.ZeroPayments()
        
# Este fragmento de codigo permite ejecutar la prueb individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    # print( Payment.calcularCuota.__doc__)
    unittest.main()