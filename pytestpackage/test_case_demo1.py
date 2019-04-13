
import  pytest

@pytest.fixture()
def setUp():
    print("once before every method")

def testMethodA(setUp):
    print('Running method from A')

def testMethodB(setUp):
    print('Running method from B')