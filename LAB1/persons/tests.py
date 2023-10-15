import unittest

from django.test import TestCase, Client
from django.urls import reverse


class TestView(TestCase):

    def setUp(self):
        self.client = Client()
        self.all = reverse('persons')
        self.data = {
            'name': 'test_name',
            'age': 999,
            'address': 'test_address',
            'work': 'test_work',
        }

        self.patched_data = {
            'name': 'patched_name',
            'age': 7,
            'address': 'patched_address',
            'work': 'patched_work',
        }

        self.invalid_data = {
            'data': 'invalid',
        }

    def test_GET_all(self):

        request = self.client.get(self.all)

        self.assertEqual(request.status_code, 200)

    def test_POST_new(self):

        request = self.client.post(self.all, self.data, content_type='application/json')

        self.assertEqual(request.status_code, 201)

    def test_POST_invalid(self):

        request = self.client.post(self.all, self.invalid_data, content_type='application/json')

        self.assertEqual(request.status_code, 400)

    def test_GET_existing(self):

        request = self.client.post(self.all, self.data, content_type='application/json')

        location = request.headers["Location"]
        created_id = int(location[location.rfind("/") + 1:])

        request = self.client.get(reverse('record', args=[created_id]))

        self.assertEqual(request.status_code, 200)

    def test_PATCH(self):

        request = self.client.post(self.all, self.data, content_type='application/json')

        location = request.headers["Location"]
        created_id = int(location[location.rfind("/") + 1:])

        request = self.client.patch(reverse('record', args=[created_id]), self.patched_data, content_type='application/json')

        self.assertEqual(request.status_code, 200)

    def test_DELETE(self):

        request = self.client.post(self.all, self.data, content_type='application/json')

        location = request.headers["Location"]
        created_id = int(location[location.rfind("/") + 1:])

        request = self.client.delete(reverse('record', args=[created_id]))

        self.assertEqual(request.status_code, 204)


if __name__ == '__main__':
    unittest.main()
