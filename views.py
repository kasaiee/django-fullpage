from django.shortcuts import render
from models import Section, FullPage, slides as Slides

def index(request):
    fullpage = FullPage.objects.all()[0]
    sections = Section.objects.all()
    slides = Slides.objects.all()
    return render(request, 'index.html',
            {
                'fullpage' : fullpage,
                'sections' : sections,
                'slides' : slides,
            }
        )
