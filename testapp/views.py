from django.shortcuts import render
from .forms import StudentRegistrationForm
from .models import StudentRagistration
from django.http import JsonResponse


# Create your views here.
def home_view(request):
    form=StudentRegistrationForm()
    data = StudentRagistration.objects.order_by('-id')[:5]  # Get the latest 5 records
    return render(request,'testapp/index.html',{'form':form,'data':data})
    # return render(request,'testapp/index.html',{'form':form})

# for add data via ajax add_views here.
def add_view(request):
    if request.method=='POST':
        form=StudentRegistrationForm(request.POST)
        if form.is_valid():
            sid=request.POST.get('stuid')
            name=request.POST['name']
            email=request.POST['email']
            password=request.POST['password']
            if sid=='':
                stubent=StudentRagistration(name=name,email=email,password=password)
            else:
                stubent=StudentRagistration(id=sid, name=name, email=email, password=password)
            stubent.save()
            #Return model data *************************
            # stu=StudentRagistration.objects.values()
            stu = StudentRagistration.objects.order_by('-id').values()[:5]
            print(stu)
            stu_list=list(stu)         

            return JsonResponse({'status':1,'stu_list':stu_list})           
        else:
            return JsonResponse({'status':0})   
            
# for Delete data via ajax delete_views here.
def delete_view(request):
    print("Hello1")
    if request.method == 'POST':
        id_to_delete = request.POST['sid']
        try:
            # Delete data with the given id
            stu = StudentRagistration.objects.get(pk = id_to_delete)
            stu.delete()     
            response_data = {'success': 1}
        except Exception as e:
            response_data = {'success': 0, 'error_message': str(e)}   
        return JsonResponse(response_data)

    return JsonResponse({'success': 0, 'error_message': 'Invalid request'})

# for Edit data via ajax edit_view here.
def edit_view(request):
    print("Hello1")
    if request.method == 'POST':
        id_to_edit = request.POST['sid']
        try:
            # Edit data with the given id
            print("Edit Id:") 
            print(id_to_edit)  
            student= StudentRagistration.objects.get(pk = id_to_edit)   
            stu_detail={"id":student.id,"name":student.name,"email":student.email,"password":student.password}
            response_data = {'stu_detail': stu_detail}
        except Exception as e:
            response_data = {'stu_detail': "", 'error_message': str(e)}   
        return JsonResponse(response_data)

    return JsonResponse({'stu_detail': 0, 'error_message': 'Invalid request'})
        