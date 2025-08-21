from django.shortcuts import render
from .models import New
# Create your views here.
def base_page_view(request):
    news = New.objects.all()
    context = {
        'news': news,
    }
    return render(request, 'base.html', context)