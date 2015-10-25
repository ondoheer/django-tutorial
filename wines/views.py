from django.shortcuts import render, get_object_or_404
from django.template import RequestContext, loader
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.views import generic 

from .models import Wine
from .forms import WineForm
# Create your views here.


class IndexView(generic.ListView):
	template_name = "wines/index.html"
	context_object_name = "wines"

	def get_queryset(self):
		return Wine.objects.all()


class SingleWineView(generic.DetailView):
	model = Wine
	template_name = "wines/wine_detail.html"

	def get_context_data(self, **kwargs):
		context = super(SingleWineView, self).get_context_data(**kwargs)
		context["wines"] = Wine.objects.all()
		return context



def add_wine(request):
	"""
	Renders form to add wines"
	"""
	

	if request.method == "POST":

		form = WineForm(request.POST, request.FILES)
		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/wines")

		else:
			print("Didin't validate")
			print(form.errors)
	else:
		form = WineForm()


	return render(request, "wines/add_wine.html", {"form":form})


def edit_wine(request, wine_id):
	"""
	Edits existing wine
	"""
	
	wine = Wine.get_object_or_404(Wine, pk=wine_id)
	form = WineForm(instance=wine)

	return render(request, "wines/edit_wine.html", {"form":form})

