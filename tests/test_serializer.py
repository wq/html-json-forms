from rest_framework.test import APITestCase
from tests.test_app.models import Parent


class RestTestCase(APITestCase):
    def test_submit(self):
        response = self.client.post('/parents/', {
            'name': 'Test',
            'children[0][name]': 'Test 1',
            'children[1][name]': 'Test 2',
        })
        p = Parent.objects.first()
        self.assertEqual(
            {
                'id': p.pk,
                'name': 'Test',
                'children': [
                    {
                        'id': p.children.first().pk,
                        'name': 'Test 1',
                    },
                    {
                        'id': p.children.last().pk,
                        'name': 'Test 2',
                    },
                ]
            },
            response.data
        )
