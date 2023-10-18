import json
from django.http import JsonResponse
from posts.models import Posts, PostsComments
from django.views import View


def create_posts(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post = data.get('post', None)
        text = data.get('text', None)

        if post is not None:
            new_post = Posts.objects.create(post=post, text=text)
            return JsonResponse({'message': 'Post created successfully', 'post_id': new_post.id})
        else:
            return JsonResponse({'message': 'Invalid data. Post data is missing.'}, status=400)
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)




def create_comments(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        post_id = data.get('post_id', '')
        comments = data.get('comments', '')

        if post_id is not None:
            post = PostsComments(post_id=post_id, text=comments)
            post.save()
            return JsonResponse({'message': 'Comments created successfully'})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)


def get_comment(request, post_id):
    if request.method == 'GET':
        post = Posts.objects.get(id=post_id)
        comments = PostsComments.objects.filter(post=post)

        comments_list = [{'text': comment.text} for comment in comments]

        return JsonResponse({'comments': comments_list})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)