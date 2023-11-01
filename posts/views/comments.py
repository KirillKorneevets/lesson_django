import json
from django.http import JsonResponse
from django.shortcuts import redirect, render
from posts.models import Posts, PostsComments
from posts.django_forms.posts_forms import PostsForm
from posts.django_forms.comments_forms import CommentsForm
from django.views.generic.base import View


class CreatePosts(View):

    def post(self, request):
        form = PostsForm(request.POST)
        if form.is_valid():
            post_data = form.cleaned_data

            new_post = Posts.objects.create(post=post_data['post'], text=post_data['text'])
            
            return redirect('create_posts')
        else:
            return JsonResponse({'message': 'Invalid data'}, status=400)
    
    def get (self, request):
        form = PostsForm()
        return render(request, 'posts_forms.html', {'form': form}) 




class CreateComments(View):
    def post(self, request):
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment_data = form.cleaned_data

            new_comment = PostsComments.objects.create(post_id=comment_data['post_id'], text=comment_data['text'])

            return redirect('create_posts')
        
    def get(self, request):
        form = CommentsForm()
        return render(request, 'comments_forms.html', {'form': form})



def get_comment(request, post_id):
    if request.method == 'GET':
        post = Posts.objects.get(id=post_id)
        comments = PostsComments.objects.filter(post=post)

        comments_list = [{'text': comment.text} for comment in comments]

        return JsonResponse({'comments': comments_list})
    else:
        return JsonResponse({'message': 'Invalid request method'}, status=400)