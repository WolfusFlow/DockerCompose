from django.http import HttpResponse
import datetime

#table("value: ")(value)(time???)
def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
