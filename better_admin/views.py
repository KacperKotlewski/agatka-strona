from agatka.useful import *
import images.models as imagesModels
import images.forms as imagesForms
import django.forms as modelsformset_factory
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import SimpleUploadedFile
        
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

            ctx["categories_select"] = request.POST.get("categories_select", "none")
            ctx["groups_select"] = request.POST.get("groups_select", "none")
            template = get_template("add_images/main.html")
            content = template.render(ctx)
            return JsonResponse({"html":content})
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

        ctx["img_form"] = imagesForms.ImageForm2()
        template = get_template("add_images/get_groups.html")
        content = template.render(ctx)
        return JsonResponse({"html":content})

@csrf_exempt
def NewImage(request):
    if request.user.is_superuser:
        form = imagesForms.ImageForm()
        ctx = {}
        if request.method == 'POST':
            form = imagesForms.ImageForm(data=request.POST, files=request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Dodano zdjęcie")
                return JsonResponse({"success":True})
            else:
                messages.error(request, "Nie udało się dodać zdjęcia, spróbuj jeszcze raz lub skontaktuj się z deweloperem strony")
                try:
                    form.save()
                except Exception as e:
                    messages.error(request, "Error" + str(e))

            
        ctx['form'] = form
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
                form.save()
                messages.success(request, "Stworzono nową grupe")
                return JsonResponse({"success":True})
            else:
                messages.error(request, "Nie udało się utworzyć grupy, spróbuj jeszcze raz lub skontaktuj się z deweloperem strony")
                try:
                    form.save()
                except Exception as e:
                    messages.error(request, "Error" + str(e))
            
        ctx['form'] = form
        template_link ="add_images/new_group.html"
        template = get_template(template_link )
        content = template.render(ctx)
        return JsonResponse({"html":content})