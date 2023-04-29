import asyncio

import aiormq
from core.config import (broker_url,
                         settings_queue)
from services.message_handlers_service import get_event_handler_service


async def base_event_handler(connection_path_: str, queue: str, func_consumer):
    connection = await aiormq.connect(connection_path_)
    channel = await connection.channel()
    await channel.basic_qos(prefetch_count=1)
    await channel.basic_consume(queue, func_consumer, no_ack=True)


async def main():
    event_handler_service = get_event_handler_service()
    tasks = [
        asyncio.create_task(
            base_event_handler(
                broker_url,
                settings_queue.rabbitmq_queue_send_welcome,
                event_handler_service.handler_event_welcome,
            )
        ),
        asyncio.create_task(
            base_event_handler(
                broker_url,
                settings_queue.rabbitmq_queue_send_personal_selection,
                event_handler_service.handler_event_personal_selection,
            )
        ),
        asyncio.create_task(
            base_event_handler(
                broker_url,
                settings_queue.rabbitmq_queue_send_bulk_mails,
                event_handler_service.handler_event_bulk_mails,
            )
        ),
        asyncio.create_task(
            base_event_handler(
                broker_url,
                settings_queue.rabbitmq_queue_send_mail,
                event_handler_service.handler_event_mail,
            )
        ),
        asyncio.create_task(
            base_event_handler(
                broker_url,
                settings_queue.rabbitmq_queue_send_like,
                event_handler_service.handler_event_like,
            )
        ),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
