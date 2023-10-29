import json
from django.http import JsonResponse
from rest_framework.decorators import api_view

from users.models import CustomUser


def change_balance(user):
    """Функция для изменения баланса пользователя"""
    hesoyam = 250000
    old_user = user
    old_user.balance += hesoyam
    old_user.save()


@api_view(['POST'])
def payment_controller(request, pk):
    """Функция для изменения баланса себе или всем пользователям"""
    try:
        user = CustomUser.objects.get(id=pk)

        if request.user.is_staff:
            body = json.loads(request.body)
            choice = body.get('choice')
            if choice == 'Всем':
                users = CustomUser.objects.all()
                for old_user in users:
                    change_balance(old_user)
                message = {
                    'message': 'Вы успешно добавили на счета всех пользователей 250.000$!'
                }
            elif choice == 'Себе':
                change_balance(user)
                message = {
                    'message': 'Вы успешно добавили на свой баланс 250.000$!'
                }
            else:
                message = {
                    'message': 'Вы допустили ошибку, выберите кому вы хотите изменить баланс(Себе или Всем)!'
                }
        elif request.user.is_authenticated and request.user == user:
            change_balance(user)

            message = {
                'message': 'Вы успешно добавили на свой баланс 250.000$!'
            }
        elif request.user.is_authenticated and request.user != user:
            message = {
                'message': 'Вы можете изменить баланс только себе!'
            }

        return JsonResponse(message, status=200)
    except:
        message = {
            'message': 'Пользователь не найден, попробуйте ещё раз!'
        }

        return JsonResponse(message, status=404)
