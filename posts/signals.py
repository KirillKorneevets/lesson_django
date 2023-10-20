from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models import User, Wallet


@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        Wallet.objects.create(user=instance, balance=0)


    # sender: Этот аргумент указывает на класс модели, который инициировал событие. В данном случае, это модель User.
    # instance: Этот аргумент представляет конкретный экземпляр объекта модели, который был сохранен. В данном случае, это новый пользователь, который был создан
    # created: Этот аргумент - булевое значение, которое указывает, был ли объект только что создан (True) или обновлен (False).