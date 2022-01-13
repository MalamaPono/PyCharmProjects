import unittest
from person import Person

class TestPerson(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("SetUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print('setUp')
        self.per1 = Person("Koa",16)
        self.per2 = Person("Keli'i",10)

    def tearDown(self):
        print('tearDown\n')

    def test_constructor(self):
        self.assertEqual(self.per1.name,'Koa')
        self.assertEqual(self.per1.age,16)

        self.assertEqual(self.per2.name, "Keli'i")
        self.assertEqual(self.per2.age, 10)

    def test_agemultiplier(self):
        self.assertEqual(self.per1.getMultipliedAge(),24)

    def test_string(self):
        self.assertEqual(self.per1.__str__(), "My name is Koa and I am 16 years old.")

if __name__ == '__main__':
    unittest.main()