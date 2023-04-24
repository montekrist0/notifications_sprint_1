import aiormq

from core.configs import settings

connection: aiormq.Connection | None = None
channel: aiormq.Channel | None = None


async def create_connection_rabbitmq():
    connection_ = await aiormq.connect(
        f'amqp://{settings.rabbitmq_username}:{settings.rabbitmq_password}@{settings.rabbitmq_host}:{settings.rabbitmq_port}/')
    return connection_


async def create_channel_rabbitmq(connection_):
    channel_ = await connection_.channel()
    return channel_


async def init_queues(channel_: aiormq.Channel):
    await channel_.queue_declare(queue=settings.rabbitmq_queue_send_welcome, durable=True)
    await channel_.queue_declare(queue=settings.rabbitmq_queue_send_like, durable=True)
    await channel_.queue_declare(queue=settings.rabbitmq_queue_send_personal_selection, durable=True)
    await channel_.queue_declare(queue=settings.rabbitmq_queue_send_bulk_mails, durable=True)
    await channel_.queue_declare(queue=settings.rabbitmq_queue_send_mail, durable=True)


async def send_to_rabbitmq(routing_key, body):
    message_properties = aiormq.spec.Basic.Properties(delivery_mode=settings.rabbitmq_delivery_mode)
    await channel.basic_publish(exchange='', routing_key=routing_key, body=body, properties=message_properties)

