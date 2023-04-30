from fastapi import APIRouter, Depends, HTTPException, Response, status

from view.models import BulkMails, Like, Mail, PersonalSelection, Welcome

from services.like import LikeService, get_like_service
from services.welcome import WelcomeService, get_welcome_service
from services.mail import MailService, get_mail_service
from services.bulk_mails import BulkMailsService, get_bulk_mails_service
from services.personal_selection import (
    PersonalSelectionService,
    get_personal_selection_service,
)

router = APIRouter()


@router.post('/send-welcome', summary='Отправка приветственного письма')
async def send_welcome(
    data: Welcome, service: WelcomeService = Depends(get_welcome_service)
):
    await service.send_event(data.dict())


@router.post('/send-like', summary='Поставили лайк')
async def send_like(data: Like, service: LikeService = Depends(get_like_service)):
    await service.send_event(data.dict())


@router.post('/send-personal_selection', summary='Персональная подборка')
async def send_personal_selection(
    dates: list[PersonalSelection],
    service: PersonalSelectionService = Depends(get_personal_selection_service),
):
    await service.send_event([date.dict() for date in dates])


@router.post('/send-bulk_mails', summary='Массовая рассылка')
async def send_bulk_mails(
    data: BulkMails, service: BulkMailsService = Depends(get_bulk_mails_service)
):
    await service.send_event(data.dict())


@router.post('/send-mail', summary='Индивидуальная рассылка')
async def send_mail(data: Mail, service: MailService = Depends(get_mail_service)):
    await service.send_event(data.dict())
