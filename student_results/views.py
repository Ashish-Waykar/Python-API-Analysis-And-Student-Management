from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *
import os
import pandas as pd
# Create your views here.
def home(request):
    stu= student.objects.all()

    # getting source from external File
    file=os.path.join("students_complete.csv")
    df=pd.read_csv(file)[:200]
    styles = [
        dict(selector="tr:hover",
                    props=[("background", "black")]),
        dict(selector="th", props=[("color", "gray"),
                                   ("border", "1px solid #eee"),
                                   ("padding", "12px 35px"),
                                   ("border-collapse", "collapse"),
                                   ("background", "#00ccc"),
                                   ("text-transform", "uppercase"),
                                   ("font-size", "18px")
                                   ]),
        dict(selector="td", props=[("color", "red"),
                                   ("border", "1px solid #eee"),
                                   ("padding", "12px 35px"),
                                   ("border-collapse", "collapse"),
                                   ("font-size", "15px")
                                   ]),
        dict(selector="table", props=[
                                        ("font-family" , 'Arial'),
                                        ("margin" , "25px auto"),
                                        ("border-collapse" , "collapse"),
                                        ("border" , "1px solid #eee"),
                                        ("border-bottom" , "2px solid #00cccc"),
                                          ]),
    dict(selector="caption", props=[("caption-side", "bottom")])
    ]
    red=df.style.set_table_styles(styles).hide_index().set_caption("Designed by Ashish Waykar").bar(subset=['math_score', 'reading_score'],color="#D9A9A9").to_html()

    df_json = pd.read_json(os.path.join("pincodes_API_Dataset.json"))[:200]
    # df_json = pd.read_json("https://raw.githubusercontent.com/ozlerhakan/mongodb-json-files/master/datasets/students.json", lines=True)

    red_json=df_json.style.set_table_styles(styles).set_caption("Designed by Ashish Waykar").to_html()

    context={
    'stu':stu,
    'student':red,
    'red_json':red_json
    }
    return render(request,"home.html",context)

def student_del(request,s_roll):
    stu= student.objects.get(s_roll=s_roll)
    stu.delete()
    return redirect('home_student')


def create_stu(request):
    if request.method=='POST':
        form=CreateStudent(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_student')
    create=CreateStudent()
    context={'create':create,}
    return render(request,'Student/Add_Student.html',context)


def edit_stu(request,s_roll):
    if request.method=='POST':
        form=EditStudent(request.POST)
        if form.is_valid():
            data= student.objects.get(s_roll=s_roll)
            data.s_name=form.cleaned_data['s_name']
            data.branch=form.cleaned_data['branch']
            data.year=form.cleaned_data['year']
            data.mail=form.cleaned_data['mail']
            data.mobile=form.cleaned_data['mobile']
            data.save()
            return redirect('home_student')
    stu= student.objects.get(s_roll=s_roll)
    context={'stu':stu}
    return render(request,'Student/Edit_Student.html',context)



# Results CRUD
def all_results(request):
    res= result.objects.all()
    context={
    'results':res,
    }
    return render(request,"Result/All_Results.html",context)

def result_del(request,s_roll):
    res= result.objects.get(s_roll=s_roll)#s_roll==id Of Student Object
    res.delete()
    return redirect('all_results')


def create_result(request):
    if request.method=='POST':
        form=CreateResult(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_results')
    create=CreateResult()
    context={'create':create,}
    return render(request,'Result/Add_Result.html',context)


def edit_result(request,id):
    stu= student.objects.get(id=id)
    if request.method=='POST':
        form=EditStudent(request.POST,request.FILES)
        if form.is_valid():
            print(form)
            data= result.objects.get(reg_no=stu)
            data.name=form.cleaned_data['name']
            data.branch=form.cleaned_data['branch']
            data.year=form.cleaned_data['year']
            data.s_marksheet=form.cleaned_data['s_marksheet']
            data.save()
            return redirect('all_results')
    res= result.objects.get(reg_no=stu)
    context={'result':res}
    return render(request,'Result/Edit_Result.html',context)
