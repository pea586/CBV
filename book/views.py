from django.shortcuts import render

# Create your views here.


from django.views import View


class BookView(View):

    def get(self, request):
        return HttpResponse('View Get请求...')

    def post(self, request):
        return HttpResponse('View Post请求...')

    def delete(self, request):
        return HttpResponse('View Delete请求...')
