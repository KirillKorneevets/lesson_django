import json
from django.http import JsonResponse
from posts.models import User
from django.shortcuts import get_object_or_404
from django.views import View


class UserViews(View):

    def post(self, request):
        if request.method == 'POST':
            data = json.loads(request.body)
            username = data.get('username', '')
            age = data.get('age', '')

            new_user = User(username=username, age=age)
            new_user.save()
        
            return JsonResponse({'message': 'User created successfully'})
        else:
            return JsonResponse({'message': 'Invalid data'}, status=400)
    
    def get(self, request, user_id=None):
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
        
    def put(self, request, user_id):
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
    
    def delete(self, request, user_id):  
        if request.method == 'DELETE':
            user = User.objects.filter(id=user_id).first()
            if user:
                user.delete()
                return JsonResponse({'message': 'User deleted successfully'})
            else:
                return JsonResponse({'message': 'User not found'}, status=404)
        else:
            return JsonResponse({'message': 'Invalid request method'}, status=400)
