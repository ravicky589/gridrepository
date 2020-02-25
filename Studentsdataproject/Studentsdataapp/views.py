from django.shortcuts import render,redirect
from .models import StudentsData

def home_view(request):
    students = StudentsData.objects.all()
    context = {'students':students}
    return render(request,'studentsdata/homepage.html',context)

def add_student_view(request):
    return render(request,'studentsdata/addstudents.html')

def inserting_data_view(request):
    roll = request.POST.get('roll')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    school = request.POST.get('school')
    cls = request.POST.get('cls')
    section = request.POST.get('section')
    telugu = request.POST.get('telugu')
    hindi = request.POST.get('hindi')
    english = request.POST.get('english')
    maths = request.POST.get('maths')
    science = request.POST.get('science')
    social = request.POST.get('social')

    data = StudentsData(
        roll_number=roll,
        first_name=fname,
        last_name=lname,
        email=email,
        school_name=school,
        class_name=cls,
        section_name=section,
        telugu_marks=telugu,
        hindi_marks=hindi,
        english_marks=english,
        maths_marks=maths,
        social_marks=social,
        science_marks=science
    )
    data.save()
    return redirect('/')


def updating_data_view(request,pk):
    student = StudentsData.objects.get(id=pk)
    context = {'student':student}
    return render(request, 'studentsdata/updatestudent.html', context)


def replacing_data_view(request,pk):
    student = StudentsData.objects.get(id=pk)
    student.roll_number = request.POST.get('roll')
    student.first_name = request.POST.get('fname')
    student.last_name =request.POST.get('lname')
    student.email = request.POST.get('email')
    student.school_name = request.POST.get('school')
    student.class_name = request.POST.get('cls')
    student.section_name = request.POST.get('section')
    student.telugu_marks = request.POST.get('telugu')
    student.hindi_marks = request.POST.get('hindi')
    student.english_marks = request.POST.get('english')
    student.maths_marks = request.POST.get('maths')
    student.science_marks = request.POST.get('science')
    student.social_marks = request.POST.get('social')
    student.save()
    return redirect('/')


def deleting_data_view(request,pk):
    student = StudentsData.objects.get(id=pk)
    student.delete()
    return redirect('/')
