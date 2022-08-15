from ast import Pass
import unittest

class Product(unittest.TestCase):
    def setUp(self):
        self.fixture = self._Fixture()
        
    def test_product_is_valid(self):
        self.fixture.given_a_product(code, name, price)
        self.fixture.when_verify_product_is_called()
        self.fixture.then_result_should_be()
    
    def test_product_availability(self):
        self.fixture.given_a_product(code, name, price)
        self.fixture.when_check_product_availability_is_called()
        self.fixture.then_result_should_be()
    
    def test_product_code_is_valid(self):
        self.fixture.given_a_product(code, name, price)
        self.fixture.when_verify_product_is_called(code, name, price)
        self.fixture.then_result_should_be()
    
    class _Fixture(unittest.TestCase):
        
        def __init__(self, methodName: str = ...) -> None:
            super().__init__(methodName)
        
        def given_a_product(self):
            pass
        
        def when_verify_product_is_called(self, code, name, price):
            pass
        
        def when_check_product_availability_is_called(self):
            pass
        
        def then_result_should_be(self):
            pass

if __name__ == '__main__':
    unittest.main()     