from django.shortcuts import render
from django.http import JsonResponse

POSTS = [
    {
        'title':'first post',
        'text': 'This is my first post',
    },
    {
        'title':'second post',
        'text': 'This is my second post',
    }
]

def get_posts(request):
    all_posts = []

    for post in POSTS:
        all_posts.append(post)

    return JsonResponse(all_posts, safe=False)