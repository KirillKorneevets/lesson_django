from django.shortcuts import render
from django.http import JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404


def create_posts(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        age = request.POST.get('age', '')

        new_user = User(username=username, age=age)
        new_user.save()
        
        return JsonResponse({'message': 'User created successfully'})
    else:
        return JsonResponse({'message': 'Invalid data'}, status=400)
    
def get_posts(request, user_id=None):
    if request.method == 'GET':
        if user_id is not None:
            user = get_object_or_404(User, id=user_id)
            data = {'username': user.username, 'age': user.age}
        else:
            users = User.objects.all()
            data = [{'id': user.id, 'username': user.username, 'age': user.age} for user in users]
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({'message': 'Invalid data'}, status=400)















# def create_post(request):
#     res = {
#           'data': []
#     }
#     posts = Posts.objects.all()
#     for i in posts:
#           res['data'].append({'title': i.title, 'text': i.text})
#     return JsonResponse(res)