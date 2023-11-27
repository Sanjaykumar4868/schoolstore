from . models import Department,Course

def menu_links(request):
    links = Department.objects.all()
    return dict(links=links)


# def menu_link(request):
#     link = Course.objects.all().filter(department = True)
#     return dict(link=link)