from django.shortcuts import render

def index(request):
	template_name= 'index.html'
	nombres=['Juan', 'Ceci', 'Marcos']
	contexto = {'nombres': nombres}
	return render(request, template_name,contexto)