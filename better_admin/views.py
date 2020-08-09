from agatka.useful import *

def Better_admin(request):
    if not request.user.is_superuser:
        return Login(request)
    else:
        ctx = set_navname("admin", base_context(request))
        return render(request, "admin.html", ctx)

def Login(request):
    return redirect('/admin/panel/login/?next=/admin/')