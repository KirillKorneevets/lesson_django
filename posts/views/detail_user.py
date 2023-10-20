from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from posts.models import User
from django.shortcuts import redirect, render
from django.urls import reverse



class DetailUser(View):

    def get(self, request):
        users = User.objects.all()
        template = loader.get_template("user/user.html")
        context = {"users": users}
        rendered_html = template.render(context)
        return HttpResponse(rendered_html)


                
class RegistrationView(View):
    def post(self, request):
        username = request.POST.get('username', '')
        age = request.POST.get('age', '')

        if username and age:
            new_user = User(username=username, age=age)
            new_user.save()
            return redirect('get_users')
        else:
            users = User.objects.all()
            context = {"users": users, "error_message": "Заполните все поля."}
            template = loader.get_template("user/registration_form.html")
            rendered_html = template.render(context)
            return HttpResponse(rendered_html)

    def get(self, request):
        template = loader.get_template("user/registration_form.html")
        rendered_html = template.render()
        return HttpResponse(rendered_html)


class СhangeUser(View):
    def post(self, request):
        user_id = request.POST.get('user_id')
        username = request.POST.get('username', '')
        age = request.POST.get('age', '')
        user = User.objects.filter(id=user_id).first()
        if user:
            user.username = username
            user.age = age
            user.save()
            return redirect('get_users')
        
    def get(self, request):
        return render(request, "user/change_user.html")
