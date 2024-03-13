from django.shortcuts import render
from django.views import views


class home(View)
     template_name = "produto/index.html"

    def get(self, request, *args, **kwargs)
        return render(request,self.template_name)
