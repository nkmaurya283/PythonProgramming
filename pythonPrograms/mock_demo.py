from unittest1 import TestCase, mock

from pythonPrograms.mock import work_on


class TestWorkMockingModule(TestCase):

    def test_using_context_manager(self):
        with mock.patch('work.os') as mocked_os:
            work_on()
            mocked_os.getcwd.assert_called_once()
