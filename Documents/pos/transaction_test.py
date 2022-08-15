import unittest

class POS_TDD(unittest.TestCase):
    
    def setUp(self):
        self.fixture = self._Fixture()
        self.lineItems = LineItems()
        
    def test_transaction_is_made(self):
        lineItems = self.lineItems.getLineItems()
        total = self.lineItems.getTotal()
        self.fixture.given_the_transaction_is_made(lineItems, total, balance = 2000)
        self.fixture.when_make_transaction_is_called()
        self.fixture.then_result_should_be(True)
    
    def test_display_total_amount_given_the_transaction_is_succesful(self):
        total = self.lineItems.getTotal()
        self.fixture.given_display_total_amount(total)
        self.fixture.when_display_total_is_called()
        self.fixture.then_result_should_be(True)
    
    def test_display_line_items_when_transaction_is_made(self):
        lineItems = self.lineItems.getLineItems()
        self.fixture.given_display_line_items(lineItems)
        self.fixture.when_display_line_items_is_called()
        self.fixture.then_result_should_be(True)
        
    def test_display_total_amount_given_for_line_items(self):
        self.fixture.given_the_balance_provided(balance= 2000)   
        self.fixture.when_display_total_amount_given_is_called()
        self.fixture.then_result_should_be(2000)
            
    def test_calculate_total_change(self):
        lineItems = self.lineItems.getLineItems()
        total = self.lineItems.getTotal()
        balance = 1000
        self.fixture.given_the_transaction_is_made(lineItems , total, balance)   
        self.fixture.when_calculate_total_change_is_called()
        self.fixture.then_change_should_be(total - balance)
    
    def test_display_total_change(self):
        lineItems = self.lineItems.getLineItems()
        total = self.lineItems.getTotal()
        balance = 1000
        self.fixture.given_the_transaction_is_made(lineItems , total, balance)  
        self.fixture.when_display_total_change_is_called()
        self.fixture.then_change_should_be(total - balance)
    
    class Fixture(unittest.TestCase):
        
        def __init__(self) -> None:
            self.transaction = Transaction()
        
        def when_display_line_items_is_called(self):
            pass
            
        def when_display_total_amount_given_is_called(self):
            pass
            
        def when_display_total_change_is_called(self):
            pass
            
        def when_calculate_total_change_is_called(self):
            pass
        
        def when_subtract_from_line_item_is_called(self):
            pass
        

if __name__ == '__main__':
    unittest.main()     