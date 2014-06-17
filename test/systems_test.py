from remote import ResourceNotFoundError, MethodNotAllowedError
import tests
import utils


class SystemsTestCase (tests.TestCase):

    def test_get_systems (self):
        systems = self.client.get_systems()

    def test_get_system (self):
        system = self.client.get_system(system='chicago')

        self.assertEqual(system['slug'], 'chicago')
        self.assertRaises(ResourceNotFoundError, self.client.get_system, system='not-found')


def suite ():
    return SystemsTestCase.get_suite()


def main (**kwargs):
    return SystemsTestCase.run_tests(**kwargs)


if __name__ == '__main__':
    main(**utils.args)
