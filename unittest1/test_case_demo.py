import unittest


class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print("*#" *30)
        print("I will run only once before tests")
        print("*#" * 30)

    def setUp(self):
        print("i will run before every method")

    def test_methodA(self):
        print("i ma in method A")

    def test_methodB(self):
        print("I am in method B")

    def tearDown(self):
        print("I will run after every test")

    @classmethod
    def tearDownClass(self):
        print("*#" *30)
        print("I will run only once After tests")
        print("*#" * 30)


if __name__ == '__main__':
    unittest.main(verbosity=2)
