import unittest



class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("i will run before every method")

    def test_methodA(self):
        print("i ma in method A")

    def test_methodB(self):
        print("I am in method B")

    def tearDown(self):
        print("I will run after every test")


if __name__ == '__main__':
    unittest.main()

