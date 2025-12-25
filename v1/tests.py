from django.test import RequestFactory, SimpleTestCase
from django.utils import translation

from v1.utils.i18n import activate_request_language


class ActivateRequestLanguageTests(SimpleTestCase):
    def setUp(self):
        self.factory = RequestFactory()
        translation.activate("en")

    def tearDown(self):
        translation.deactivate()

    def test_prefers_query_param_over_prefix(self):
        request = self.factory.get("/uz/api/v1/about-us/?lang=ru")
        request.LANGUAGE_CODE = "uz"

        activate_request_language(request)

        self.assertEqual(request.LANGUAGE_CODE, "ru")
        self.assertEqual(translation.get_language(), "ru")

    def test_uses_language_prefix_when_no_param(self):
        request = self.factory.get("/kz/api/v1/products/")
        request.LANGUAGE_CODE = "kz"

        activate_request_language(request)

        self.assertEqual(request.LANGUAGE_CODE, "kz")
        self.assertEqual(translation.get_language(), "kz")

    def test_invalid_prefix_keeps_active_language(self):
        translation.activate("en")
        request = self.factory.get("/xx/api/v1/products/")
        request.LANGUAGE_CODE = "xx"

        activate_request_language(request)

        self.assertEqual(request.LANGUAGE_CODE, "en")
        self.assertEqual(translation.get_language(), "en")
