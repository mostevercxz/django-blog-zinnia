from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import Genre

# Create your views here.
def show_genres(request):
    return render_to_response("mptt_model/genres.html", 
            {'nodes':Genre.objects.all()}, 
            context_instance=RequestContext(request))
