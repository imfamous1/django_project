import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from myapp1.models import TelegramUsers, Roles


def show_index_page(request):
    data = TelegramUsers.objects.all()
    return render(request, 'index.html', context={'data': data})


def show_roles_page(request):
    all_roles = Roles.objects.all()

    # Способ 1. Фильтр через связанное поле
    # users_adm_role = TelegramUsers.objects.filter(role__name='Администратор')

    # Способ 2. Фильтр через предварительно полученный объект
    # role_design = Roles.objects.get(name='Дизайнер')
    # users_designer_role = TelegramUsers.objects.filter(role=role_design)

    # Способ 3. Обратный запрос через Related Manager
    # role_develop = Roles.objects.get(name='Разработчик')
    # users_develop_role = role_develop.telegramusers_set.all()
    # print(users_develop_role)

    return render(request, 'roles.html', context={'data': all_roles})


def get_user_data(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        try:
            user = TelegramUsers.objects.get(user_id=user_id)
            data = {
                'username': user.username,
                'role': user.role.name,
                'user_id': user.user_id,
            }
            return JsonResponse(data)
        except TelegramUsers.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    elif request.method == 'POST':
        return JsonResponse({'data': 'POST IS WORKED'})


@csrf_exempt
def save_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            username = data.get('username', '')

            # Создаем или обновляем пользователя
            user, created = TelegramUsers.objects.update_or_create(
                user_id=user_id,
                defaults={
                    'username': username,
                    # Другие поля можно оставить по умолчанию
                }
            )

            return JsonResponse({
                'status': 'success',
                'user_id': user.user_id,
                'created': created
            })

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def get_all_users(request):
    if request.method == 'GET':
        users = TelegramUsers.objects.all()
        users_list = []

        for user in users:
            users_list.append({
                'user_id': user.user_id,
                'username': user.username,
                'first_name': getattr(user, 'first_name', ''),
                'last_name': getattr(user, 'last_name', '')
            })

        return JsonResponse({'users': users_list})

    return JsonResponse({'error': 'Invalid request method'}, status=405)