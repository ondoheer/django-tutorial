from django.forms import ModelForm
from .models import Wine


class WineForm(ModelForm):
	class Meta:
		model = Wine
		fields = [
			"name",
			"vineyard",
			"year",
			"type",
			"country",
			"image",
			"rating",
			"notes",
			
		]