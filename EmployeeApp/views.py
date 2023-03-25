from django.shortcuts import render, redirect

from .models import Employee

# Create your views here.

# Create Employee...
def home(request):
    return render(request,'home.html')


def insert_emp(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile_no = request.POST['mobile_no']
        address = request.POST['address']
        qualification=request.POST['qualification']
        data = Employee(first_name=first_name, middle_name=middle_name, last_name=last_name, email= email,mobile_no=mobile_no,address=address,qualification=qualification)
        data.save()
  
        return redirect('../show/')
    else:
        return render(request, 'insert.html')
# Retrieve Employees...

def show_emp(request):
    employees = Employee.objects.all()
    return render(request,'show.html',{'employees':employees} )

# Update Employees...

def edit_emp(request,pk):
   if request.method == 'POST':
        
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        mobile_no = request.POST.get('mobile_no')
        address = request.POST.get('address')
        qualification = request.POST.get('qualification')


        employees=Employee.objects.get(id=pk)
        employees.first_name=first_name
        employees.middle_name=middle_name
        employees.last_name=last_name
        employees.email=email
        employees.mobile_no=mobile_no
        employees.address=address
        employees.qualification=qualification
        employees.save()
        return redirect('../show')
   
   else:
    employees = Employee.objects.get(id=pk)

    context = {
            'employees': employees,
        }
   
   return render(request,'edit.html',context)
# Delete Employees...

def remove_emp(request,pk):
    employees = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employees.delete()
        return redirect('../show')

    context = {
        'employees': employees,
    }

    return render(request, 'delete.html', context)