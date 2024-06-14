from django.urls import path
from Employee.views import *
urlpatterns = [
    path('AddEmp',AddEmp),
    path('Show/',ShowEmp),
    path('del/<int:id>/', DelEmp),
    path('update/<int:id>/', Update),
    path('Update_Done/<int:id>/', Update_Done),

]
