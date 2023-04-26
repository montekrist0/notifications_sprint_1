import asyncio

import aiormq
from core.config import (broker_url, settings_queue)
from services.message_handlers import (event_welcome,
                                       event_like,
                                       event_personal_selection)


async def base_event_handler(connection_path_: str, queue: str, func_consumer):
    connection = await aiormq.connect(connection_path_)
    channel = await connection.channel()
    await channel.basic_qos(prefetch_count=1)
    await channel.basic_consume(queue, func_consumer, no_ack=True)


async def main():
    tasks = [asyncio.create_task(base_event_handler(broker_url,
                                                    settings_queue.rabbitmq_queue_send_welcome,
                                                    event_welcome)),
             asyncio.create_task(base_event_handler(broker_url,
                                                    settings_queue.rabbitmq_queue_send_like,
                                                    event_like)),
             asyncio.create_task(base_event_handler(broker_url,
                                                    settings_queue.rabbitmq_queue_send_personal_selection,
                                                    event_personal_selection))
             ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
