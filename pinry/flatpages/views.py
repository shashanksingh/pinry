from django.template.response import TemplateResponse


def goodies(request):
	context = {}
	return  TemplateResponse(request , 'pins/goodies.html', context)
