from agatka.useful import *
import images.models as imagesForms
import images.forms as imagesForms
        
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
        ctx["categories_select"] = request.POST.get("categories_select") if request.method == 'POST' and 'categories_select' else 'none'
        ctx["groups_select"] = request.POST.get("groups_select") if request.method == 'POST' and 'groups_select' else 'none'
        if request.method == 'POST':
            for item in request.POST.items():
                ctx[item[0]] = item[1]
                print(item)
            print("files")
            for item in request.FILES.items():
                ctx[item[0]] = item[1]
                print(item)
                
            form = imagesForms.GroupForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                print("saved")
            else:
                print("not saved")
                print("form:",form)




        ctx["categories"] = imagesForms.Category.objects.all()
        return render(request, "add_images/main.html", ctx)








@csrf_exempt
def GetGroups(request):
    if request.method == 'GET':
        category = request.GET["category"]
        cat = imagesForms.Category.objects.filter(id=category)[0]
        grp = imagesForms.Group.objects.filter(category=cat)
        ctx = {"groups":grp}
        if request.method == 'GET':
            for item in request.GET.items():
                ctx[item[0]] = item[1]
            for item in request.FILES.items():
                ctx[item[0]] = item[1]

        template = get_template("add_images/get_groups.html")
        content = template.render(ctx)
        return JsonResponse({"html":content})

@csrf_exempt
def GetImages(request):
    if request.method == 'GET':
        category = request.GET["category"]
        cat = imagesForms.Category.objects.filter(id=category)[0]
        grp = imagesForms.Group.objects.filter(category=cat)
        ctx = {"groups":grp}
        ctx["groups_select"] = request.GET["groups_select"]

        template = get_template("add_images/get_groups.html")
        content = template.render(ctx)
        return JsonResponse({"html":content})
def NewGroup(request):
    if request.user.is_superuser:
        form = imagesForms.GroupForm2()
        ctx = {}
        if request.method == 'GET':
            form = imagesForms.GroupForm2(data=request.GET, files=request.FILES)
            if form.is_valid():
                print("is_valid")
            else:
                print("files")
                print(form.files)
            
        ctx['form'] = form
        template_link ="add_images/new_group.html"
        template = get_template(template_link )
        content = template.render(ctx)

        if request.GET.get('pure_html',False):
            form = imagesForms.GroupForm2(data=request.GET, files=request.FILES)
            ctx['pure_html'] = request.GET.get('pure_html')
            if form.is_valid():
                form.save()
                print("saved")
            else:
                print("not saved")
                print("form:",form)
            return render(request, template_link , ctx)
        else:
            return JsonResponse({"html":content})