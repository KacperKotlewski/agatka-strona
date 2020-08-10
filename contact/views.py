from agatka.useful import *
from .forms import MailingForm
from django.core.mail import *

def Contact(request):    
    ctx = set_navname("contact", base_context(request))
    ctx['form'] = MailingForm()
    TestMial(request, ctx)
    return render(request, "contact.html", ctx)

def TestMial(request, ctx):
    if request.method == 'POST':
        form = MailingForm(request.POST)
        if form.is_valid():
            try:
                template = get_template("email_respond_to_agat.html")
                context = {"message":form["message"].value(), "names" : form["names"].value(), "email" : form["email"].value() }
                content = template.render(context)
                
                headers = {'Reply-To': form["email"].value()}
                msg = EmailMessage(
                    form["topic"].value(), 
                    content,
                    "lyzewa2@gmail.com",
                    ["lyzewa2@gmail.com"],
                    headers=headers
                    )
                msg.content_subtype = "html"
                msg.send()
                messages.success(request, "Wysłano maila :D")
                return
            except:
                pass


        ctx['form'] = form
        messages.error(request, "Wystąpił jakiś problem. Nie wysłano maila, proszę spróbuj ponownie :)")