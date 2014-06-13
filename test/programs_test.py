import tests
import utils


class ProgramsTestCase (tests.TestCase):

    def test_get_programs (self):
        self.assertTrue(True)


def suite ():
    return ProgramsTestCase.get_suite()


def main (**kwargs):
    return ProgramsTestCase.run_tests(**kwargs)


if __name__ == '__main__':
    main(**utils.args)
