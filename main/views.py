from django.shortcuts import render,redirect
from .models import Content, Data, Skills
from django.contrib.auth import authenticate, login
from django.forms import modelformset_factory
from django.forms import TextInput, Textarea
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        detail = Content.objects.all()
        data = Data.objects.all()
        p = {'detail': detail, 'data':data}
        pdf = render_to_pdf('portfolio/pdf.html', p)
        return HttpResponse(pdf, content_type='application/pdf')


def detail(request):
    detail = Content.objects.all()
    data = Data.objects.all()
    skills = Skills.objects.all()
    return render(request,'portfolio/main.html',{'detail':detail,  'data':data, 'skills':skills})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('edit')
            else:
                return render(request, 'portfolio/signin.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'portfolio/signin.html', {'error_message': 'Invalid login'})

    return render(request, 'portfolio/signin.html')

@login_required(login_url='/login/')
def edit(request):
    detail = Content.objects.all()
    data = Data.objects.all()
    skills = Skills.objects.all()
    x = {
        'fname':TextInput(attrs={'class': 'field1'}),
        'dob': TextInput(attrs={'class': 'field1'}),
        'address': TextInput(attrs={'class': 'field1'}),
        'email': TextInput(attrs={'class': 'field1'}),
        'phone': TextInput(attrs={'class': 'field1'}),
        'linkedin': TextInput(attrs={'class': 'field1'}),
        'about': Textarea(attrs={'class': 'field4'}),
        'about2': Textarea(attrs={'class': 'field4'}),

    }
    y = {
        'topic': TextInput(attrs={'class': 'field2'}),
        'point1': Textarea(attrs={'class': 'field3'}),
        'point2': Textarea(attrs={'class': 'field3'}),
        'point3': Textarea(attrs={'class': 'field3'}),
    }
    z = {
        'area': TextInput(attrs={'class': 'field1'}),
        'percentage': TextInput(attrs={'class': 'field1'}),
    }
    Personal = modelformset_factory(Content, fields=('fname', 'phone', 'address', 'email', 'linkedin', 'about','about2', 'dob'), widgets=x, extra=0)
    DataFormSet = modelformset_factory(Data, fields=('topic', 'point1','point2','point3'), widgets=y,extra=2, max_num=10, can_delete=True)
    SkillsFormSet = modelformset_factory(Skills, fields=('area', 'percentage'), widgets=z,extra=2, max_num=10,can_delete=True)
    if request.method == 'POST':
        personalformset = Personal(request.POST, request.FILES, prefix='personalfield')
        formset = DataFormSet(request.POST, request.FILES, prefix='addfield')
        skillsformset = SkillsFormSet(request.POST, request.FILES, prefix='skillsfield')
        if personalformset.is_valid() and formset.is_valid() and skillsformset.is_valid():
            personalformset.save()
            formset.save()
            skillsformset.save()
        return render(request, 'portfolio/afterlogin.html',{'detail': detail, 'data':data, 'skills':skills})
    else:
        personalformset = Personal(prefix='personalfield')
        formset = DataFormSet(prefix='addfield')
        skillsformset = SkillsFormSet(prefix='skillsfield')

    return render(request, 'portfolio/edit.html',
                  {'personalformset': personalformset, 'formset': formset, 'skillsformset':skillsformset, 'detail': detail, 'data':data, 'skills':skills})

