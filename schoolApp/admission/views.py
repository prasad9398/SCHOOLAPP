from django.shortcuts import render
from admission.models import Student
from admission.forms import StudentModelForm
from admission.forms import VendorForm
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from admission.models import Teacher
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.


#function based views

@login_required
def homepage(request):
    return render(request,'index.html')

def logoutUser(request):
    return render(request,'logout.html')

@login_required
def addAdmission(request):
    form = StudentModelForm
    studentform = {'form':form}
    if request.method=='POST':
        form =  StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)

    return render(request,'admission/add-admission.html',studentform)


@login_required
def admissionReport(request):
    #get all the record from the table
    result = Student.objects.all(); #SELECT * FROM students
    #store it in dictionary students
    students = {'allstudents':result}
    return render(request,'admission/admission-report.html',students)

@login_required
def deleteStudent(request,id):
    s = Student.objects.get(id=id)# select * from admission_student where id=idvalue
    s.delete()
    return admissionReport(request)


@login_required
def updateStudent(request, id):
    s = Student.objects.get(id=id)
    form = StudentModelForm(instance=s)
    dict = {'form':form}
    if request.method=='POST':
        form =  StudentModelForm(request.POST, instance=s)
        if form.is_valid():
            form.save()
        return admissionReport(request)

    return render(request,'admission/update-admission.html',dict)



@login_required
def addVendor(request):
    form = VendorForm
    vform = {'form':form}
    if request.method=='POST':
        form =  VendorForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            a = form.cleaned_data['address']
            c = form.cleaned_data['contact']
            i = form.cleaned_data['item']
            dict = {"name":n,"address":a,"contact":c,"item":i}
        return render(request,'index.html',dict)

    return render(request,'admission/add-admission.html',vform)



#class based view
class FirstClassBasedView(View):
    def get(self, request):
        return HttpResponse("<h1>Hello ... this is my first class based view</h1>")


class TeacherRead(ListView):
    model = Teacher


class GetTeacher(DetailView):
    model = Teacher


class AddTeacher(CreateView):
    model = Teacher
    fields = ('name','exp','subject','contact')


class UpdateTeacher(UpdateView):
    model = Teacher
    fields = ('name','exp','subject','contact')

class DeleteTeacher(DeleteView):
    model = Teacher
    success_url = reverse_lazy('listteachers')
