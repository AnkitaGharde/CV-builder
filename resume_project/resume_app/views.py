from django.shortcuts import render,redirect
from .models import Resume
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required


from io import BytesIO
from django.views import View
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from html import escape
#==============================================================================
# Create your views here.
def index(request):
    return render(request,'resume_app/index.html')


@login_required(login_url='login')
def make_cv(request):
    if request.method == "POST":
        # user_profile = request.POST.get('user_profile')
        Name = request.POST.get('Name')

        email = request.POST.get('email')
        address=request.POST.get('address')
        phone = request.POST.get('phone')
        careerObj = request.POST.get('careerObj')
        collegeName=request.POST.get('collegeName')
        course = request.POST.get('course')
        year_of_pass=request.POST.get('year_of_pass')
        percentage=request.POST.get('percentage')
        project = request.POST.get('project')
        technical_skills = request.POST.get('technical_skills')
        profile = request.POST.get('profile')
        company = request.POST.get('company')


        Resume(Name=Name, email=email,address=address, phone=phone, careerObj=careerObj,collegeName=collegeName,course=course,year_of_pass=year_of_pass,percentage=percentage,project=project,technical_skills=technical_skills,profile=profile,company=company).save()

        # return HttpResponse('Great ,Resume successfully created')
        return render(request, 'resume_app/show_cv.html')
    else:
        return render(request,'resume_app/make_cv.html')


# def show_cv(request,id):
#     re = Resume.objects.get(pk=id)
#     return render('resume_app/show_cv.html',{"re":re})

# def show_cv(request):
#     return redirect(show_cv)

def show_cv(request):
    return redirect(show_cv)



# @csrf_exempt
# def cv(request,id):
#     re=Resume.objects.get(pk=id)
#     return render(request,'resume_app/cv.html',{"usr_cv":re})


#----------------------------------------login views-------------------------------------------------------------

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('login')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'resume_app/signup_login/signup.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect(index)
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('make_cv')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'resume_app/signup_login/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('index')

# @csrf_exempt
# def get_resume(request,id):
#     user_profile=Resume.objects.get(pk=id)
#     return render(request,'resume_app/get_resume.html',{"user_profile":user_profile})

#===================================================================================
#-------------------------------pdf views----------------------------------------------------------------


def render_to_pdf(template_src,context_dict={}):

    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None




# Opens up page as PDF
class ViewPDF(View):
    def get(self, request, id,*args, **kwargs):
        template = get_template(
            'resume_app/get_resume.html')
        usr_cv=Resume.objects.order_by('-id')[0]
        pdf = render_to_pdf('resume_app/get_resume.html', {"usr_cv":usr_cv})
        return HttpResponse(pdf, content_type='application/pdf')
usr_cv={
     "Name":'Name',
     "email":'email',
}

# Automaticly downloads to PDF file
# class DownloadPDF(View):
#     def get(self, request, *args, **kwargs):
#
#
#         pdf = render_to_pdf('resume_app/get_resume.html', usr_cv)
#
#         response = HttpResponse(pdf, content_type='application/pdf')
#         filename = "resume_%s.pdf" % ("12341231")
#         content = "attachment; filename='%s'" % (filename)
#         response['Content-Disposition'] = content
#         return response





