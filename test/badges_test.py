import tests
import utils


class BadgesTestCase (tests.TestCase):

    def test_get_all_badges (self):
        badges = self.client.get_all_badges(system='system')

        self.assertEqual(len(badges), 2)

    def test_get_badges (self):
        badges = self.client.get_badges(system='system')

        self.assertEqual(len(badges), 1)


def suite ():
    return BadgesTestCase.get_suite()


def main (**kwargs):
    return BadgesTestCase.run_tests(**kwargs)


if __name__ == '__main__':
    main(**utils.args)
