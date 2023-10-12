import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import Posts, User, PostsComments
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404




def create_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username', '')
        age = data.get('age', '')

        new_user = User(username=username, age=age)
        new_user.save()
        
        return JsonResponse({'message': 'User created successfully'})
    else:
        return JsonResponse({'message': 'Invalid data'}, status=400)
    
def get_user(request, user_id=None):
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
    
def update_user(request, user_id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            username = data.get('username', '')
            age = data.get('age', '')

            user = User.objects.filter(id=user_id).first()
            if user:
                user.username = username
                user.age = age
                user.save()
                return JsonResponse({'message': 'User updated successfully'})
            else:
                return JsonResponse({'message': 'User not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
    
def delete_user(request, user_id):
    if request.method == 'DELETE':
        user = User.objects.filter(id=user_id).first()
        if user:
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'})
        else:
            return JsonResponse({'message': 'User not found'}, status=404)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)
