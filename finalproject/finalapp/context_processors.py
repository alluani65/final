from.models import Genere
def menu_links(request):
    links=Genere.objects.all()
    return dict(links=links)