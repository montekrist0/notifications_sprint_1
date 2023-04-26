from fastapi import APIRouter, Depends, Response, status
from services.user_preference_service import (
    UserPreferenceService,
    get_user_pref_service,
)
from view.api.v1.models import UserInfo, UserPreferenceInput

router = APIRouter()


@router.get(
    "/users/{user_id}",
    response_model=UserInfo,
    summary="Получение информации о пользователе",
)
async def get_likes_list_for_film(
    user_id: str,
    user_pref_service: UserPreferenceService = Depends(get_user_pref_service),
):
    user_info = await user_pref_service.get_user_info(user_id)
    return UserInfo.parse_obj(user_info)


@router.patch(
    "/users/{user_id}",
    response_model=UserInfo,
    summary="Обновление записи о пользователе",
)
async def change_rating_film(
    user_id: str,
    preferences_params: UserPreferenceInput,
    user_pref_service: UserPreferenceService = Depends(get_user_pref_service),
):
    update_result = await user_pref_service.set_user_preference(
        user_id, dict(preferences_params)
    )
    if update_result:
        return Response("Preferences were updated", status_code=status.HTTP_200_OK)

    return Response(
        "Preferences were not updated", status_code=status.HTTP_304_NOT_MODIFIED
    )
