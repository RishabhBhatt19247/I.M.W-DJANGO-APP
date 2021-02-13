from django.shortcuts import render,HttpResponse
from data.models import Detail
from django.contrib import messages
import random
import datetime

# Create your views here.
def alldetail(request):
    if request.method=='POST':
        name= request.POST['name']
        age= request.POST['age']
        date= request.POST['date']
        time= request.POST['time']
        email= request.POST['email']
        problem= request.POST['problem']
        doctor= request.POST['output']

        T=time[0:5]
        T=T.replace(":",".")
        T=float(T)

        currenttime=datetime.datetime.now()
        if currenttime.month<10:
            month="0"+str(currenttime.month)
        D=str(currenttime.year)+"-"+month+"-"+str(currenttime.day)
        ti=str(currenttime.hour)+"."+str(currenttime.minute)

        if date==D:
             if float(ti)>T:
                   messages.error(request,"❌ Sorry!,you are too late for today's date kindly try with another time or date ")
                   return render(request,'registerform.html')

        if(doctor=="Dr.Raju_Pokhral(Overweight_specialist)" or doctor=="Dr.Vaidh_Trivedi" or doctor=="Dr.Aadarsh_Srivastava" or doctor=="Dr.Samay_Srivastava(Reseacher_on_Hiv_vaccine)" or doctor=="Dr.Mahira_Khan" or doctor=="Dr.Kaushal_Tondon" or doctor=="Dr.Vaibhava_Trivedi(Researcher_on_corona_vaccine)" or doctor=="Dr.Aashay_Pal" or doctor=="Dr.Saurabh_Kumar" or doctor=="Dr.Aadarsh_Srivastava(Mental_Health_Specialist)" or doctor=="Dr.Ravi_Bishnoi" or doctor=="Dr.Rajendra_Kumar" or doctor=="Dr.Rakesh_Prakash(Cheif_surgeon)" or doctor=="Dr.Tisha_Sharma" or doctor=="Dr.Arvind_Shingh" or doctor=="Dr.Ramnath_Prakash" or doctor=="Dr.Md.Farhan" or doctor=="Dr.Mayank_Agarwal" or doctor=="Dr.Arun_Pratap(Bones_specialist)" or doctor=="Dr.Sarad_Sharma" or doctor=="Dr.Aman_Dinkar" or doctor=="Dr.Aman_Bansal" or doctor=="Dr.Amit_Trivedi" or doctor=="Dr.Aysha_Kumari" or doctor=="Dr.Md.Afsaan(Bladder_Cancer)" or doctor=="Dr.Tripti_Dibri(Breast_Cancer)" or doctor=="Dr.Himanshu_Kohli(Oral_Cancer)" or doctor=="Dr.Sandeep_Reddy" or doctor=="Dr.Vijya_Reddy" or doctor=="Dr.Prabhas_Malya"):
             if T>=14.00 or T<=6.00:
                   messages.error(request,"❌ Sorry!,Your Doctor is unavailable in this time.Kindly Choose time between 6am to 2pm")
                   return render(request,'registerform.html')
  
        if(doctor=="Dr.Sameer_Saini" or doctor=="Dr.Sambit_Saini(Kidney_Cancer)" or doctor=="Dr.Jaideep_Bhusan(Lung_Cancer)" or doctor=="Dr.Aakash_Dubey(Lymphoma_Cancer)" or doctor=="Dr.Anil_Bhatia(Melanoma_Cancer)" or doctor=="Dr.Raveena_Parmar" or doctor=="Dr.Gautam_Gulati" or doctor=="Dr.Priyanka_Verma" or doctor=="Dr.Radha_Shukla" or doctor=="Dr.Akshat_Jain" or doctor=="Dr.Rajiv_Shing" or doctor=="Dr.Prashant_Shingh" or doctor=="Dr.Rajesh_Trivedi" or doctor=="Dr.Ayush_Kumar" or doctor=="Dr.Faisal_Khan" or doctor=="Dr.Divya_Kumari"):
             if T<14.00 or T>=20.00:
                   messages.error(request,"❌ Sorry!,Your Doctor is unavailable in this time.Kindly Choose time between 2pm to 8pm")
                   return render(request,'registerform.html')

        if(doctor=="Dr.Raju_Pokhral(Overweight_specialist)" or doctor=="Dr.Samay_Srivastava(Reseacher_on_Hiv_vaccine)" or doctor=="Dr.Mahira_Khan" or doctor=="Dr.Kaushal_Tondon" or doctor=="Dr.Md.Afsaan(Bladder_Cancer)" or doctor=="Dr.Tripti_Dibri(Breast_Cancer)" or doctor=="Dr.Himanshu_Kohli(Oral_Cancer)"):
             place="All India Institute of Medical Science,New Delhi"
        elif(doctor=="Dr.Rajesh_Trivedi" or doctor=="Dr.Ayush_Kumar" or doctor=="Dr.Vaidh_Trivedi" or doctor=="Dr.Aadarsh_Srivastava" or doctor=="Dr.Faisal_Khan" or doctor=="Dr.Sambit_Saini(Kidney_Cancer)" or doctor=="Dr.Jaideep_Bhusan(Lung_Cancer)" or doctor=="Dr.Aakash_Dubey(Lymphoma_Cancer)" or doctor=="Dr.Anil_Bhatia(Melanoma_Cancer)"):
             place="All India Institute of Medical Science,Rishikesh" 
        elif(doctor=="Dr.Vaibhava_Trivedi(Researcher_on_corona_vaccine)" or doctor=="Dr.Aashay_Pal" or doctor=="Dr.Saurabh_Kumar" or doctor=="Dr.Aadarsh_Srivastava(Mental_Health_Specialist)" or doctor=="Dr.Ravi_Bishnoi" or doctor=="Dr.Sandeep_Reddy" or doctor=="Dr.Vijya_Reddy" or doctor=="Dr.Prabhas_Malya" or doctor=="Dr.Sameer_Saini"):
             place="Fortis Hospital,Mumbai"
        elif(doctor=="Dr.Rajiv_Shing" or doctor=="Dr.Prashant_Shingh" or doctor=="Dr.Rajendra_Kumar" or doctor=="Dr.Akshat_Jain" or doctor=="Dr.Rakesh_Prakash(Cheif_surgeon)" or doctor=="Dr.Tisha_Sharma" or doctor=="Dr.Arvind_Shingh"):
             place="Apollo Gleneagles Hospital,Kolkata"
        elif(doctor=="Dr.Radha_Shukla" or doctor=="Dr.Ramnath_Prakash" or doctor=="Dr.Md.Farhan" or doctor=="Dr.Mayank_Agarwal" or doctor=="Dr.Priyanka_Verma"):
             place="Fortis Hospital,Punjab"
        elif(doctor=="Dr.Arun_Pratap(Bones_specialist)" or doctor=="Dr.Sarad_Sharma" or doctor=="Dr.Aman_Dinkar" or doctor=="Dr.Gautam_Gulati"):
             place="G.S.V.M Medical College,Kanpur"
        elif(doctor=="Dr.Aman_Bansal" or doctor=="Dr.Amit_Trivedi" or doctor=="Dr.Aysha_Kumari" or doctor=="Dr.Raveena_Parmar"):
             place="City Hospital,Sultanpur"             
        else:
             place="Cooper hospital,Mumbai"
        appno=random.randint(111111111,999999999)
        doctor=doctor.replace("_"," ")

        if Detail.objects.filter(date=date,time=time,doctor=doctor).exists():
             messages.error(request,"❌ Sorry!,this time has allready alloted to another patient,kindly try with another date or time")
             return render(request,'registerform.html')
  
        detail= Detail(name=name,age=age,date=date,time=time,problem=problem,place=place,email=email,appno=appno,doctor=doctor)   
        detail.save()
          
        params={'NAME':name,'AGE':age,'DATE':date,'TIME':time,'PROBLEM':problem,'PLACE':place,'EMAIL':email,'DOCTOR':doctor,'APPNO':appno}
        messages.success(request,"✅Your Doctor Is available , ✅Asked date and time is valid and not alloted to anyone else ,  ✅GREAT NEWS!______You got the appointment please read the note in allotement letter carefully.")
        return render(request,'letter.html',params)  
    else:
        return HttpResponse("Technical error occur")
            