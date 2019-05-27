import unittest


class TestcaseDemo(unittest.TestCase):

    def setUp(self):
        print("i will run befire every test")

    def test_1(self):
        print("i am test in 1")
    def test_2(self):
        print("i am in test 2")

    def tearDown(self):
        print("i will run after every test")


if __name__ == '__main__':
    unittest.main(verbosity=2)
