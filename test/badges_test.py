from remote import ResourceNotFoundError, MethodNotAllowedError, ValidationError
import tests
import utils


class BadgesTestCase (tests.TestCase):

    def test_get_badges (self):
        """Get all badges"""
        badges = self.client.get_badges(system='chicago')

        self.assertEqual(len(badges), 3)

    def test_get_all_badges (self):
        """Get all badges, including archived"""
        badges = self.client.get_all_badges(system='chicago')

        self.assertEqual(len(badges), 4)

    def test_get_valid_badge (self):
        """Get valid badge"""
        badge = self.client.get_badge(system='chicago', badge='badge')

        self.assertEqual(badge['slug'], 'badge')

    def test_get_invalid_badge (self):
        """Get invalid badge"""
        self.assertRaises(ResourceNotFoundError, self.client.get_badge,
                            system='chicago', badge='not-found')

    def test_get_badge_in_wrong_context (self):
        """Get badge in wrong context"""
        badge = self.client.get_badge(system='chicago', badge='scratch')

        self.assertNotEqual(badge._parent['slug'], 'chicago')

    def test_create_new_badge (self):
        """Create new badge"""
        badge = {
            'name': 'Test Badge',
            'slug': 'test',
            'earnerDescription': 'Earner Description',
            'consumerDescription': 'Consumer Description',
            'criteriaUrl': 'http://example.org/criteria',
            'unique': False,
            'image': 'http://example.org/badge.png',
            'type': 'test',
        }

        self.client.create_badge(system='chicago', badge=badge);

    def test_create_invalid_badge (self):
        """Create invalid badge"""

        self.assertRaises(ValidationError, self.client.create_badge,
                            system='chicago', badge={})

    def test_update_badge (self):
        """Update badge"""

        badge_data = {
            'name': 'Updated',
            'slug': 'badge',
        }

        badge = self.client.update_badge(system='chicago', badge=badge_data)
        self.assertEqual(badge['name'], badge_data['name'])

    def test_delete_badge (self):
        """Delete badge"""
        badge = self.client.delete_badge(system='chicago', badge='badge')

        self.assertEqual(badge['slug'], 'badge')

        self.assertRaises(ResourceNotFoundError, self.client.delete_badge,
                            system='chicago', badge='badge')


def suite ():
    return BadgesTestCase.get_suite()


def main (**kwargs):
    return BadgesTestCase.run_tests(**kwargs)


if __name__ == '__main__':
    main(**utils.args)
