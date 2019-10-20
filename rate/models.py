from django.db import models
from django.db.models.signals import post_save
from . import get_rate

class Currency(models.Model):
    """
    Модель Currency
    """
    name = models.CharField(max_length=120, unique=True)
    
    def __str__(self):
        return self.name

    @staticmethod
    def get_list(limit=10, page=0) -> list:
        """ 
        Вернет список валют
        @param limit - количество валют
        @param page - номер страницы 

        @return list - список валют.
        """
        offset = page*limit
        return list(Currency.objects.all()[offset:limit+offset].values())

class Rate(models.Model):
    """
    Модель Rate
    """
    currency = models.ForeignKey('Currency', on_delete=models.CASCADE)
    date = models.DateField()
    rate = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
        return f"{self.currency.name} {self.rate} {self.volume} {str(self.date)}"
           
    @staticmethod
    def get_last_rate(currency_id: int) -> float:
        """ 
        Вернет последний курс валюты
        @param currency_id - идентификатор валюты

        @return rate
        """
        rate = Rate.objects.filter(currency_id=currency_id).values('rate').order_by('-date')[:1]
        return rate[0]['rate'] if rate else None

    @staticmethod
    def get_mean_volume(currency_id: int) -> float:
        """ 
        Вернет средний объем торгов за последние 10 дней
        @param currency_id - идентификатор валюты

        @return volumes_sum / 10
        """
        volumes = Rate.objects.filter(currency_id=currency_id).values('volume').order_by('-date')[:10]
        volumes_sum = 0
        for v in volumes:
            volumes_sum += v["volume"]
        return volumes_sum / 10
    
    @staticmethod
    def refresh_by_currency(currency: 'Currency'):
        """
        Обновит данные по конкретной валюте
        """
        if not currency or not isinstance(currency, Currency):
            return
        rate_data = get_rate(currency.name)
        for item in rate_data:
            Rate.objects.update_or_create(defaults=item,  date=item["date"], currency_id=currency.id)

    @staticmethod
    def refresh_all():
        """
        Обновит данные по всем валютам
        """
        curs = Currency.objects.all()
        for cur in curs:
            Rate.refresh_by_currency(cur)


def currency_handler_save(**kwargs):
    # при сохранении валюты обновим данные курса
    inst = kwargs["instance"]
    Rate.refresh_by_currency(inst)
# подписываемся на событие сохранения валюты
post_save.connect(currency_handler_save, sender=Currency)
