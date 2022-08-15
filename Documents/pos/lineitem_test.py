import unittest

class LineItems_(unittest.TestCase):
    
    def setUp(self):
        self.fixture = self._Fixture()
        self.product = self.Product()
        self.line_items = self.LineItems()
        
    def test_add_line_items(self):
        self.fixture.given_a_product(self.product) #product will be a dictionary with qunatity as value
        self.fixture.when_add_line_item_is_called()
        self.fixture.then_result_should_be(quantity +1)
        
    def test_subtract_line_items(self):
        self.fixture.given_a_product(self.product)
        self.fixture.when_subtract_from_line_item_is_called()
        self.fixture.then_result_should_be(quantity - 1)
        
    def test_display_line_items_list_when_transaction_is_made(self):
        self.fixture.given_the_transaction_is_made(self.product)
        self.fixture.when_display_line_items_is_called()
        self.fixture.then_result_should_be(self.product)
    
    def test_update_quantity_of_line_item(self):
        self.fixture.given_line_items()   
        self.fixture.when_update_quantity_of_line_item_is_called()
        self.fixture.then_result_should_be(True)
     
    def test_calculate_total_balance_of_line_items(self):
        self.fixture.given_line_items(self.line_items)   
        self.fixture.when_calculate_total_balance_is_called()
        self.fixture.then_result_should_be(True)
     
    def test_display_total_balance_of_line_items(self):
        self.fixture.given_line_items()   
        self.fixture.when_display_total_balance_is_called()
        self.fixture.then_result_should_be(True)
        
    def test_void_the_line_item(self):
        self.fixture.given_line_items()
        self.fixture.when_void_the_line_item_is_called()
        self.fixture.then_result_should_be(True)
    
    def test_display_all_voided_and_non_voided_line_items(self):
        self.fixture.given_all_line_items()
        self.fixture.when_display_all_line_items_is_called()
        self.fixture.then_result_should_be(True)    

                 
    class _Fixture(unittest.TestCase):
        
        def __init__(self, methodName: str = ...) -> None:
            super().__init__(methodName)
        
        def given_a_product(self):
            pass
            
        def given_line_items(self):
            pass
            
        def given_all_line_items(self):
            pass
        
        def when_add_line_item_is_called(self):
            pass
            
        def when_subtract_from_line_item_is_called(self):
            pass
            
        def given_the_transaction_is_made(self):
            pass
            
        def when_display_line_items_is_called(self):
            pass
            
        def when_update_quantity_of_line_item_is_called(self):
            pass
            
        def when_calculate_total_balance_is_called(self):
            pass
            
        def when_display_total_balance_is_called(self):
            pass
        
        def when_void_the_line_item_is_called(self):
            pass
        
        def when_display_all_line_items_is_called(self):
            pass
                  
        def then_result_should_be(self):
            pass
        
        def then_result_should_be(self):
            pass
            
        
if __name__ == '__main__':
    unittest.main()     