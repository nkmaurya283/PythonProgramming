import  unittest

class AssertDemo(unittest.TestCase):


    def test_assertTrueFalse(self):
        a=True

        self.test_assertTrue(a,"a is not false")
        b=False
        self.assertFalse(b, "b is not true")


    def test_assertEqual(self):
        a="Test"
        b="Test"
        self.assertEqual(a,b, "'a' is not equal to 'b'")

