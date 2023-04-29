import sentry_sdk
import uvicorn
from core.configs import settings
from db.clients import mongo
from fastapi import FastAPI
from view.api.v1 import user_preference

# sentry_sdk.init(
#     dsn=settings.sentry_dsn,
#     traces_sample_rate=settings.traces_sample_rate,
# )

app = FastAPI(
    title="API для управления пользовательскими предпочтениями по получению уведомлений",
    docs_url="/api/openapi",
    openapi_url="/api/openapi.json",
    description="API для управления пользовательскими предпочтениями по получению уведомлений",
    version="1.0.0",
)


app.include_router(
    user_preference.router,
    prefix="/api/v1/notification_preference",
    tags=["User Preference"],
)


@app.on_event("startup")
def startup():
    mongo.client = mongo.create_mongo_client()


@app.on_event("shutdown")
def shutdown():
    mongo.client.close()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True)
