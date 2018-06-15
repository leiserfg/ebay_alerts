from django.test import TestCase

from alerts.models import Alert


class AlertTestCase(TestCase):
    def test_create_alert_with_email(self):
        alert = Alert.create_with_email(
            'user@email.com', search_terms='knife', frequency=2)
        self.assertEqual(alert.search_terms, 'knife')
        self.assertEqual(alert.frequency, 2)
        self.assertEqual(alert.owner.email, 'user@email.com')

    def test_create_alert_dont_recreate_owner(self):
        alert1 = Alert.create_with_email(
            'user@email.com', search_terms='knife', frequency=2)

        alert2 = Alert.create_with_email(
            'user@email.com', search_terms='pan', frequency=10)

        self.assertEqual(alert1.owner, alert2.owner)
        self.assertEqual(alert1.owner.alerts.count(), 2)
