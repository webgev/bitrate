from django.test import TestCase
from .models import Rate, Currency

class RateTestCase(TestCase):
    def setUp(self):
        Currency.objects.create(name="BTC")
        Currency.objects.create(name="ETH")
        Currency.objects.create(name="XRP")

    def test_currency_list(self):
        currency_list = Currency.get_list()
        self.assertIsInstance(currency_list, list, "not list")
        self.assertEqual(len(currency_list), 3, "не работает метод get_list")

        currency_list_page2 = Currency.get_list(page=1, limit=1)
        self.assertIsInstance(currency_list_page2, list, "not list")
        self.assertEqual(len(currency_list_page2), 1, "не работает пагинация")
        self.assertNotEqual(currency_list[0]["name"], currency_list_page2[0]["name"], "не работает пагинация")

        currency_list_one = Currency.get_list(limit=1)
        self.assertIsInstance(currency_list_one, list, "not list")
        self.assertEqual(len(currency_list_one), 1, "не работает лимит")


        currency_list_page_and_limit = Currency.get_list(limit=1, page=1)
        self.assertIsInstance(currency_list_page_and_limit, list, "not list")
        self.assertEqual(len(currency_list_page_and_limit), 1, "не работает лимит")
        self.assertEqual(currency_list_page_and_limit[0]["name"], "ETH", "не работает лимит с пагинацией")

    def test_rate(self):
        currency_list = Currency.get_list(limit=1)
        
        rate = Rate.get_last_rate(currency_list[0]["id"])
        self.assertIsNotNone(rate, "не загрузились данные по курсам")
        Rate.get_mean_volume(1)
        
