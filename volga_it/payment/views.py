import json
from django.http import JsonResponse
from rest_framework.decorators import api_view

from users.models import CustomUser


def change_balance(pk):
    """Функция для изменения баланса пользователя"""
    hesoyam = 250000
    user = CustomUser.objects.get(id=pk)
    user.balance += hesoyam
    user.save()


@api_view(['POST'])
def payment_controller(request, pk):
    """Функция для изменения баланса себе или всем пользователям"""
    if request.user.is_staff:
        body = json.loads(request.body)
        choice = body.get('choice')
        if choice == 'Всем':
            users_ids = CustomUser.objects.values_list('id', flat=True)
            for user_id in users_ids:
                change_balance(user_id)
            message = {
                'message': 'Вы успешно добавили на счета всех пользователей 250.000$!'
            }
        elif choice == 'Себе':
            change_balance(pk)
            message = {
                'message': 'Вы успешно добавили на свой баланс 250.000$!'
            }
        else:
            message = {
                'message': 'Вы допустили ошибку, выберите кому вы хотите изменить баланс(Себе или Всем)!'
            }
    elif request.user.is_authenticated:
        change_balance(pk)
        message = {
            'message': 'Вы успешно добавили на свой баланс 250.000$!'
        }
    return JsonResponse(message, status=200)
