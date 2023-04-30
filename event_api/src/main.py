import uvicorn
from fastapi import FastAPI

from db.channels import rabbitmq
from view.api import events

app = FastAPI(
    title='API для получения событий',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
    description='...',
    version='1.0.0',
)

app.include_router(events.router, prefix='/api/v1/events', tags=['Events'])


@app.on_event('startup')
async def startup():
    rabbitmq.connection = await rabbitmq.create_connection_rabbitmq()
    rabbitmq.channel = await rabbitmq.create_channel_rabbitmq(rabbitmq.connection)
    await rabbitmq.init_queues(rabbitmq.channel)


@app.on_event('shutdown')
def shutdown():
    rabbitmq.connection.close()


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8001, reload=True)
