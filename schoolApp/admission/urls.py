from django.urls import path

from admission.views import addAdmission
from admission.views import admissionReport
from admission.views import addVendor
from admission.views import deleteStudent
from admission.views import updateStudent
from admission.views import FirstClassBasedView
from admission.views import TeacherRead
from admission.views import GetTeacher
from admission.views import AddTeacher
from admission.views import UpdateTeacher
from admission.views import DeleteTeacher
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('newadm/', addAdmission),
    path('admreport/', admissionReport),
    path('newvendor/', addVendor),
    path('update/<int:id>', updateStudent),
    path('delete/<int:id>', deleteStudent),

    path('firstcbv/', login_required(FirstClassBasedView.as_view())),
    path('teacherslist/', login_required(TeacherRead.as_view()),name='listteachers'),
    path('getteacherdetails/<int:pk>/', login_required(GetTeacher.as_view()),name='getteacherinfo'),
    path('insertteacher/', login_required(AddTeacher.as_view())),
    path('updateteacher/<int:pk>/', login_required(UpdateTeacher.as_view())),
    path('deleteteacher/<int:pk>/', login_required(DeleteTeacher.as_view())),



    ]
