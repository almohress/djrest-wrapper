from django.test import TestCase
from .models import ExampleModel
from .service import ExampleService


class ExampleServiceTestCase(TestCase):
    def setUp(self):
        pass

    def test_service_successful_init(self):
        service = ExampleService(ExampleModel)
        self.assertIsNotNone(service)

    def test_service_fail_init(self):
        service = None
        try:
            service = ExampleService(ExampleModel)
        except Exception as e:
            self.assertIsNone(service)
