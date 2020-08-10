from agatka.useful import *
import images.models as imagesForms
import images.forms as imagesForms
from django.core.files.storage import FileSystemStorage
        
from django.views.decorators.csrf import csrf_exempt

def Better_admin(request):
    if not request.user.is_superuser:
        return Login(request)
    else:
        ctx = set_navname("admin", base_context(request))
        return render(request, "admin.html", ctx)

def Login(request):
    return redirect('/admin/panel/login/?next=/admin/')



def AddImages(request):
    if not request.user.is_superuser:
        return Login(request)
    else:
        ctx = set_navname("add_images", base_context(request))
        ctx["categories"] = imagesForms.Category.objects.all()
    
        ctx["categories_select"] = "none"
        ctx["groups_select"] = "none"
        if request.method == "POST":
            for item in request.method.items():
                print(item)
            ctx["categories_select"] = request.POST.get("categories_select", "none")
            ctx["groups_select"] = request.POST.get("groups_select", "none")
        return render(request, "add_images/main.html", ctx)


@csrf_exempt
def GetGroups(request):
    if request.method == 'GET':
        category = request.GET["category"]
        cat = imagesForms.Category.objects.filter(id=category)[0]
        grp = imagesForms.Group.objects.filter(category=cat)
        ctx = {"groups":grp}
        ctx["groups_select"] = "none"
        if request.method == "POST":
            ctx["groups_select"] = request.POST.get("groups_select", "none")

        template = get_template("add_images/get_groups.html")
        content = template.render(ctx)
        return JsonResponse({"html":content})

def NewImage(request):
    if request.method == 'GET':
        for target_list in request.GET.items():
            print(target_list)
        ctx = {}
        # ctx["img"] = request.GET["file"]

        template = get_template("add_images/new_image.html")
        content = template.render(ctx)
        return JsonResponse({"html":content})

@csrf_exempt
def NewGroup(request):
    if request.user.is_superuser:
        form = imagesForms.GroupForm()
        ctx = {}
        if request.method == 'POST':
            form = imagesForms.GroupForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                print("is_valid")
                print(form.save())
                return JsonResponse({"success":True})
            
        ctx['form'] = form
        template_link ="add_images/new_group.html"
        template = get_template(template_link )
        content = template.render(ctx)
        return JsonResponse({"html":content})