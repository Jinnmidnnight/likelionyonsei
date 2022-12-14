from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.utils import timezone

# Create your views here.

def home(request):
    company_form = CompanyForm()
    project_form = ProjectForm()

    company_list = Company.objects.order_by('?')
    project_list = Project.objects.order_by('-number', 'name')

    ctx = {
        'company_form':company_form,
        'project_form':project_form,
        'company_list':company_list,
        'project_list':project_list,
    }
    return render(request, 'home.html', ctx)

def alumni(request):
    all_members = Member.objects.all().order_by('-number')
    latest_num = all_members[0].number
    page = request.GET.get('page', latest_num)
    page = int(page or latest_num)
    members = Member.objects.filter(number=page).order_by('-status', 'name')
    member_form = MemberForm()
    ctx = {
        'members':members, 
        'member_form':member_form,
        'page':page,
        'latest_num':latest_num,
    }
    return render(request, 'alumni.html', ctx)

def recruit(request):
    if (request.method == 'POST'):
        form = RecruitForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('recruit')
    else:
        initial_data = {'url':'https://'}
        form = RecruitForm(initial=initial_data)
        # for user
        today = timezone.now()
        recruit_url = Recruit.objects.last()
        s_date = recruit_url.start_date
        e_date = recruit_url.end_date
        if (s_date > today or e_date < today):
            recruit_url = Recruit.objects.none()
        return render(request, 'recruit.html', {'form':form, 'recruit_url':recruit_url})

def contact(request):
    return render(request, 'contact.html')

def add_member(request):
    if (request.method == 'POST'):
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('alumni')

def add_company(request):
    if (request.method == 'POST'):
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('home')

def add_project(request):
    if (request.method == 'POST'):
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('home')

def page_not_found(request, exception):
    return render(request, '404.html')