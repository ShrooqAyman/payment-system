from abc import ABC, abstractmethod 

class PaymentMethod(ABC):
    @abstractmethod
    def authorize_payment(self, payment_info):
        """
        Verify the correctness of the payment information.

        Args:
            payment_info (dict): A dictionary containing the payment information.

        Returns:
            bool: True if the payment information is correct,False otherwise.
        """
        pass
    
    @abstractmethod
    def process_payment(self, payment_info):
        """
        Process the payment using the payment information.

        Args:
            payment_info (dict): A dictionary containing the payment information.

        Returns:
            bool: True if the payment was successful,False otherwise.
        """
        pass


class PayPal(PaymentMethod):
    def authorize_payment(self, payment_info):
        """
        Verify the correctness of the paypal payment information.

        Args:
            payment_info (dict): A dictionary containing the PayPal payment information.

        Returns:
            bool: True if the PayPal payment information is correct,False otherwise.
        """

        if payment_info['email'] and payment_info['password']:
            print('paypal info correct')
            return True
        print('paypal info not correct')
        return False

    def process_payment(self, payment_info):
        """
        Process the payment using the PayPal payment information.

        Args:
            payment_info (dict): A dictionary containing the PayPal payment information.

        Returns:
            bool: True if the PayPal payment was successful,False otherwise.
        """
        if payment_info['amount'] > 0:
            print('payment with paypal process successfully done')
            return True
        return False
    
    
class CreditCard(PaymentMethod):
    def authorize_payment(self, payment_info):
        """
        Verify the correctness of the CreditCard payment information.

        Args:
            payment_info (dict): A dictionary containing the CreditCard payment information.

        Returns:
            bool: True if the CreditCard payment information is correct,False otherwise.
        """
        if payment_info['exp_date'] and payment_info['card_num'] and payment_info['cvv']:
            print('CreditCard info correct')
            return True
        print('CreditCard info not correct')
        return False

    def process_payment(self, payment_info):
        """
        Process the payment using the CreditCard payment information.

        Args:
            payment_info (dict): A dictionary containing the CreditCard payment information.

        Returns:
            bool: True if the CreditCard payment was successful,False otherwise.
        """
        if payment_info['amount'] > 0:
            print('payment with CreditCard process successfully done')
            return True
        return False


class BankTransfer(PaymentMethod):
    def authorize_payment(self, payment_info):
        """
        Verify the correctness of the BankTransfer payment information.

        Args:
            payment_info (dict): A dictionary containing the BankTransfer payment information.

        Returns:
            bool: True if the BankTransfer payment information is correct,False otherwise.
        """
        if payment_info['account1'] and payment_info['account2']:
            print('Accounts info correct')
            return True
        print('Accounts info not correct')
        return False

    def process_payment(self, payment_info):
        """
        Process the payment using the BankTransfer payment information.

        Args:
            payment_info (dict): A dictionary containing the BankTransfer payment information.

        Returns:
            bool: True if the BankTransfer payment was successful,False otherwise.
        """
        if payment_info['amount'] > 0:
            print('payment with BankTransfer process successfully done')
            return True
        return False
