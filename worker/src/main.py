import asyncio

import aiormq
from config import broker_url, settings, value_list_queue
from message_handlers import event_welcome


async def base_event_handler(connection_path_: str, queue: str):
    connection = await aiormq.connect(connection_path_)
    channel = await connection.channel()
    await channel.basic_qos(prefetch_count=1)
    await channel.basic_consume(queue, event_welcome, no_ack=True)


async def main():
    tasks = []
    for queue in value_list_queue:
        task = asyncio.create_task(base_event_handler(broker_url, queue))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_forever()
