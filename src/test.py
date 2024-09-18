import unittest
from main import Main

# Unit Test for the three important sections
class Test(unittest.TestCase):

    def setUp(self):
        self.app = Main('test.yml', 10)  
        self.data = self.app.load_endpoints()   

    def test_load_endpoints(self):
        self.assertIsInstance(self.data, list)  
        self.assertGreater(len(self.data), 0)   

    def test_check_endpoints(self):
        for endpoint in self.data:
            self.app.status = self.app.check_status.check_endpoint(endpoint)
            self.assertIn(self.app.status, ['UP', 'DOWN'])  

    def test_print_logs(self):
        self.app.check_status.print_logs()     

if __name__ == '__main__':
    unittest.main()