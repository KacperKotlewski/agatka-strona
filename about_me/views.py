from agatka.useful import *

def About_Me(request):
    ctx = set_navname("about_me", base_context(request))
    # messages.info(request, 'Your password has been changed successfully!')
    return render(request, "about.html", ctx)