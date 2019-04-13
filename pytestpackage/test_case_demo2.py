
import  pytest

@pytest.yield_fixture()
def setUp():
    print("once before every method")
    yield
    print("After the test")

def testMethodA(setUp):
    print('Running method from A')

def testMethodB(setUp):
    print('Running method from B')