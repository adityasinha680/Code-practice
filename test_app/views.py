from django.shortcuts import render
from test_app.models import StudentInformation

# Create your views here.
def index(request):
	students = StudentInformation.objects.all()
	print(students)
	data = {
		'student':students
	}
	return render(request,'test_app/index.html',context=data)
