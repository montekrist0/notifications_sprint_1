from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    rabbitmq_host: str = Field(default='localhost')
    rabbitmq_port: int = Field(default=5672)
    rabbitmq_username: str = Field(default='admin')
    rabbitmq_password: str = Field(default='admin')
    rabbitmq_delivery_mode: int = Field(default=2)

    rabbitmq_queue_send_welcome: str = Field(default='emails.send-welcome')
    rabbitmq_queue_send_like: str = Field(default='emails.send-like')
    rabbitmq_queue_send_personal_selection: str = Field(
        default='emails.send-personal_selection'
    )
    rabbitmq_queue_send_bulk_mails: str = Field(default='emails.send-bulk_mails')
    rabbitmq_queue_send_mail: str = Field(default='emails.send-mail')


settings = Settings()
