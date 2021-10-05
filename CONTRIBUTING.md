# I.M.W-DJANGO-APP
a DJANGO PROJECT

-----Why This App?-----
It is a django project, Designed on the concept of Online medical services. through this Web app patient can book their slot and fix their appointment with World's Best Doctors
..---NOTE-Any genuine contribution is appreciated and I will merge it definately .

-----Database---
currently this app uses django's builtin database sqlite .

----How Can I run this app On my local Machine----
step1--If you have allready installed Python,You just need to install Django (Django 3.1.1 recommended.)

step2-- fork this repository, open this project in your editor on your local machine.

step3--delete pycache , migrations , db.sqlite files (because they will generate automatically when you use this app on your local machine).

step4--Run python manage.py makemigrations and python manage.py migrate(for generating database files).

step5- run django-admin createsuperuser  give your name ,email password etc (for accessing admin panel of app).

step6--just run python manage.py runserver.




-------------------------What I actually Have Done---------------------
1)--install Python

2)--install django

3)--Create an project using django-admin startproject .

4)--Create an app- data.

5)--create a folder template ,in which all front end work is done with help of html , css , javascript and Bootstrape(content delivery network based framework).

6)--In urls.py of project(our project),I added all templates path .

7)--in views.py of Project , added handlelogin, handlelogout , signup functions for authentication purpose.

8)--In urls.py of data, I have added final template ,which is appointment letter provided to patient on succesfull booking of appointment.

9)--In views.py of data, created a Detail function for fethcing details of patient, and check that date is valid, Doctor is available, ask Time slot is not Given to any other patient etc.

10)--in models.py of data, added some required data fields such as Disease ,doctor date etc.

11)--In admin.py of data, added field ,filters, display list.



   








