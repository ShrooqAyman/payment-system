from billingSystem import BillingSystem
from payment_method import PayPal, CreditCard, BankTransfer

class PaymentGateway:
    """
    A payment gateway that processes payment using different payment methods.
    """
    def __init__(self):
        """
        Initializes instances of the payment methods.
        """
        self.PayPal = PayPal()
        self.CreditCard = CreditCard()
        self.BankTransfer = BankTransfer()

    def receives_payment_info(self, payment_info):
        """
        Receives payment information and calls the appropriate payment method based on strategy value.
        
        Args:
            payment_info: a dictionary containing payment information.
        
        Returns:
            payment response from the selected payment method.
        """
        print('payment gateway received payment info successfully')
        response = self.transmit_to_payment_processor(payment_info)
        return self.send_payment_response(response)

    def transmit_to_payment_processor(self, payment_info):
        """
        Authorizes and processes the payment using selected payment method.
        
        Args:
             payment_info: a dictionary containing payment information.
        
        Returns:
            True if payment processing is successful, False otherwise.
        """

        if payment_info['strategy'] == 'CreditCard':
            try:
                if self.CreditCard.authorize_payment(payment_info):
                    return self.CreditCard.process_payment(payment_info)
            except Exception as e:
                print('Error ')

        elif payment_info['strategy'] == 'PayPal':
            try: 
                if self.PayPal.authorize_payment(payment_info):
                    return self.PayPal.process_payment(payment_info)
            except Exception as e:
                print('Error')

        elif payment_info['strategy'] == 'BankTransfer':
            try:
                if self.BankTransfer.authorize_payment(payment_info):
                    return self.BankTransfer.process_payment(payment_info)
            except Exception as e:
                return False

    def send_payment_response(self, reponse):
        """
        Sends the payment response.
        
        Args:
            response: the payment response from selected payment method.
        
        Returns:
            the payment response.
        """
        return reponse

