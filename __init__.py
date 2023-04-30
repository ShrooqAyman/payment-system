from payment_facade import PaymentFacade


facade = PaymentFacade()

facade.payWithCreditCard(100, "1234567890123456", "12/23", "123")
facade.payWithPayPal(50, "example@gmail.com", "password")
facade.payWithBankTransfer(75, "123456789", "987654321")
facade.payWithBankTransfer(-75, "123456789", "987654321")