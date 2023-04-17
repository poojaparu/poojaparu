from newapp.models import Course
def menu_links(request):
    links=Course.objects.all()
    return dict(links=links)