from django.shortcuts import render
from .models import Post
from .models import Ekipa
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, "blog/post_list.html", {"posts" : posts})

def ekipa_list(request):
    uzytkownicy = Ekipa.objects.all()
    return render(request, "blog/ekipa_list.html", {"uzytkownicy" : uzytkownicy})
