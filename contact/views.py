from agatka.useful import *

def Contact(request):
    ctx = set_navname("contact", base_context(request))
    # messages.info(request, 'Your password has been changed successfully!')
    return render(request, "contact.html", ctx)