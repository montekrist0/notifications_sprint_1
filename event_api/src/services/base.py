import orjson

from db.channels.rabbitmq import send_to_rabbitmq


class BaseService:
    def __init__(self, rabbitmq_queue):
        self.rabbitmq_queue = rabbitmq_queue

    async def send_event(self, data: dict | list[dict]):
        data = orjson.dumps(data)
        await send_to_rabbitmq(self.rabbitmq_queue, data)


class BaseContextCollectService:
    pass