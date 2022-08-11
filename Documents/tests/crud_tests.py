import unittest
from db import *
from user import User
import pdb

class CrudTest(unittest.TestCase):
        def setUp(self):
            self.fixture = self._Fixture()        
        
        def test_create_a_user_table(self):
            self.fixture.given_a_table()
            self.fixture.when_create_table_is_called()
            self.fixture.then_result_should_be('Table created successfully')
            
        def test_user_with_no_fields(self):
            self.fixture.given_no_data()
            self.fixture.when_create_user_is_called()
            self.fixture.then_result_should_be(False)
         
        def test_user_with_required_fields(self):
            self.fixture.given_required_fields('Ahmad', 'ahmad@qbatch.com', 'qbatch@123')
            self.fixture.when_create_user_is_called()
            self.fixture.then_result_should_be(True)
            
        def test_user_with_optional_fields(self):
            self.fixture.given_optional_fields('Ahmad', 'ahmad@qbatch.com', 'qbatch@123', 'Faisalabad', '21')
            self.fixture.when_create_user_is_called()
            self.fixture.then_result_should_be(True)
            
        def test_when_user_already_exists(self):
            self.fixture.given_existant_user('Ahmad', 'ahmad@qbatch.com', 'qbatch@123') 
            self.fixture.when_create_user_is_called()
            self.fixture.then_result_should_be('User already exists')
            
        def test_user_when_weak_password_provided(self):
            self.fixture.given_weak_password('Ahmad', 'ahmad@qbatch.com', '123')
            self.fixture.when_create_user_is_called()
            self.fixture.then_result_should_be('Provide a strong password')
            
        def test_user_when_invalid_email_provided(self):
            self.fixture.given_invalid_email('Ahmad', 'ahmad@123.com', 'qbatch@123')
            self.fixture.when_create_user_is_called()
            self.fixture.then_result_should_be('Provide a valid email address')
            
        def test_user_when_invalid_name_provided(self):
            self.fixture.given_invalid_name('12@hmad', 'ahmad@123.com', 'qbatch@123')
            self.fixture.when_create_user_is_called()
            self.fixture.then_result_should_be('Name must be all letters')
        
        def test_fetch_user_data(self):
            self.fixture.given_fetch_user_data(t_name = 'user' , c_name = ['username'], condition = {'key' : 'value'})
            self.fixture.when_fetch_user_data_is_called()
            self.fixture.then_result_should_be(True)
        
        def test_invalid_table_name_provided_for_fetch_user_data(self):
            self.fixture.given_invalid_table_name(t_name = 'test' , c_name = ['username'], condition = {'key' : 'value'})
            self.fixture.when_fetch_user_data_is_called()
            self.fixture.then_result_should_be(False)
        
        def test_invalid_column_name_for_fetch_user_data(self):
            self.fixture.given_invalid_column_name_for_fetch_user_data(t_name = 'user' , c_name = ['usern@ame'], condition = {'key' : 'value'})
            self.fixture.when_fetch_user_data_is_called()
            self.fixture.then_result_should_be(False)
        
        def test_invalid_condition_for_fetch_user_data(self):
            self.fixture.given_invalid_condition_for_fetch_user_data(t_name = 'test' , c_name = ['username'], condition = {'email' : 123})
            self.fixture.when_fetch_user_data_is_called()
            self.fixture.then_result_should_be(False)
        
        def test_update_user_data(self):
            self.fixture.given_update_user_data(t_name = 'user' ,c_value = {'username':'Ali'}, condition = {'key' : 'value'})
            self.fixture.when_update_user_data_is_called()
            self.fixture.then_exception_should_be_this("ValueError")
        
        def test_invalid_table_name_for_update_user_data(self):
            self.fixture.given_invalid_table_name_for_update_user_data(t_name = 'us3r' ,c_value = {'username':'Ali'}, condition = {'key' : 'value'})
            self.fixture.when_update_user_data_is_called()
            self.fixture.then_result_should_be(False)
        
        def test_invalid_column_name_for_update_user_data(self):
            self.fixture.given_invalid_column_name_for_update_user_data(t_name = 'user', c_value = {'n@ame' : 'Ali'}, condition = {'key': 'value'})
            self.fixture.when_update_user_data_is_called()
            self.fixture.then_result_should_be(False)
        
        def test_invalid_value_for_update_user_data(self):
            self.fixture.given_invalid_value_for_update_user_data(t_name= 'user', c_value = {'name' : 123}, condition = {'key': 'value'})
            self.fixture.when_update_user_data_is_called()
            self.fixture.then_result_should_be(False)
        
        def test_invalid_condition_for_update_user_data(self):
            self.fixture.given_invalid_condition_for_update_user_data(t_name = 'user', c_value = {'name' : 'Ahmad'}, condition = {'email' : '1'})
            self.fixture.when_update_user_data_is_called()
            self.fixture.then_result_should_be(False)
        
        def test_delete_user_data(self):
            self.fixture.given_delete_user_data(table = 'user', condition = {'key' : 'value'})
            self.fixture.when_delete_user_data_is_called()
            self.fixture.then_result_should_be(True)
        
        def test_invalid_condition_for_delete_user_data(self):
            self.fixture.given_invalid_condition_for_delete_user_data(table = 'user', condition = {'email' : 123})
            self.fixture.when_delete_user_data_is_called()
            self.fixture.then_result_should_be(False)
        
        def test_invalid_column_for_delete_user_data(self):
            self.fixture.given_invalid_table_for_delete_user_data(table = 'user2', condition = {'key' : 'value'})
            self.fixture.when_delete_user_data_is_called()
            self.fixture.then_result_should_be(False)
        
    
            
        class _Fixture(unittest.TestCase):
            def __init__(self) -> None:
                self.database = Database()
                self.user = User()
            
            def given_no_data(self):
                 pass
                
            def given_required_fields(self, name, email, password, *args):
                self.name = name
                self.email = email
                self.password = password
                self.args = args
                
            def given_optional_fields(self, name, email, password, city, age):
                self.name = name
                self.email = email
                self.password = password
                self.city = city
                self.age = age
                
            def given_existant_user(self, name, email, password, *args):
                self.name = name
                self.email = email
                self.password = password
                self.args = args
                
            def given_weak_password(self, name, email, password, *args):
                self.name = name
                self.email = email
                self.password = password
                self.args = args
                
            def given_invalid_email(self, name, email, password, *args):
                self.name = name
                self.email = email
                self.password = password
                self.args = args
                
            def given_invalid_name(self, name, email, password, *args):
                self.name = name
                self.email = email
                self.password = password
                self.args = args
             
            def given_invalid_table_name(self, t_name, c_name, condition):
                self.t_name = t_name
                self.c_name = c_name
                self.condition = condition   
            
            def given_fetch_user_data(self, t_name, c_name, condition):
                self.t_name = t_name
                self.c_name = c_name
                self.condition = condition
            
            def given_invalid_column_name_for_fetch_user_data(self, t_name, c_name, condition):
                self.t_name = t_name
                self.c_name = c_name
                self.condition = condition
                
            def given_invalid_condition_for_fetch_user_data(self, t_name, c_name, condition):
                self.t_name = t_name
                self.c_name = c_name
                self.condition = condition
                
            def given_update_user_data(self, t_name, c_value, condition):
                self.t_name = t_name
                self.c_value = c_value
                self.condition = condition
                
            def given_invalid_table_name_for_update_user_data(self, t_name, c_value, condition):
                self.t_name = t_name
                self.c_value = c_value
                self.condition = condition
                
            def given_invalid_column_name_for_update_user_data(self, t_name, c_value, condition):
                self.t_name = t_name
                self.c_value = c_value
                self.condition = condition
                
            def given_invalid_value_for_update_user_data(self, t_name, c_value, condition):
                self.t_name = t_name
                self.c_value = c_value
                self.condition = condition
                 
            def given_invalid_condition_for_update_user_data(self, t_name, c_value, condition): 
                self.t_name = t_name
                self.c_value = c_value
                self.condition = condition
                
            def given_delete_user_data(self, t_name, condition):
                self.t_name = t_name
                self.condition = condition
                
            def given_invalid_condition_for_delete_user_data(self, t_name, condition):
                self.t_name = t_name
                self.condition = condition
                
            def given_invalid_table_for_delete_user_data(self, t_name, condition):
                self.t_name = t_name
                self.condition = condition
                
            def when_connection_established(self):
                self.result = self.database.connection(self.conn)
                
            def when_create_user_is_called(self):
                self.result = self.user.create(self.name, self.email, self.password, self.args)  
            
            def when_fetch_user_data_is_called(self):
                self.result = self.user.fetch(self.t_name, self.c_name, self.condition)
                         
            def when_update_user_data_is_called(self):
                try:
                    self.result = self.user.update(self.t_name, self.c_value, self.condition)
                except Exception as e:
                    # get name of that exception
                    # self.exception_name=""
                    pass
                         
            def when_delete_user_data_is_called(self):
                self.result = self.user.delete(self.t_name, self.condition)
                         
            def then_result_should_be(self, expected_result):
                self.assertAlmostEqual(self.result, expected_result)
            
            
if __name__ == '__main__':
    unittest.main()
                
        