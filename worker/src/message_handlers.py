import json

from aiormq.abc import DeliveredMessage


async def event_welcome(message: DeliveredMessage):
    print(f"     Message body is: {message.body!r}")
    # TODO получить по id данные пользователя в сервисе с предпочтениями
    # TODO получить шаблон пиьсьма


async def event_like(message: DeliveredMessage):
    print(f"     Message body is: {message.body!r}")
    # TODO получить по id данные пользователя в сервисе с предпочтениями
    # TODO получить шаблон пиьсьма


async def event_personal_selection(message: DeliveredMessage):
    print(f"     Message body is: {message.body!r}")
    # TODO получить по id данные пользователя в сервисе с предпочтениями
    # TODO получить шаблон пиьсьма


async def event_bulk_mails(message: DeliveredMessage):
    print(f"     Message body is: {message.body!r}")
    # TODO получить по id данные пользователя в сервисе с предпочтениями
    # TODO получить шаблон пиьсьма


async def event_mail(message: DeliveredMessage):
    print(f"     Message body is: {message.body!r}")
    # TODO получить по id данные пользователя в сервисе с предпочтениями
    # TODO получить шаблон пиьсьма
