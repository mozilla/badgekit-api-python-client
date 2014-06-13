import tests
import utils


class IssuersTestCase (tests.TestCase):

    def test_get_issuers (self):
        self.assertTrue(True)


def suite ():
    return IssuersTestCase.get_suite()


def main (**kwargs):
    return IssuersTestCase.run_tests(**kwargs)


if __name__ == '__main__':
    main(**utils.args)
