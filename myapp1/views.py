from django.shortcuts import render

from myapp1.models import TelegramUsers


# Create your views here.
# MODEL-VIEW-TEMPLATE

def show_index_page(request):
    """
    some_users = TelegramUsers.objects.filter(wallet=100) # WHERE
    print(some_users)

    all_users = TelegramUsers.objects.all()
    print(all_users)

    new_user = TelegramUsers(user_id='312412512', username='cat2', wallet=500)
    new_user.save()

    for user in all_users:
        print(user.user_id, user.username, user.wallet)

    user_to_change = TelegramUsers.objects.get(id=1)
    user_to_change.username = 'rat'
    user_to_change.save()
    """

    TelegramUsers.objects.get(id=1).delete()

    return render(request, 'index.html')

