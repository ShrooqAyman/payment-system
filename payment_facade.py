from paymentGateway import PaymentGateway
from billingSystem import BillingSystem


class PaymentFacade:
    def __init__(self):
        """
        Initialize a PaymentFacade instance with a PaymentGateway and a BillingSystem.
        """
        self.paymentGateway = PaymentGateway()
        self.billingSystem = BillingSystem()

    def payWithCreditCard(self, amount, card_num, exp_date, cvv):
        """
        Make payment with a credit card.

        Args:
            amount (float): amount to be paid.
            card_num (str): credit card number.
            exp_date (str): credit card expire date.
            cvv (str): credit card cvv.
        """

        payment_info = {'strategy': 'CreditCard', 'amount': amount,
                        'card_num': card_num, 'exp_date': exp_date, 'cvv': cvv}
        if self.paymentGateway.receives_payment_info(payment_info):
            print('Done successfully pay With a Credit Card\n')
            self.billingSystem.add_bill(payment_info)
        else:
            print('fail pay With a Credit Card')

    def payWithPayPal(self, amount, email, password):
        """
        Make payment with a paypal.

        Args:
            amount (float): amount to be paid.
            email (str): paypal email.
            password (str): paypal password.
        """
        payment_info = {'strategy': 'PayPal', 'amount': amount,
                        'email': email, 'password': password}
        if self.paymentGateway.receives_payment_info(payment_info):
            print('Done successfully pay With PayPal\n')
            self.billingSystem.add_bill(payment_info)
        else:
            print('fail pay WithPayPal')

    def payWithBankTransfer(self, amount, account1, account2):
        """
        Make payment with a BankTransfer.

        Args:
            amount (float): amount to be paid.
            account1 (str): bank account to transfer from.
            account2 (str): bank account to transfer to.
        """
        payment_info = {'strategy': 'BankTransfer', 'amount': amount,
                        'account1': account1, 'account2': account2}
        if self.paymentGateway.receives_payment_info(payment_info):
            print('Done successfully pay With Bank Transfer\n')
            self.billingSystem.add_bill(payment_info)
        else:
            print('fail pay With Bank Transfer')
