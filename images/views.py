from agatka.useful import *

def Images(request, image, category="none", group="none"):
    ctx = set_navname("about_me", base_context(request))
    # messages.info(request, 'Your password has been changed successfully!')
    return render(request, "about.html", ctx)