Stationery and Trade Management System

The project is designed using Django(Python). This system is named NIRVAAS by us.
The main objective of creating this system is, in our University, there is no systematic approach to trade books or other items. We used to face various issues while trying to obtain books from seniors. Hence, we decided to create this system.
The purpose of using Django to make this system is, since Django is a python language, it became easier for us to understand and learn Django, it's feature of customizable framework was a deciding factor for us.
Features of this project:
-> Allows for login/ registration for 3 types of users, Student, Stationery Staff, and System Adminstrator.
-> What can a student do?
	=> Bidding - Put an item on bid, bid on an item, view old bids
To run this project:
1. download pycharm professional version(with default settings). Install git from https://git-scm.com/download/win. To check installation run git --version in cmd.
2. on the first screen of pycharm, you will find an option get from version control, click on it.
3. over there, you will have two options repository url, github	
	3.1 if you choose repository url, paste this url in the url box -> https://github.com/Ishikashah2510/Fashion-Bazar.git
	4.2 if you use github, login with github account, select fahsion bazar project and click on clone
4. Now, in the terminal, run the following commands
	4.1 python manage.py makemigrations
	4.2 python manage.py migrate
	4.3 python manage.py runserver
5. After the old/new user homepage is displayed, you can either select new user to sign up or click on old user
	5.1 The added users are : 
			Email: 18bce081@nirmauni.ac.in 
			Password: Password123#
			User Type: Student
			
			Email: 18bce078@nirmauni.ac.in 
			Password: Password123#
			User Type: Student
			
			Email: shiv@gmail.com
			Password: Password123#
			User Type: Stationery Staff
			
			Email: ishika@gmail.com
			Password: Password123#
			User Type: System Admin
	5.2 For registration, a valid email ID is required for all users, with a 10 Digit phone number.
		For registration as a student, the email must be in the following format only. 
			{1-9}{0-9}{a-zA-Z}{a-zA-Z}{a-zA-Z}{0-9}{0-9}{0-9}@nirmauni.ac.in
			Ex: 18bce081@nirmauni.ac.in
		This was done specifically to show registration for our University's students.
		To change it for your university or for any other pattern, go to welcome->views.py->register(request)->line 39 and change the regex pattern.
6. The web framework can now be used without any issues.

For any problems or any other queries, feel free to email on 18bce081@nirmauni.ac.in.